#!/usr/bin/env python3
"""Generate embeddings for every KG node and optionally push to ChromaDB."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import List

from kg_loader import MarketingAnalyticsKG

try:
    from sentence_transformers import SentenceTransformer  # type: ignore
except ImportError:  # pragma: no cover
    SentenceTransformer = None

try:
    import chromadb  # type: ignore
except ImportError:  # pragma: no cover
    chromadb = None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Embed marketing analytics KG nodes")
    parser.add_argument("--kg", type=Path, required=True, help="Path to marketing_analytics_kg.json")
    parser.add_argument("--out", type=Path, required=True, help="JSON file to store node embeddings")
    parser.add_argument(
        "--model",
        default="sentence-transformers/all-MiniLM-L12-v2",
        help="SentenceTransformer model name",
    )
    parser.add_argument("--persist-dir", type=Path, default=None, help="Optional ChromaDB directory")
    parser.add_argument(
        "--collection",
        default="marketing-analytics-nodes",
        help="Chroma collection name (when --persist-dir is set)",
    )
    return parser


def compose_text(node) -> str:
    payload = node.payload
    description = payload.get("description", "")
    kpis = ", ".join(payload.get("kpis", []))
    tools = ", ".join(payload.get("tools", []))
    value_streams = ", ".join(payload.get("value_streams", []))
    return " \n".join(
        filter(
            None,
            [
                node.name,
                description,
                f"Topic: {node.topic_path}",
                f"KPIs: {kpis}" if kpis else "",
                f"Tools: {tools}" if tools else "",
                f"Value: {value_streams}" if value_streams else "",
            ],
        )
    )


def push_to_chroma(nodes, embeddings, persist_dir: Path, collection_name: str) -> None:
    if chromadb is None:  # pragma: no cover
        raise RuntimeError("chromadb is not installed. `pip install chromadb`.")
    client = chromadb.PersistentClient(path=str(persist_dir))
    collection = client.get_or_create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})
    collection.upsert(
        ids=[node.id for node in nodes],
        documents=[compose_text(node) for node in nodes],
        embeddings=embeddings,
        metadatas=[{"topic_path": node.topic_path} for node in nodes],
    )


def main() -> None:
    args = build_parser().parse_args()
    if SentenceTransformer is None:  # pragma: no cover
        raise RuntimeError("sentence-transformers is not installed. `pip install sentence-transformers`.")

    kg = MarketingAnalyticsKG(args.kg)
    nodes = list(kg.nodes.values())
    texts = [compose_text(node) for node in nodes]
    model = SentenceTransformer(args.model)
    embeddings = model.encode(texts, convert_to_numpy=True).tolist()

    payload = {
        "model": args.model,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "node_count": len(nodes),
        "nodes": [
            {
                "id": node.id,
                "topic_path": node.topic_path,
                "text": text,
                "embedding": vector,
            }
            for node, text, vector in zip(nodes, texts, embeddings)
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    if args.persist_dir:
        push_to_chroma(nodes, embeddings, args.persist_dir, args.collection)

    print(f"Embedded {len(nodes)} nodes with {args.model} -> {args.out}")


if __name__ == "__main__":
    main()
