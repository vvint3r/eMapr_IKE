# Marketing Analytics KG – Usage Overview

## 1. Deploy the Knowledge Graph to Neo4j
1. Install Neo4j locally (Desktop/Docker) or create a Neo4j Aura instance.
2. Obtain Bolt connection details (e.g., `bolt://localhost:7687`) and credentials.
3. Push the KG with:
   ```bash
   scripts/kg_loader.py --kg artifacts/marketing_analytics_kg.json push-neo4j \
       --uri bolt://localhost:7687 --user neo4j --password <password> --wipe
   ```
4. Open the Neo4j Browser/Bloom to explore `MA_Node` vertices and relations.

## 2. Generate KG Node Embeddings
1. Install embedding deps: `pip install sentence-transformers chromadb` (optional if you only need JSON).
2. Run:
   ```bash
   scripts/node_embeddings.py --kg artifacts/marketing_analytics_kg.json \
       --out artifacts/kg_node_embeddings.json \
       --model sentence-transformers/all-MiniLM-L12-v2 \
       --persist-dir artifacts/chroma --collection marketing-analytics-nodes
   ```
3. Result: JSON file with vectors + optional Chroma collection for KG nodes.

## 3. Ingest Proprietary Documents
1. Choose ingestion settings; example end-to-end command:
   ```bash
   scripts/doc_ingest_pipeline.py \
       --kg artifacts/marketing_analytics_kg.json \
       --doc documents/my_source.md \
       --out artifacts/my_source.jsonl \
       --embed-model sentence-transformers/all-MiniLM-L12-v2 \
       --node-embeddings artifacts/kg_node_embeddings.json \
       --persist-dir artifacts/chroma \
       --collection marketing-analytics-content \
       --spacy-model en_core_web_sm
   ```
   - Install spaCy + the default model once if you plan to capture entities/keyphrases:
     ```bash
     pip install spacy
     python -m spacy download en_core_web_sm
     ```
   - Pass `--no-spacy` when you need heuristic-only enrichment (no additional model downloads).
2. Effects:
   - Chunks are matched to KG nodes via cosine similarity against node embeddings.
   - JSONL metadata mirrors your labeling schema.
   - Embeddings + metadata (summaries, learning-mode tags, tone signals, keyphrases, entities) are pushed to the specified Chroma collection for retrieval.

## 4. Retrieval & LLM Integration Plan
1. **Node-aware retrieval**: query Chroma for chunks filtered by `topic_path`, `knowledge_type`, etc., based on user question.
2. **Context assembly**: fetch top-N chunks + relevant KG node metadata (from Neo4j) to build prompts, dashboards, or docs.
3. **Feedback loop**: when new documents arrive, re-run the ingestion command to keep both the graph and vector store in sync.
4. **Optional managed vector DB**: swap Chroma for Qdrant/Pinecone by replacing the persistence layer inside the ingestion pipeline (the metadata schema stays identical).

## 5. Streamlit KG Explorer
1. Install dependencies inside the project virtualenv (already done once):
   ```bash
   source .venv/bin/activate
   pip install streamlit pyvis
   ```
2. Launch the UI (forward the chosen port if you are remote):
   ```bash
   streamlit run app/streamlit_app.py --server.port 8900 --server.headless true
   ```
3. Sidebar controls let you pick a focus node, traversal depth, and chunk query.
4. The main area shows:
   - **Graph + Details**: PyVis subgraph with lateral relationship summaries.
   - **Hierarchy Explorer**: Plotly sunburst + immediate-children table (top-down tree view).
   - **Chunk Retrieval**: semantic matches pulled from Chroma, including the auto-generated summary, learning/tone tags, keyphrases, entity list, and the raw label JSON for each chunk.
5. Environment variables (`KG_NEO4J_URI`, `KG_NEO4J_USER`, `KG_NEO4J_PASSWORD`, `KG_CHROMA_PATH`, `KG_CHROMA_COLLECTION`, `KG_JSON_PATH`) override the defaults when connecting to Aura or another deployment.

This flow keeps the KG authoritative in Neo4j while embeddings enable semantic retrieval for LLM-based applications.

## 6. Document Router & Multi-Format Ingestion
1. Supports `.txt`, `.md`, `.pdf` (text-based or scanned via OCR). Hooks are ready for future image/video/URL preprocessors.
2. Run the router to triage documents before chunking:
   ```bash
   source .venv/bin/activate
   PYTHONPATH=/home/wynt3r/makr:$PYTHONPATH scripts/doc_router.py --path documents --auto
   ```
   - `--path` can be a directory or a single file.
   - `--auto` ingests “accepted” docs immediately; omit to inspect decisions first.
3. Router outcomes:
   - **accept** – novel content; optionally ingested automatically.
   - **skip** – duplicate or too similar to existing coverage.
   - **review** – too short or no confident KG topic match; check manually.
4. All routing decisions and checksums are logged in `artifacts/router/manifest.json`, preventing reprocessing of the same material on future runs.

## 7. LangChain RAG Chat
1. Set an OpenAI API key in your environment: `export OPENAI_API_KEY=sk-...`
2. (Optional) choose a different chat model via `export RAG_MODEL_NAME=gpt-4.1-mini`.
3. Relaunch Streamlit – a “Chat with the Knowledge Graph” panel appears.
4. Conversations are grounded with:
   - Chroma chunk retrieval (semantic context).
   - KG facts pulled from Neo4j for cited nodes.
5. The UI logs chat history per session and displays sources/relationships alongside each answer.
