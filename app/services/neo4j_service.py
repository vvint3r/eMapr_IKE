from __future__ import annotations

from typing import Dict, List, Optional

from neo4j import GraphDatabase


class Neo4jService:
    """Thin wrapper around the Neo4j driver for KG exploration."""

    def __init__(self, uri: str, user: str, password: str, database: Optional[str] = None) -> None:
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._database = database

    def close(self) -> None:
        if self._driver:
            self._driver.close()

    def list_nodes(self, limit: int = 200) -> List[Dict]:
        query = (
            "MATCH (n:MA_Node) "
            "RETURN n.id AS id, n.name AS name, n.topic_path AS topic_path "
            "ORDER BY toLower(n.name) LIMIT $limit"
        )
        return self._run_list(query, {"limit": limit})

    def fetch_subgraph(self, node_id: str, depth: int = 2, limit: int = 200) -> Dict[str, List[Dict]]:
        depth = max(1, min(int(depth), 4))
        nodes: Dict[str, Dict] = {}
        edges: Dict[str, Dict] = {}

        range_query = (
            "MATCH (start:MA_Node) WHERE start.id = $node_id "
            "CALL (start) { "
            f"MATCH p=(start)-[r*1..{depth}]-(m:MA_Node) "
            "RETURN p LIMIT $limit "
            "} RETURN p"
        )
        with self._driver.session(database=self._database) as session:
            results = session.run(range_query, {"node_id": node_id, "limit": limit})
            for record in results:
                path = record["p"]
                for node in path.nodes:
                    nodes[node["id"]] = self._format_node(node)
                for rel in path.relationships:
                    rel_id = f"{rel.start_node['id']}->{rel.end_node['id']}:{rel.type}"
                    edges[rel_id] = {
                        "source": rel.start_node["id"],
                        "target": rel.end_node["id"],
                        "type": rel.type,
                    }

        if node_id not in nodes:
            with self._driver.session(database=self._database) as session:
                record = session.run(
                    "MATCH (n:MA_Node {id:$node_id}) RETURN n",
                    {"node_id": node_id},
                ).single()
                if record:
                    nodes[node_id] = self._format_node(record["n"])

        return {"nodes": list(nodes.values()), "edges": list(edges.values())}

    def search_nodes(self, term: str, limit: int = 20) -> List[Dict]:
        query = (
            "MATCH (n:MA_Node) "
            "WHERE toLower(n.name) CONTAINS toLower($term) "
            "RETURN n.id AS id, n.name AS name, n.topic_path AS topic_path "
            "ORDER BY n.name LIMIT $limit"
        )
        return self._run_list(query, {"term": term, "limit": limit})

    def _run_list(self, query: str, params: Dict) -> List[Dict]:
        with self._driver.session(database=self._database) as session:
            results = session.run(query, params)
            return [dict(record) for record in results]

    @staticmethod
    def _format_node(node: Record) -> Dict:
        return {
            "id": node.get("id"),
            "name": node.get("name"),
            "topic_path": node.get("topic_path"),
            "level": node.get("level"),
            "content_types": node.get("content_types", []),
            "knowledge_types": node.get("knowledge_types", []),
            "application_contexts": node.get("application_contexts", []),
        }
