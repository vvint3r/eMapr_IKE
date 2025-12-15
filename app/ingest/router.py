from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
from sentence_transformers import SentenceTransformer

from app.ingest.preprocess import DocumentPreprocessor


@dataclass
class RouterConfig:
    kg_json_path: Path
    manifest_path: Path = Path("artifacts/router/manifest.json")
    min_length: int = 400
    similarity_threshold: float = 0.92
    embed_model: str = "sentence-transformers/all-MiniLM-L6-v2"


@dataclass
class RoutedDocument:
    source_path: Path
    text: str
    checksum: str
    matched_nodes: List[str]
    decision: str
    reason: str


class DocumentRouter:
    def __init__(self, config: RouterConfig) -> None:
        self.config = config
        self.preprocessor = DocumentPreprocessor(min_length=config.min_length)
        self.manifest = self._load_manifest()
        self.model = SentenceTransformer(config.embed_model)
        self.node_texts = self._load_nodes()
        self.node_embeddings = self.model.encode(
            [n["text"] for n in self.node_texts], convert_to_numpy=True
        )

    def _load_nodes(self) -> List[Dict]:
        data = json.loads(Path(self.config.kg_json_path).read_text(encoding="utf-8"))
        rows: List[Dict] = []

        def recurse(node: Dict) -> None:
            rows.append(
                {
                    "id": node["id"],
                    "text": node["name"] + " " + node.get("topic_path", ""),
                }
            )
            for child in node.get("children", []):
                recurse(child)

        for root in data.get("nodes", []):
            recurse(root)
        return rows

    def _load_manifest(self) -> Dict[str, Dict]:
        if self.config.manifest_path.exists():
            return json.loads(self.config.manifest_path.read_text())
        return {}

    def _save_manifest(self) -> None:
        self.config.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        self.config.manifest_path.write_text(json.dumps(self.manifest, indent=2))

    def route(self, path: Path) -> Optional[RoutedDocument]:
        text = self.preprocessor.load(path)
        if not text:
            return None

        checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if checksum in self.manifest:
            return RoutedDocument(path, text, checksum, [], "skip", "duplicate checksum")

        doc_embedding = self.model.encode(text[:4000], convert_to_numpy=True)
        similarities = self._cosine_similarity(doc_embedding, self.node_embeddings)
        matched_ids = [self.node_texts[i]["id"] for i, score in enumerate(similarities) if score > 0.45]

        if not matched_ids:
            decision = "review"
            reason = "No KG topic match"
        else:
            max_sim = max(similarities)
            if max_sim > self.config.similarity_threshold:
                decision = "skip"
                reason = "Too similar to existing content"
            else:
                decision = "accept"
                reason = f"Matches topics {', '.join(matched_ids[:3])}"

        routed = RoutedDocument(path, text, checksum, matched_ids, decision, reason)
        self.manifest[checksum] = {
            "path": str(path),
            "decision": decision,
            "reason": reason,
            "topics": matched_ids,
        }
        self._save_manifest()
        return routed

    @staticmethod
    def _cosine_similarity(vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
        vec_norm = vec / np.linalg.norm(vec)
        mat_norm = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)
        return mat_norm @ vec_norm
