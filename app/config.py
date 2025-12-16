from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass(frozen=True)
class ConnectionProfile:
    """Neo4j connection settings surfaced in the Streamlit UI."""

    name: str
    uri: str
    user: str
    password: str
    database: str | None = None


class AppConfig:
    """Configuration container for the Streamlit KG UI."""

    def __init__(self, profile_name: str | None = None) -> None:
        self.chroma_path: Path = Path(os.getenv("KG_CHROMA_PATH", "artifacts/chroma"))
        self.chroma_collection: str = os.getenv(
            "KG_CHROMA_COLLECTION", "marketing-analytics-content"
        )
        self.node_embeddings_file: Path = Path(
            os.getenv("KG_NODE_EMBEDDINGS", "artifacts/kg_node_embeddings.json")
        )
        self.default_chunk_limit: int = int(os.getenv("KG_CHUNK_LIMIT", "5"))
        self.default_graph_depth: int = int(os.getenv("KG_GRAPH_DEPTH", "2"))
        self.kg_json_path: Path = Path(
            os.getenv("KG_JSON_PATH", "artifacts/marketing_analytics_kg.json")
        )
        self.learning_blueprint_path: Path = Path(
            os.getenv("KG_LEARNING_BLUEPRINTS", "artifacts/learning_blueprints.json")
        )
        self.openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
        self.rag_model_name: str = os.getenv("RAG_MODEL_NAME", "gpt-4o-mini")

        self._profiles: Dict[str, ConnectionProfile] = self._build_profiles()
        if not self._profiles:
            raise RuntimeError("No Neo4j connection profiles configured.")

        self.profile_names: List[str] = list(self._profiles.keys())
        if profile_name and profile_name in self._profiles:
            self.active_profile_name = profile_name
        else:
            self.active_profile_name = self.profile_names[0]

        active = self._profiles[self.active_profile_name]
        self.neo4j_uri: str = active.uri
        self.neo4j_user: str = active.user
        self.neo4j_password: str = active.password
        self.neo4j_database: str | None = active.database

    # ------------------------------------------------------------------
    def _build_profiles(self) -> Dict[str, ConnectionProfile]:
        profiles: Dict[str, ConnectionProfile] = {}

        def add_profile(name: str, uri: str, user: str, password: str, database: str | None) -> None:
            profiles[name] = ConnectionProfile(
                name=name,
                uri=uri,
                user=user,
                password=password,
                database=database,
            )

        local_name = os.getenv("KG_LOCAL_PROFILE_NAME", "Local Docker")
        add_profile(
            local_name,
            os.getenv("KG_NEO4J_URI", "bolt://localhost:7687"),
            os.getenv("KG_NEO4J_USER", "neo4j"),
            os.getenv("KG_NEO4J_PASSWORD", "neo4jkg123"),
            os.getenv("KG_NEO4J_DATABASE"),
        )

        aura_uri = os.getenv("KG_AURA_URI")
        aura_user = os.getenv("KG_AURA_USER")
        aura_password = os.getenv("KG_AURA_PASSWORD")
        if aura_uri and aura_user and aura_password:
            add_profile(
                os.getenv("KG_AURA_PROFILE_NAME", "Neo4j Aura"),
                aura_uri,
                aura_user,
                aura_password,
                os.getenv("KG_AURA_DATABASE"),
            )

        extra_profiles = os.getenv("KG_CONNECTION_PROFILES_JSON")
        if extra_profiles:
            try:
                payload = json.loads(extra_profiles)
                for entry in payload:
                    name = entry.get("name")
                    uri = entry.get("uri")
                    user = entry.get("user")
                    password = entry.get("password")
                    if not all([name, uri, user, password]):
                        continue
                    database = entry.get("database")
                    add_profile(name, uri, user, password, database)
            except json.JSONDecodeError:
                # Fallback silently; invalid JSON should not break the UI
                pass

        return profiles

    # ------------------------------------------------------------------
    def profile_label(self, name: str) -> str:
        profile = self._profiles[name]
        return f"{profile.name} ({profile.uri})"

