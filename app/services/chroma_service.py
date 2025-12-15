from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import chromadb


class ChromaService:
    """Helper around a Chroma collection for chunk retrieval."""

    def __init__(self, persist_path: Path, collection_name: str) -> None:
        self._client = chromadb.PersistentClient(path=str(persist_path))
        self._collection = self._client.get_or_create_collection(name=collection_name)

    def search_chunks(
        self,
        query: str,
        n_results: int = 5,
        node_id: Optional[str] = None,
        topic_path: Optional[str] = None,
    ) -> List[Dict]:
        where: Dict[str, str] = {}
        if node_id:
            where["node_id"] = node_id
        if topic_path:
            where["topic_path"] = topic_path

        results = self._collection.query(
            query_texts=[query],
            where=where or None,
            n_results=n_results,
        )
        return self._format_results(results)

    def _format_results(self, results: Dict) -> List[Dict]:
        output: List[Dict] = []
        if not results.get("documents"):
            return output

        ids = results.get("ids", [[]])[0]
        chunks = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for chunk_id, text, metadata, distance in zip(ids, chunks, metadatas, distances):
            labels_raw = metadata.get("labels")
            labels = json.loads(labels_raw) if isinstance(labels_raw, str) else labels_raw
            output.append(
                {
                    "chunk_id": chunk_id,
                    "text": text,
                    "metadata": metadata,
                    "labels": labels or {},
                    "score": distance,
                }
            )
        return output
