#!/usr/bin/env python3
"""Document chunking, labeling, and NLP enrichment for the marketing analytics KG."""

from __future__ import annotations

import argparse
import json
import logging
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, TYPE_CHECKING

# Ensure the repository root (containing the `app` package) is importable
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from kg_loader import MarketingAnalyticsKG

try:  # pragma: no cover
    from sentence_transformers import SentenceTransformer  # type: ignore
except ImportError:  # pragma: no cover
    SentenceTransformer = None

try:  # pragma: no cover
    import chromadb  # type: ignore
except ImportError:  # pragma: no cover
    chromadb = None

try:  # pragma: no cover
    import spacy  # type: ignore
except ImportError:  # pragma: no cover
    spacy = None

try:  # pragma: no cover
    from app.ingest.preprocess import DocumentPreprocessor as RouterPreprocessor  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    RouterPreprocessor = None

if TYPE_CHECKING:  # pragma: no cover
    from spacy.tokens import Doc

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
logger = logging.getLogger("doc_ingest_pipeline")

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
STOPWORDS = {
    "and",
    "the",
    "for",
    "that",
    "with",
    "from",
    "into",
    "your",
    "their",
    "about",
    "this",
    "these",
    "those",
    "which",
    "there",
    "while",
    "where",
    "when",
    "will",
    "shall",
    "should",
    "could",
    "might",
    "been",
    "have",
    "has",
    "had",
}

LEARNING_MODE_RULES = {
    "Learn": [
        "introduction",
        "primer",
        "how to",
        "foundational",
        "step-by-step",
        "tutorial",
        "playbook",
    ],
    "Review": [
        "summary",
        "recap",
        "checklist",
        "key takeaway",
        "revision",
        "cheat sheet",
    ],
    "Reference": [
        "reference",
        "lookup",
        "benchmark",
        "api",
        "glossary",
        "metric definition",
    ],
}

TONE_RULES = {
    "tutorial": ["walkthrough", "step", "how to", "guide", "playbook"],
    "case-study": ["case study", "case-study", "example", "client", "brand"],
    "strategic": ["strategy", "roadmap", "framework", "governance"],
    "tactical": ["campaign", "execution", "workflow", "automation"],
    "analytical": ["model", "analysis", "statistical", "regression", "experiment"],
    "technical": ["sql", "schema", "api", "lambda", "spark", "python"],
}

FRAMEWORK_RULES = {
    "Learning Outcomes": [
        "learning objective",
        "outcome",
        "competency",
        "performance indicator",
    ],
    "Prerequisites": [
        "prerequisite",
        "assumed prior",
        "before you begin",
        "foundation",
    ],
    "Instructional Content": [
        "concept",
        "framework",
        "mental model",
        "supportive information",
    ],
    "Learning Activities": [
        "activity",
        "exercise",
        "practice",
        "project",
        "simulation",
    ],
    "Assessment Strategy": [
        "assessment",
        "quiz",
        "rubric",
        "grading",
        "evaluation",
    ],
    "Sequence & Scaffolding": [
        "sequence",
        "scaffold",
        "phase",
        "stage",
        "backward design",
    ],
    "Metacognitive Support": [
        "reflection",
        "self-assessment",
        "metacognitive",
        "feedback loop",
    ],
    "Resources": [
        "resource",
        "reading",
        "tool",
        "software",
        "reference list",
    ],
}


@dataclass
class ChunkRecord:
    doc_id: str
    chunk_id: str
    text: str
    node_id: str
    topic_path: str
    confidence: float
    labels: Dict[str, List[str]]
    source_path: str
    summary: str = ""
    learning_modes: List[str] = field(default_factory=list)
    tone_signals: List[str] = field(default_factory=list)
    key_phrases: List[str] = field(default_factory=list)
    entities: List[Dict[str, str]] = field(default_factory=list)
    framework_tags: List[str] = field(default_factory=list)


@dataclass
class NodeIndex:
    model: str
    node_ids: List[str]
    topic_paths: List[str]
    embeddings: List[List[float]]
    norms: List[float]

    def best_match(self, vector: List[float]) -> Tuple[str, str, float]:
        v_norm = math.sqrt(sum(x * x for x in vector)) + 1e-12
        best_idx = 0
        best_score = -1.0
        for idx, node_vec in enumerate(self.embeddings):
            score = self._cosine(vector, v_norm, node_vec, self.norms[idx])
            if score > best_score:
                best_idx = idx
                best_score = score
        return self.node_ids[best_idx], self.topic_paths[best_idx], best_score

    @staticmethod
    def _cosine(
        vec_a: List[float],
        norm_a: float,
        vec_b: List[float],
        norm_b: float,
    ) -> float:
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        return dot / (norm_a * norm_b + 1e-12)


class NLPEnricher:
    """Extract entities, key phrases, summaries, and learning framework tags."""

    def __init__(self, model_name: Optional[str], disable: bool = False) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model_name = model_name
        self._nlp = self._load_model(model_name) if (not disable and model_name) else None

    def _load_model(self, model_name: Optional[str]):  # pragma: no cover - runtime dependency
        if not model_name:
            return None
        if spacy is None:
            self.logger.warning("spaCy is not installed; skipping advanced NLP enrichment.")
            return None
        try:
            return spacy.load(model_name)
        except Exception as exc:
            self.logger.warning(
                "Could not load spaCy model '%s' (%s). Run `python -m spacy download %s` to enable NER/keyphrases.",
                model_name,
                exc,
                model_name,
            )
            return None

    def enrich(self, text: str) -> Dict[str, Any]:
        doc = self._nlp(text) if self._nlp else None
        summary = summarize_text(text)
        entities = self._extract_entities(doc)
        key_phrases = self._extract_key_phrases(doc, text)
        learning_modes = self._infer_learning_modes(text)
        tone_signals = self._infer_tone(text)
        framework_tags = self._infer_framework_tags(text)
        return {
            "summary": summary,
            "entities": entities,
            "key_phrases": key_phrases,
            "learning_modes": learning_modes,
            "tone_signals": tone_signals,
            "framework_tags": framework_tags,
        }

    def _extract_entities(self, doc: Optional["Doc"]) -> List[Dict[str, str]]:
        if doc is None:
            return []
        allowed = {"ORG", "PERSON", "PRODUCT", "GPE", "NORP", "EVENT", "WORK_OF_ART", "FAC", "LAW", "LOC"}
        results: List[Dict[str, str]] = []
        for ent in doc.ents:
            if ent.label_ in allowed:
                text = ent.text.strip()
                if len(text) >= 2:
                    results.append({"text": text, "label": ent.label_})
            if len(results) >= 12:
                break
        return results

    def _extract_key_phrases(self, doc: Optional["Doc"], text: str) -> List[str]:
        phrases: List[str] = []
        if doc is not None:
            seen = set()
            for chunk in doc.noun_chunks:
                phrase = chunk.text.strip()
                cleaned = re.sub(r"\s+", " ", phrase)
                normalized = cleaned.lower()
                if (
                    4 <= len(cleaned) <= 60
                    and normalized not in seen
                    and not all(token in STOPWORDS for token in normalized.split())
                ):
                    seen.add(normalized)
                    phrases.append(cleaned)
                if len(phrases) >= 12:
                    break
        if not phrases:
            phrases = self._fallback_phrases(text)
        return phrases[:12]

    @staticmethod
    def _fallback_phrases(text: str) -> List[str]:
        tokens = re.findall(r"[A-Za-z][A-Za-z0-9\-/]+", text)
        lowered = [tok.lower() for tok in tokens if len(tok) > 4 and tok.lower() not in STOPWORDS]
        freq = Counter(lowered)
        return [word for word, _ in freq.most_common(10)]

    def _infer_learning_modes(self, text: str) -> List[str]:
        lowered = text.lower()
        modes = {
            mode
            for mode, keywords in LEARNING_MODE_RULES.items()
            if any(keyword in lowered for keyword in keywords)
        }
        if not modes:
            modes.add("Learn" if len(text.split()) > 120 else "Reference")
        return sorted(modes)

    def _infer_tone(self, text: str) -> List[str]:
        lowered = text.lower()
        tones = {
            tone
            for tone, keywords in TONE_RULES.items()
            if any(keyword in lowered for keyword in keywords)
        }
        return sorted(tones)

    def _infer_framework_tags(self, text: str) -> List[str]:
        lowered = text.lower()
        tags = {
            tag
            for tag, keywords in FRAMEWORK_RULES.items()
            if any(keyword in lowered for keyword in keywords)
        }
        return sorted(tags)


def summarize_text(text: str, max_sentences: int = 3, max_chars: int = 420) -> str:
    sentences = [s.strip() for s in SENTENCE_SPLIT_RE.split(text.strip()) if s.strip()]
    if not sentences:
        return text[:max_chars]
    summary = " ".join(sentences[:max_sentences])
    if len(summary) > max_chars:
        summary = summary[:max_chars].rsplit(" ", 1)[0] + "..."
    return summary


# ---------------------------------------------------------------------------
# Chunking helpers


def chunk_words(words: List[str], chunk_size: int, overlap: int) -> Iterable[List[str]]:
    if not words:
        return []
    stride = max(chunk_size - overlap, 1)
    for start in range(0, len(words), stride):
        piece = words[start : start + chunk_size]
        if not piece:
            break
        yield piece
        if start + chunk_size >= len(words):
            break


def chunk_text(text: str, chunk_size: int = 650, overlap: int = 150) -> List[str]:
    words = text.split()
    return [" ".join(block) for block in chunk_words(words, chunk_size, overlap)]


# ---------------------------------------------------------------------------
# Matching + labeling heuristics


def heuristic_match(chunk: str, kg: MarketingAnalyticsKG) -> Tuple[str, str, float]:
    lowered = chunk.lower()
    best = kg.get_node("MA-ROOT")
    best_score = 0
    for node in kg.nodes.values():
        topic_leaf = node.topic_path.split("/")[-1]
        tokens = topic_leaf.replace("_", " ").split()
        score = sum(1 for tok in tokens if tok and tok.lower() in lowered)
        if score > best_score:
            best = node
            best_score = score
    confidence = min(best_score / 3.0, 1.0)
    return best.id, best.topic_path, confidence


def inherit_labels(chunk: str, node_payload: Dict[str, Any]) -> Dict[str, List[str]]:
    labels: Dict[str, List[str]] = {
        "knowledge_type": node_payload.get("knowledge_types", []),
        "content_type": node_payload.get("content_types", []),
        "application_contexts": node_payload.get("application_contexts", []),
        "skill_dimensions": node_payload.get("skill_dimensions", []),
        "purpose_labels": [],
        "quality_status": ["Pending"],
        "compliance_tags": [],
    }
    lowered = chunk.lower()
    if "how to" in lowered or "step-by-step" in lowered:
        labels["purpose_labels"].append("Educational")
    if "gdpr" in lowered or "privacy" in lowered:
        labels["compliance_tags"].append("GDPR")
    return labels


def load_node_index(path: Path) -> NodeIndex:
    data = json.loads(path.read_text())
    nodes = data["nodes"]
    embeddings: List[List[float]] = [node["embedding"] for node in nodes]
    norms = [math.sqrt(sum(x * x for x in emb)) + 1e-12 for emb in embeddings]
    return NodeIndex(
        model=data["model"],
        node_ids=[node["id"] for node in nodes],
        topic_paths=[node["topic_path"] for node in nodes],
        embeddings=embeddings,
        norms=norms,
    )


def load_document_text(doc_path: Path, preprocessor: Optional[Any]) -> str:
    if preprocessor:
        loader = getattr(preprocessor, "load", None)
        processor = getattr(preprocessor, "preprocess", None)
        try:
            if callable(loader):
                text = loader(doc_path)
            elif callable(processor):
                text = processor(doc_path)
            else:
                text = None
        except Exception as exc:  # pragma: no cover - optional path
            logger.warning("Preprocessor failed for %s: %s", doc_path, exc)
            text = None
        if text:
            return text
    return doc_path.read_text(encoding="utf-8", errors="ignore")


# ---------------------------------------------------------------------------
# Pipeline


def ingest_document(
    doc_path: Path,
    kg: MarketingAnalyticsKG,
    chunk_size: int,
    overlap: int,
    enricher: NLPEnricher,
    preprocessor: Optional[Any] = None,
) -> List[ChunkRecord]:
    text = load_document_text(doc_path, preprocessor)
    if not text.strip():
        raise ValueError(f"No text extracted from {doc_path}")

    chunks = chunk_text(text, chunk_size, overlap)
    records: List[ChunkRecord] = []
    for idx, chunk in enumerate(chunks):
        node_id, topic_path, confidence = heuristic_match(chunk, kg)
        node_payload = kg.get_node(node_id).payload
        labels = inherit_labels(chunk, node_payload)
        enrichment = enricher.enrich(chunk)
        records.append(
            ChunkRecord(
                doc_id=doc_path.stem,
                chunk_id=f"{doc_path.stem}-{idx:03d}",
                text=chunk,
                node_id=node_id,
                topic_path=topic_path,
                confidence=confidence,
                labels=labels,
                source_path=str(doc_path),
                summary=enrichment["summary"],
                learning_modes=enrichment["learning_modes"],
                tone_signals=enrichment["tone_signals"],
                key_phrases=enrichment["key_phrases"],
                entities=enrichment["entities"],
                framework_tags=enrichment["framework_tags"],
            )
        )
    return records


def save_records(records: List[ChunkRecord], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record.__dict__, ensure_ascii=False) + "\n")


def apply_node_similarity(
    records: List[ChunkRecord],
    embeddings: List[List[float]],
    node_index: NodeIndex,
    kg: MarketingAnalyticsKG,
) -> None:
    for record, vector in zip(records, embeddings):
        node_id, topic_path, score = node_index.best_match(vector)
        record.node_id = node_id
        record.topic_path = topic_path
        record.confidence = score
        record.labels = inherit_labels(record.text, kg.get_node(node_id).payload)


def compute_embeddings(records: List[ChunkRecord], model_name: str) -> List[List[float]]:
    if SentenceTransformer is None:  # pragma: no cover
        raise RuntimeError("sentence-transformers is not installed. `pip install sentence-transformers`.")
    model = SentenceTransformer(model_name)
    texts = [record.text for record in records]
    return model.encode(texts, convert_to_numpy=True).tolist()


def flatten_labels(labels: Dict[str, List[str]]) -> Dict[str, str]:
    flat: Dict[str, str] = {}
    for key, values in labels.items():
        if isinstance(values, list):
            flat[key] = ";".join(str(v) for v in values if v)
        else:
            flat[key] = str(values)
    return flat


def push_to_chroma(
    records: List[ChunkRecord],
    embeddings: List[List[float]],
    persist_dir: Path,
    collection_name: str,
) -> None:
    if chromadb is None:  # pragma: no cover
        raise RuntimeError("chromadb is not installed. `pip install chromadb`.")

    client = chromadb.PersistentClient(path=str(persist_dir))
    collection = client.get_or_create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})

    def _join(values: List[str]) -> str:
        return ";".join(v for v in values if v)

    collection.upsert(
        ids=[record.chunk_id for record in records],
        documents=[record.text for record in records],
        embeddings=embeddings,
        metadatas=[
            {
                "doc_id": record.doc_id,
                "node_id": record.node_id,
                "topic_path": record.topic_path,
                "confidence": round(record.confidence, 4),
                "source_path": record.source_path,
                "summary": record.summary,
                "learning_modes": _join(record.learning_modes),
                "tone_signals": _join(record.tone_signals),
                "key_phrases": _join(record.key_phrases),
                "framework_tags": _join(record.framework_tags),
                "entities_json": json.dumps(record.entities, ensure_ascii=False),
                "labels": json.dumps(record.labels, ensure_ascii=False),
                **flatten_labels(record.labels),
            }
            for record in records
        ],
    )


# ---------------------------------------------------------------------------
# CLI


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Chunk, label, enrich, and push documents into the marketing analytics knowledge graph",
    )
    parser.add_argument("--kg", type=Path, required=True, help="Path to marketing_analytics_kg.json")
    parser.add_argument("--doc", type=Path, required=True, help="Path to the document to ingest")
    parser.add_argument("--out", type=Path, required=True, help="Path to the JSONL output file")
    parser.add_argument("--chunk-size", type=int, default=650)
    parser.add_argument("--overlap", type=int, default=150)
    parser.add_argument("--embed-model", default=None, help="SentenceTransformer model name for chunk embeddings")
    parser.add_argument(
        "--persist-dir",
        type=Path,
        default=None,
        help="ChromaDB persistence directory for vector storage (optional)",
    )
    parser.add_argument(
        "--collection",
        default="marketing-analytics-content",
        help="ChromaDB collection name (used when --persist-dir is provided)",
    )
    parser.add_argument(
        "--node-embeddings",
        type=Path,
        default=None,
        help="Optional path to KG node embeddings JSON; enables embedding-based node matching.",
    )
    parser.add_argument("--skip-jsonl", action="store_true", help="Skip writing JSONL output (vector-only mode)")
    parser.add_argument(
        "--spacy-model",
        default="en_core_web_sm",
        help="spaCy model used for NER/keyphrase enrichment (default: en_core_web_sm)",
    )
    parser.add_argument(
        "--no-spacy",
        action="store_true",
        help="Disable spaCy loading (heuristic-only metadata; avoids large model downloads)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    kg = MarketingAnalyticsKG(args.kg)
    node_index: Optional[NodeIndex] = None
    if args.node_embeddings:
        node_index = load_node_index(args.node_embeddings)

    embed_model_name = args.embed_model
    if node_index:
        if embed_model_name and embed_model_name != node_index.model:
            raise ValueError(
                f"Node embeddings were generated with {node_index.model}, "
                f"but --embed-model={embed_model_name}. Please align them."
            )
        if embed_model_name is None:
            embed_model_name = node_index.model

    preprocessor = RouterPreprocessor() if RouterPreprocessor else None
    enricher = NLPEnricher(
        model_name=None if args.no_spacy else args.spacy_model,
        disable=args.no_spacy,
    )

    records = ingest_document(
        args.doc,
        kg,
        args.chunk_size,
        args.overlap,
        enricher=enricher,
        preprocessor=preprocessor,
    )

    if not records:
        logger.warning("No chunks generated for %s", args.doc)
        return

    embeddings: Optional[List[List[float]]] = None
    if embed_model_name:
        embeddings = compute_embeddings(records, embed_model_name)

    if node_index:
        if embeddings is None:
            raise ValueError("Node similarity requires embeddings. Supply --embed-model or matching node model.")
        apply_node_similarity(records, embeddings, node_index, kg)

    if not args.skip_jsonl:
        save_records(records, args.out)

    if args.persist_dir:
        if embeddings is None:
            raise ValueError("Vector store push requested but no embeddings computed. Set --embed-model.")
        push_to_chroma(records, embeddings, args.persist_dir, args.collection)

    summary_parts = [f"processed {len(records)} chunks"]
    if not args.skip_jsonl:
        summary_parts.append(f"jsonl -> {args.out}")
    if embeddings is not None:
        summary_parts.append(f"embeddings model={embed_model_name}")
    if args.persist_dir:
        summary_parts.append(f"chroma dir={args.persist_dir}")
    if not args.no_spacy and enricher._nlp is not None:
        summary_parts.append(f"nlp-model={args.spacy_model}")
    print("; ".join(summary_parts))


if __name__ == "__main__":
    main()
