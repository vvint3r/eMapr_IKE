from __future__ import annotations

import json
from typing import Dict, List, Optional

from pyvis.network import Network


def build_graph(
    nodes: List[Dict],
    edges: List[Dict],
    focus_node_id: Optional[str] = None,
) -> Network:
    net = Network(
        height="650px",
        width="100%",
        bgcolor="#060b16",
        font_color="#f5f5f5",
        notebook=True,
        cdn_resources="in_line",
    )
    net.barnes_hut(gravity=-2500, central_gravity=0.08, spring_length=220, damping=0.10)
    net.set_options(
        json.dumps(
            {
                "edges": {"color": "#4c566a", "smooth": {"type": "dynamic"}},
                "nodes": {
                    "borderWidth": 2,
                    "font": {"size": 18, "face": "Inter"},
                    "shape": "dot",
                    "scaling": {"min": 12, "max": 42},
                },
                "interaction": {"hover": True, "dragNodes": True, "zoomView": True},
                "physics": {
                    "stabilization": {"iterations": 250},
                    "minVelocity": 0.75,
                },
            }
        )
    )

    for node in nodes:
        title_lines = [f"<b>{node.get('name', node['id'])}</b>"]
        if node.get("topic_path"):
            title_lines.append(f"<small>{node['topic_path']}</small>")
        if node.get("knowledge_types"):
            title_lines.append(f"Knowledge: {', '.join(node['knowledge_types'])}")
        if node.get("content_types"):
            title_lines.append(f"Content: {', '.join(node['content_types'])}")
        level = node.get("level")
        node_color = _level_color(level)
        if focus_node_id and node["id"] == focus_node_id:
            node_color = "#f72585"
        net.add_node(
            node["id"],
            label=node.get("name") or node["id"],
            title="<br/>".join(title_lines),
            color=node_color,
            value=level or 2,
        )

    for edge in edges:
        net.add_edge(
            edge["source"],
            edge["target"],
            label=edge.get("type", ""),
            color=_edge_color(edge.get("type")),
            arrows="to",
        )

    return net


def _level_color(level: int | None) -> str:
    palette = {
        1: "#4cc9f0",
        2: "#4361ee",
        3: "#4895ef",
        4: "#560bad",
        5: "#7209b7",
    }
    return palette.get(level, "#4895ef")


def _edge_color(rel_type: str | None) -> str:
    colors = {
        "REL_HIERARCHY": "#ffb703",
        "REL_INFLUENCES": "#8ecae6",
        "REL_FEEDS": "#fb8500",
        "REL_DEPENDS_ON": "#219ebc",
    }
    return colors.get(rel_type or "", "#adb5bd")
