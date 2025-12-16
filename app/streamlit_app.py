from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

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
def get_services(profile_name: str) -> tuple[AppConfig, Neo4jService, ChromaService | None]:
    config = AppConfig(profile_name=profile_name)
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


@st.cache_data(show_spinner=False)
def load_learning_blueprints(path: str | Path) -> Dict[str, Dict[str, Any]]:
    blueprint_path = Path(path)
    if not blueprint_path.exists():
        return {}
    try:
        with open(blueprint_path, "r", encoding="utf-8") as fh:
            payload = json.load(fh)
    except json.JSONDecodeError as exc:
        st.warning(f"Unable to parse learning blueprint file: {exc}")
        return {}
    entries = payload.get("nodes", [])
    return {entry["node_id"]: entry for entry in entries}


def main() -> None:
    st.set_page_config(page_title="Marketing Analytics KG", layout="wide")
    st.title("Marketing Analytics Knowledge Graph")
    st.caption("Explore the taxonomy and retrieve labeled content chunks.")

    profile_seed = AppConfig()
    profile_labels = [profile_seed.profile_label(name) for name in profile_seed.profile_names]
    profile_map = dict(zip(profile_labels, profile_seed.profile_names))

    sidebar = st.sidebar
    sidebar.header("Connection")
    selected_label = sidebar.selectbox("Neo4j profile", profile_labels, index=0)
    selected_profile = profile_map[selected_label]

    config, neo_service, chroma_service = get_services(selected_profile)
    try:
        hierarchy_df = load_hierarchy_dataframe(config.kg_json_path)
    except FileNotFoundError:
        hierarchy_df = pd.DataFrame()
        st.warning(f"Cannot find KG JSON at {config.kg_json_path}. Hierarchy view disabled.")
    learning_blueprints = load_learning_blueprints(config.learning_blueprint_path)

    nodes = neo_service.list_nodes(limit=500)
    if not nodes:
        st.error("No nodes returned from Neo4j. Ensure the KG is loaded.")
        return

    id_to_name = {n["id"]: n["name"] for n in nodes}
    node_options = {f"{n['name']} ({n['topic_path']})": n["id"] for n in nodes}
    option_labels = list(node_options.keys())

    sidebar.caption(f"Active profile: {config.profile_label(config.active_profile_name)}")
    sidebar.header("Graph Controls")
    selected_label = sidebar.selectbox("Focus node", option_labels, index=0)
    selected_node_id = node_options[selected_label]
    depth = sidebar.slider(
        "Traversal depth", min_value=1, max_value=3, value=config.default_graph_depth
    )
    chunk_limit = sidebar.slider("Chunk results", 1, 10, value=config.default_chunk_limit)
    chunk_query = sidebar.text_input("Chunk query", value=selected_label.split(" (")[0])
    restrict_node = sidebar.checkbox("Restrict to selected node", value=True)
    topic_filter = None
    if not restrict_node:
        topic_options = sorted({n["topic_path"] for n in nodes if n.get("topic_path")})
        topic_filter = sidebar.selectbox("Filter by topic", ["All"] + topic_options)
        if topic_filter == "All":
            topic_filter = None

    sidebar.header("RAG Chat Settings")
    rag_model_name = config.rag_model_name
    if not config.openai_api_key:
        sidebar.warning("OPENAI_API_KEY not set. Chat functionality disabled.")
    else:
        rag_model_name = sidebar.text_input(
            "RAG Model (e.g., gpt-4o-mini)", value=config.rag_model_name
        )

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

    st.subheader("Learning Blueprint")
    blueprint = learning_blueprints.get(selected_node_id)
    if not blueprint:
        st.info(
            f"No learning blueprint found for this node. Generate via `python scripts/learning_layer_builder.py --kg {config.kg_json_path} --out {config.learning_blueprint_path}`."
        )
    else:
        gap_summary = blueprint.get("gap_summary", {})
        coverage = gap_summary.get("coverage_index", 0)
        cog = blueprint.get("cognitive_profile", {})
        cols = st.columns([1, 1, 2])
        with cols[0]:
            st.metric("Status", blueprint.get("status", "n/a").replace("_", " ").title())
            st.caption(blueprint.get("status_reason", ""))
        with cols[1]:
            st.metric("Bloom Target", cog.get("bloom_primary", "—"))
            st.caption(f"SOLO: {cog.get('solo_target', '—')}")
        with cols[2]:
            st.caption("Learning Modes")
            st.write(", ".join(blueprint.get("learning_modes", [])) or "—")
            st.progress(min(max(coverage, 0), 1.0))
            if gap_summary.get("missing_sections"):
                st.caption(f"Needs: {', '.join(gap_summary['missing_sections'])}")

        learning_outcomes = blueprint.get("blueprint", {}).get("learning_outcomes", {})
        activities = blueprint.get("blueprint", {}).get("activities", [])
        assessments = blueprint.get("blueprint", {}).get("assessments", {})
        resources = blueprint.get("blueprint", {}).get("resources", {})
        metacognition = blueprint.get("blueprint", {}).get("metacognition", {})

        with st.expander("Learning Outcomes", expanded=True):
            st.write(learning_outcomes.get("summary", ""))
            objectives = learning_outcomes.get("objectives", [])
            if objectives:
                st.markdown("**Objectives**")
                for item in objectives:
                    st.markdown(f"- {item}")

        with st.expander("Prerequisites & Enablement"):
            prereq_topics = blueprint.get("prerequisites", {}).get("topics", [])
            if prereq_topics:
                st.markdown("**Prerequisites**")
                for topic in prereq_topics:
                    st.markdown(f"- `{topic['id']}` · {topic['name']}")
            next_topics = blueprint.get("enablement_path", {}).get("next_topics", [])
            if next_topics:
                st.markdown("**Enables**")
                for topic in next_topics:
                    st.markdown(f"- `{topic['id']}` · {topic['name']}")

        with st.expander("Learning Activities"):
            if not activities:
                st.caption("No recommended activities yet.")
            else:
                for activity in activities:
                    st.markdown(
                        f"**{activity.get('name')}** — {activity.get('type')} · Focus: {activity.get('focus')}\n\n{activity.get('description')}"
                    )

        with st.expander("Assessment Strategy"):
            formative = assessments.get("formative", [])
            summative = assessments.get("summative", [])
            if not (formative or summative):
                st.caption("No assessments defined yet.")
            else:
                if formative:
                    st.markdown("**Formative**")
                    for item in formative:
                        st.markdown(f"- {item.get('name')} ({item.get('type')}): {item.get('criteria')}")
                if summative:
                    st.markdown("**Summative**")
                    for item in summative:
                        st.markdown(f"- {item.get('name')} ({item.get('type')}): {item.get('criteria')}")

        with st.expander("Resources & Metacognition"):
            tool_list = resources.get("primary_tools", [])
            if tool_list:
                st.markdown("**Tools**")
                st.write(", ".join(tool_list))
            if resources.get("content_blueprints"):
                st.markdown("**Blueprint References**")
                for ref in resources["content_blueprints"]:
                    st.markdown(f"- {ref.get('reference')}: {ref.get('usage')}")
            if resources.get("micro_assets"):
                st.markdown("**Micro-assets**")
                st.write(", ".join(resources["micro_assets"]))
            if resources.get("references"):
                st.markdown("**Notes**")
                st.write(", ".join(resources["references"]))

            if metacognition.get("reflection_prompts"):
                st.markdown("**Reflection Prompts**")
                for prompt in metacognition["reflection_prompts"]:
                    st.markdown(f"- {prompt}")
            if metacognition.get("self_checks"):
                st.markdown("**Self-checks**")
                st.write(", ".join(metacognition["self_checks"]))

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
                    model_name=rag_model_name,
                )
            )
        except Exception as exc:  # pragma: no cover
            st.warning(f"RAG chat unavailable: {exc}")

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
