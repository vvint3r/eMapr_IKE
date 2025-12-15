from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """Configuration container for the Streamlit KG UI."""

    neo4j_uri: str = os.getenv("KG_NEO4J_URI", "bolt://localhost:7687")
    neo4j_user: str = os.getenv("KG_NEO4J_USER", "neo4j")
    neo4j_password: str = os.getenv("KG_NEO4J_PASSWORD", "neo4jkg123")
    neo4j_database: str | None = os.getenv("KG_NEO4J_DATABASE")

    chroma_path: Path = Path(os.getenv("KG_CHROMA_PATH", "artifacts/chroma"))
    chroma_collection: str = os.getenv("KG_CHROMA_COLLECTION", "marketing-analytics-content")

    node_embeddings_file: Path = Path(
        os.getenv("KG_NODE_EMBEDDINGS", "artifacts/kg_node_embeddings.json")
    )
    default_chunk_limit: int = int(os.getenv("KG_CHUNK_LIMIT", "5"))
    default_graph_depth: int = int(os.getenv("KG_GRAPH_DEPTH", "2"))
    kg_json_path: Path = Path(os.getenv("KG_JSON_PATH", "artifacts/marketing_analytics_kg.json"))
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    rag_model_name: str = os.getenv("RAG_MODEL_NAME", "gpt-4o-mini")
