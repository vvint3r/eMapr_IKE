#!/usr/bin/env python3
"""Marketing Analytics Knowledge Graph loader + utilities."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
def _safe_property(value: Any) -> Any:
    """Ensure Neo4j property compatibility."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        if all(isinstance(item, (str, int, float, bool)) or item is None for item in value):
            return value
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)

try:
    import networkx as nx  # type: ignore
except ImportError:  # pragma: no cover
    nx = None

try:
    from neo4j import GraphDatabase  # type: ignore
except ImportError:  # pragma: no cover
    GraphDatabase = None


@dataclass
class KGNode:
    """Flattened node structure."""

    id: str
    name: str
    level: int
    topic_path: str
    parent_id: Optional[str]
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KGEdge:
    """Relationship between nodes."""

    source: str
    target: str
    relation: str
    payload: Dict[str, Any] = field(default_factory=dict)


class MarketingAnalyticsKG:
    """In-memory representation of the marketing analytics knowledge graph."""

    def __init__(self, kg_path: Path) -> None:
        self.kg_path = kg_path
        self.raw: Dict[str, Any] = json.loads(kg_path.read_text())
        self.nodes: Dict[str, KGNode] = {}
        self.edges: List[KGEdge] = []
        self._flatten_nodes(self.raw.get("nodes", []))
        self._load_relationships()

    # ------------------------------------------------------------------
    def _flatten_nodes(
        self,
        nodes: Iterable[Dict[str, Any]],
        parent_id: Optional[str] = None,
    ) -> None:
        for node in nodes:
            node_id = node["id"]
            payload = {
                k: v
                for k, v in node.items()
                if k not in {"children", "id", "name", "level", "topic_path"}
            }
            record = KGNode(
                id=node_id,
                name=node["name"],
                level=node["level"],
                topic_path=node["topic_path"],
                parent_id=parent_id,
                payload=payload,
            )
            self.nodes[node_id] = record

            if parent_id:
                self.edges.append(
                    KGEdge(source=parent_id, target=node_id, relation="hierarchy")
                )

            for child in node.get("children", []):
                self._flatten_nodes([child], parent_id=node_id)

    # ------------------------------------------------------------------
    def _load_relationships(self) -> None:
        for rel in self.raw.get("relationships", []):
            self.edges.append(
                KGEdge(
                    source=rel["source"],
                    target=rel["target"],
                    relation=rel["type"],
                    payload={k: v for k, v in rel.items() if k not in {"source", "target", "type"}},
                )
            )

    # ------------------------------------------------------------------
    def summary(self) -> Dict[str, Any]:
        return {
            "graph_id": self.raw.get("graph_id"),
            "version": self.raw.get("version"),
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "dimensions": self.raw.get("dimensions", {}),
        }

    def get_node(self, node_id: str) -> KGNode:
        return self.nodes[node_id]

    def find_by_topic(self, topic_path: str) -> List[KGNode]:
        return [node for node in self.nodes.values() if node.topic_path == topic_path]

    def filter_by_application_context(self, context: str) -> List[KGNode]:
        return [
            node
            for node in self.nodes.values()
            if context in node.payload.get("application_contexts", [])
        ]

    def ancestors(self, node_id: str) -> List[KGNode]:
        chain: List[KGNode] = []
        cursor = self.nodes[node_id]
        while cursor.parent_id:
            parent = self.nodes[cursor.parent_id]
            chain.append(parent)
            cursor = parent
        return chain

    # ------------------------------------------------------------------
    def to_networkx(self) -> "nx.DiGraph":
        if nx is None:  # pragma: no cover
            raise RuntimeError("networkx is not installed. `pip install networkx`." )

        graph = nx.DiGraph(graph_id=self.raw.get("graph_id"), version=self.raw.get("version"))
        for node in self.nodes.values():
            graph.add_node(
                node.id,
                name=node.name,
                level=node.level,
                topic_path=node.topic_path,
                parent_id=node.parent_id,
                **node.payload,
            )
        for edge in self.edges:
            graph.add_edge(edge.source, edge.target, relation=edge.relation, **edge.payload)
        return graph

    # ------------------------------------------------------------------
    def export_neo4j_csv(self, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        nodes_path = output_dir / "nodes.csv"
        edges_path = output_dir / "edges.csv"

        node_fields = [
            "id",
            "name",
            "level",
            "topic_path",
            "parent_id",
            "knowledge_types",
            "content_types",
            "application_contexts",
            "skill_dimensions",
        ]
        with nodes_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=node_fields)
            writer.writeheader()
            for node in self.nodes.values():
                payload = node.payload
                writer.writerow(
                    {
                        "id": node.id,
                        "name": node.name,
                        "level": node.level,
                        "topic_path": node.topic_path,
                        "parent_id": node.parent_id or "",
                        "knowledge_types": ";".join(payload.get("knowledge_types", [])),
                        "content_types": ";".join(payload.get("content_types", [])),
                        "application_contexts": ";".join(payload.get("application_contexts", [])),
                        "skill_dimensions": ";".join(payload.get("skill_dimensions", [])),
                    }
                )

        with edges_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["source", "target", "relation"])
            writer.writeheader()
            for edge in self.edges:
                writer.writerow(
                    {
                        "source": edge.source,
                        "target": edge.target,
                        "relation": edge.relation,
                    }
                )

    # ------------------------------------------------------------------
    def push_to_neo4j(
        self,
        uri: str,
        user: str,
        password: str,
        database: Optional[str] = None,
        wipe: bool = False,
    ) -> None:
        if GraphDatabase is None:  # pragma: no cover
            raise RuntimeError("neo4j-driver is not installed. `pip install neo4j` to enable push.")

        def sanitize_relation(name: str) -> str:
            cleaned = "".join(ch if ch.isalnum() else "_" for ch in name)
            cleaned = cleaned.upper()
            return f"REL_{cleaned or 'GENERIC'}"

        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session(database=database) as session:
            if wipe:
                session.run("MATCH (n:MA_Node) DETACH DELETE n")

            for node in self.nodes.values():
                payload = node.payload
                session.run(
                    """
                    MERGE (n:MA_Node {id:$id})
                    SET n.name=$name,
                        n.level=$level,
                        n.topic_path=$topic_path,
                        n.parent_id=$parent_id,
                        n.knowledge_types=$knowledge_types,
                        n.content_types=$content_types,
                        n.application_contexts=$application_contexts,
                        n.skill_dimensions=$skill_dimensions,
                        n.kpis=$kpis,
                        n.tools=$tools,
                        n.stakeholders=$stakeholders,
                        n.value_streams=$value_streams,
                        n.notes_ref=$notes_ref,
                        n.content_blueprints=$content_blueprints,
                        n.micro_assets=$micro_assets
                    """,
                    {
                        "id": node.id,
                        "name": node.name,
                        "level": node.level,
                        "topic_path": node.topic_path,
                        "parent_id": node.parent_id,
                        "knowledge_types": _safe_property(payload.get("knowledge_types", [])),
                        "content_types": _safe_property(payload.get("content_types", [])),
                        "application_contexts": _safe_property(payload.get("application_contexts", [])),
                        "skill_dimensions": _safe_property(payload.get("skill_dimensions", [])),
                        "kpis": _safe_property(payload.get("kpis", [])),
                        "tools": _safe_property(payload.get("tools", [])),
                        "stakeholders": _safe_property(payload.get("stakeholders", [])),
                        "value_streams": _safe_property(payload.get("value_streams", [])),
                        "notes_ref": _safe_property(payload.get("notes_ref", [])),
                        "content_blueprints": _safe_property(payload.get("content_blueprints", [])),
                        "micro_assets": _safe_property(payload.get("micro_assets", [])),
                    },
                )

            for edge in self.edges:
                rel_type = sanitize_relation(edge.relation)
                payload = {k: _safe_property(v) for k, v in edge.payload.items()}
                session.run(
                    f"""
                    MATCH (src:MA_Node {{id:$source}}), (tgt:MA_Node {{id:$target}})
                    MERGE (src)-[r:{rel_type} {{relation:$relation}}]->(tgt)
                    SET r += $payload
                    """,
                    {
                        "source": edge.source,
                        "target": edge.target,
                        "relation": edge.relation,
                        "payload": payload,
                    },
                )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Marketing Analytics KG utilities")
    parser.add_argument("--kg", type=Path, required=True, help="Path to marketing_analytics_kg.json")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("info", help="Show summary stats")

    filter_parser = sub.add_parser("filter", help="Filter nodes by application context")
    filter_parser.add_argument("--context", required=True)

    ancestors_parser = sub.add_parser("ancestors", help="Show ancestor chain for a node")
    ancestors_parser.add_argument("--node", required=True)

    export_parser = sub.add_parser("export-neo4j", help="Write Neo4j bulk-import CSVs")
    export_parser.add_argument("--out", type=Path, required=True)

    push_parser = sub.add_parser("push-neo4j", help="Write nodes/edges directly to Neo4j")
    push_parser.add_argument("--uri", required=True, help="Neo4j bolt URI, e.g. bolt://localhost:7687")
    push_parser.add_argument("--user", required=True)
    push_parser.add_argument("--password", required=True)
    push_parser.add_argument("--database", default=None)
    push_parser.add_argument("--wipe", action="store_true", help="Delete existing MA_Node graph before push")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    kg = MarketingAnalyticsKG(args.kg)

    if args.command == "info":
        print(json.dumps(kg.summary(), indent=2))
    elif args.command == "filter":
        nodes = [node.id for node in kg.filter_by_application_context(args.context)]
        print(json.dumps(nodes, indent=2))
    elif args.command == "ancestors":
        chain = [node.id for node in kg.ancestors(args.node)]
        print(json.dumps(chain, indent=2))
    elif args.command == "export-neo4j":
        kg.export_neo4j_csv(args.out)
        print(f"Exported {len(kg.nodes)} nodes and {len(kg.edges)} edges to {args.out}")
    elif args.command == "push-neo4j":
        kg.push_to_neo4j(
            uri=args.uri,
            user=args.user,
            password=args.password,
            database=args.database,
            wipe=args.wipe,
        )
        print(f"Pushed {len(kg.nodes)} nodes and {len(kg.edges)} edges to Neo4j at {args.uri}")
    else:  # pragma: no cover
        parser.error("Unknown command")


if __name__ == "__main__":
    main()
