#!/usr/bin/env python3
"""Preprocess and route documents before ingestion."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from app.config import AppConfig
from app.ingest.router import DocumentRouter, RouterConfig


def run_ingestion(doc_path: Path) -> None:
    base = doc_path.name.replace(" ", "_")
    cmd = [
        "scripts/doc_ingest_pipeline.py",
        "--kg",
        "artifacts/marketing_analytics_kg.json",
        "--doc",
        str(doc_path),
        "--out",
        f"artifacts/{base}.jsonl",
        "--embed-model",
        "sentence-transformers/all-MiniLM-L12-v2",
        "--node-embeddings",
        "artifacts/kg_node_embeddings.json",
        "--persist-dir",
        "artifacts/chroma",
        "--collection",
        "marketing-analytics-content",
    ]
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Route documents before ingestion")
    parser.add_argument("--path", default="documents", help="Directory to scan")
    parser.add_argument("--auto", action="store_true", help="Automatically ingest accepted documents")
    args = parser.parse_args()

    cfg = AppConfig()
    router = DocumentRouter(
        RouterConfig(
            kg_json_path=cfg.kg_json_path,
            manifest_path=Path("artifacts/router/manifest.json"),
        )
    )

    root = Path(args.path)
    if root.is_file():
        targets = [root]
    else:
        targets = sorted(root.glob("**/*"))
    stats = {"accept": 0, "skip": 0, "review": 0}

    for path in targets:
        if path.is_dir():
            continue
        routed = router.route(path)
        if not routed:
            continue
        stats[routed.decision] += 1
        print(f"{path.name}: {routed.decision} ({routed.reason})")
        if routed.decision == "accept" and args.auto:
            try:
                run_ingestion(path)
            except subprocess.CalledProcessError as exc:
                print(f"Failed to ingest {path}: {exc}")

    print("\nRouting summary:")
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
