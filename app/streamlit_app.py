from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Dict, List

import pandas as pd
import plotly.express as px

import streamlit as st
from streamlit.components.v1 import html

from app.config import AppConfig
from app.chat_service import MarketingRAG, RAGConfig
from app.services.chroma_service import ChromaService
from app.services.graph_builder import build_graph
from app.services.neo4j_service import Neo4jService


@st.cache_resource(show_spinner=False)
def get_services() -> tuple[AppConfig, Neo4jService, ChromaService | None]:
    config = AppConfig()
    neo = Neo4jService(
        config.neo4j_uri,
        config.neo4j_user,
        config.neo4j_password,
        database=config.neo4j_database,
    )
    chroma = None
    try:
        chroma = ChromaService(config.chroma_path, config.chroma_collection)
    except Exception as exc:  # pragma: no cover - optional dependency
        st.warning(f"Chroma collection unavailable: {exc}")
    return config, neo, chroma


@st.cache_data(show_spinner=False)
def load_hierarchy_dataframe(path: str | Path) -> pd.DataFrame:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    rows: List[Dict] = []

    def traverse(node: Dict, parent: str | None) -> None:
        rows.append(
            {
                "id": node["id"],
                "name": node["name"],
                "parent_id": parent or "",
                "topic_path": node.get("topic_path", node["name"]),
                "level": node.get("level"),
            }
        )
        for child in node.get("children", []):
            traverse(child, node["id"])

    for root in data.get("nodes", []):
        traverse(root, None)

    df = pd.DataFrame(rows)
    return df


def main() -> None:
    st.set_page_config(page_title="Marketing Analytics KG", layout="wide")
    st.title("Marketing Analytics Knowledge Graph")
    st.caption("Explore the taxonomy and retrieve labeled content chunks.")

    config, neo_service, chroma_service = get_services()
    rag_service: MarketingRAG | None = None
    if config.openai_api_key:
        os.environ["OPENAI_API_KEY"] = config.openai_api_key
        try:
            rag_service = MarketingRAG(
                RAGConfig(
                    chroma_path=config.chroma_path,
                    chroma_collection=config.chroma_collection,
                    neo4j_uri=config.neo4j_uri,
                    neo4j_user=config.neo4j_user,
                    neo4j_password=config.neo4j_password,
                    neo4j_db=config.neo4j_database,
                    model_name=config.rag_model_name,
                )
            )
        except Exception as exc:  # pragma: no cover
            st.warning(f"RAG chat unavailable: {exc}")
    try:
        hierarchy_df = load_hierarchy_dataframe(config.kg_json_path)
    except FileNotFoundError:
        hierarchy_df = pd.DataFrame()
        st.warning(f"Cannot find KG JSON at {config.kg_json_path}. Hierarchy view disabled.")

    nodes = neo_service.list_nodes(limit=500)
    if not nodes:
        st.error("No nodes returned from Neo4j. Ensure the KG is loaded.")
        return

    id_to_name = {n["id"]: n["name"] for n in nodes}
    node_options = {f"{n['name']} ({n['topic_path']})": n["id"] for n in nodes}
    option_labels = list(node_options.keys())

    with st.sidebar:
        st.header("Graph Controls")
        selected_label = st.selectbox("Focus node", option_labels, index=0)
        selected_node_id = node_options[selected_label]
        depth = st.slider("Traversal depth", min_value=1, max_value=3, value=config.default_graph_depth)
        chunk_limit = st.slider("Chunk results", 1, 10, value=config.default_chunk_limit)
        chunk_query = st.text_input("Chunk query", value=selected_label.split(" (")[0])
        restrict_node = st.checkbox("Restrict to selected node", value=True)
        topic_filter = None
        if not restrict_node:
            topic_options = sorted({n["topic_path"] for n in nodes if n.get("topic_path")})
            topic_filter = st.selectbox("Filter by topic", ["All"] + topic_options)
            if topic_filter == "All":
                topic_filter = None

    subgraph = neo_service.fetch_subgraph(selected_node_id, depth=depth)
    node_metadata = next((n for n in nodes if n["id"] == selected_node_id), None)

    col_graph, col_details = st.columns([3, 1])
    with col_graph:
        if subgraph["nodes"]:
            graph = build_graph(subgraph["nodes"], subgraph["edges"], selected_node_id)
            html_content = graph.generate_html(notebook=True)
            html(html_content, height=650, scrolling=True)
        else:
            st.info("No relationships found for this node.")

    with col_details:
        st.subheader("Node Details")
        if node_metadata:
            st.markdown(f"**Name:** {node_metadata.get('name', '')}")
            st.markdown(f"**Topic path:** `{node_metadata.get('topic_path')}`")
            if node_metadata.get("knowledge_types"):
                st.markdown(f"**Knowledge:** {', '.join(node_metadata['knowledge_types'])}")
            if node_metadata.get("content_types"):
                st.markdown(f"**Content:** {', '.join(node_metadata['content_types'])}")
        else:
            st.caption("Metadata unavailable for this node.")

        # Related lateral relationships
        st.markdown("---")
        st.markdown("**Related Topics**")
        related: Dict[str, List[str]] = {}
        name_lookup = {node["id"]: node["name"] for node in subgraph["nodes"]}
        for edge in subgraph["edges"]:
            counterpart = None
            if edge["source"] == selected_node_id:
                counterpart = name_lookup.get(edge["target"], edge["target"])
            elif edge["target"] == selected_node_id:
                counterpart = name_lookup.get(edge["source"], edge["source"])
            if counterpart:
                related.setdefault(edge["type"], []).append(counterpart)
        if related:
            for rel_type, names in related.items():
                st.markdown(f"*{rel_type}*: {', '.join(sorted(set(names)))}")
        else:
            st.caption("No lateral relationships in current view.")

    # Hierarchy / nested explorer
    if not hierarchy_df.empty:
        st.subheader("Hierarchy Explorer")
        tree_col, list_col = st.columns([2, 1])
        with tree_col:
            fig = px.sunburst(
                hierarchy_df,
                ids="id",
                names="name",
                parents="parent_id",
                hover_data=["topic_path", "level"],
            )
            fig.update_layout(margin=dict(t=10, l=0, r=0, b=10))
            st.plotly_chart(fig, use_container_width=True)
        with list_col:
            st.markdown("**Immediate Children**")
            child_df = hierarchy_df[hierarchy_df["parent_id"] == selected_node_id][
                ["name", "topic_path", "level"]
            ]
            if child_df.empty:
                st.caption("No children for this node.")
            else:
                st.dataframe(child_df.rename(columns={"name": "Node", "topic_path": "Topic Path", "level": "Lvl"}), use_container_width=True)

    st.subheader("Chunk Retrieval")
    effective_query = chunk_query.strip() or selected_label.split(" (")[0]
    if chroma_service and effective_query:
        results = chroma_service.search_chunks(
            effective_query,
            n_results=chunk_limit,
            node_id=selected_node_id if restrict_node else None,
            topic_path=topic_filter,
        )
        if not results:
            st.info("No matching chunks found.")
        for result in results:
            labels = json.dumps(result.get("labels", {}), indent=2)
            meta = result.get("metadata", {})
            summary = meta.get("summary")
            learning_modes = [m.strip() for m in (meta.get("learning_modes") or "").split(";") if m]
            tone_signals = [t.strip() for t in (meta.get("tone_signals") or "").split(";") if t]
            key_phrases = [kp.strip() for kp in (meta.get("key_phrases") or "").split(";") if kp]
            framework_tags = [ft.strip() for ft in (meta.get("framework_tags") or "").split(";") if ft]
            entities_raw = meta.get("entities_json")
            try:
                entities = json.loads(entities_raw) if entities_raw else []
            except json.JSONDecodeError:
                entities = []
            st.markdown(
                f"""
                <div style="border:1px solid #1f2937; padding:1rem; border-radius:12px; margin-bottom:0.75rem; background-color:#0f172a;">
                    <small>Score {result['score']:.3f} • Doc: {meta.get('doc_id')}</small>
                    <p style="margin-top:0.5rem;">{result['text']}</p>
                    <code style="display:block; white-space:pre-wrap;">{meta.get('topic_path')} • Node {meta.get('node_id')}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if summary:
                st.markdown(f"**Summary:** {summary}")
            if learning_modes or tone_signals or framework_tags or key_phrases:
                chips = []
                if learning_modes:
                    chips.append(f"Learning: {', '.join(learning_modes)}")
                if tone_signals:
                    chips.append(f"Tone: {', '.join(tone_signals)}")
                if framework_tags:
                    chips.append(f"Framework: {', '.join(framework_tags)}")
                if key_phrases:
                    chips.append(f"Key phrases: {', '.join(key_phrases[:6])}")
                st.caption(" • ".join(chips))
            if entities:
                with st.expander("Entities"):
                    st.json(entities)
            with st.expander("Labels JSON"):
                st.code(labels, language="json")
    else:
        if not chroma_service:
            st.info("Chroma metadata unavailable. Ensure the ingestion pipeline has produced artifacts/chroma.")
        else:
            st.info("Chunk query is empty. Enter a keyword above to run semantic search.")

    st.subheader("Chat with the Knowledge Graph")
    if rag_service:
        st.caption("Powered by LangChain RAG. Your OPENAI_API_KEY must be set.")
        st.session_state.setdefault("rag_history", [])
        st.session_state.setdefault("rag_display", [])

        for role, content in st.session_state["rag_display"]:
            st.chat_message(role).write(content)

        user_prompt = st.chat_input("Ask a marketing analytics question")
        if user_prompt:
            st.chat_message("user").write(user_prompt)
            try:
                result = rag_service.ask(user_prompt, history=st.session_state["rag_history"])
                answer = result["answer"]
                sources = result.get("sources", [])
                kg_context = result.get("kg_context")

                assistant_message = answer
                if sources:
                    bullet_lines = [
                        f"- {src.get('doc_id', src.get('source_path', 'chunk'))} → "
                        f"{src.get('topic_path', '')} ({src.get('node_id', 'N/A')})"
                        for src in sources
                    ]
                    assistant_message += "\n\n**Sources**\n" + "\n".join(bullet_lines)

                st.chat_message("assistant").write(assistant_message)
                if kg_context:
                    with st.chat_message("assistant"):
                        with st.expander("KG context"):
                            st.write(kg_context)

                st.session_state["rag_history"].append((user_prompt, answer))
                st.session_state["rag_display"].append(("user", user_prompt))
                st.session_state["rag_display"].append(("assistant", assistant_message))
            except Exception as exc:  # pragma: no cover
                st.error(f"Chat failed: {exc}")
    else:
        st.info("Set `OPENAI_API_KEY` and restart the app to enable chat.")


if __name__ == "__main__":
    main()
