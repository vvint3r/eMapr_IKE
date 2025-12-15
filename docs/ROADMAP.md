# Marketing Analytics KG – Current Roadmap

| Epic | Status | Description |
|------|--------|-------------|
| Streamlit hierarchy panel | ✅ done | Sunburst + child table for top-down browsing |
| LangChain RAG chat | ✅ done | Retrieval pipeline + chat UI |
| NLP metadata enrichment | ✅ done | spaCy-driven summaries, tone & learning tags surfaced in UI |
| Aura deployment | ⏳ pending | Mirror KG + UI configs to Neo4j Aura |
| Learning content layer | ⏳ pending | Map topics to Learn / Review / Reference artifacts |
| Multi-format preprocess/router | ✅ done | PDF/image/video/URL parsing + doc triage |

## Next Focus: Aura Deployment

1. **Provision & Sync**
   - Stand up a Neo4j Aura Free database and push the KG via `kg_loader.py`.
   - Capture required env vars (`KG_NEO4J_URI`, `KG_NEO4J_USER`, `KG_NEO4J_PASSWORD`, `KG_NEO4J_DATABASE`).
2. **Dual-Environment Config**
   - Allow Streamlit to switch between local Docker and Aura via sidebar toggle or env profile.
   - Document SSH tunneling / port-forwarding steps for remote data entry.
3. **Bloom / Desktop Alignment**
   - Export Bloom perspective + style JSON for remote analysts.
   - Note feature gaps vs. Desktop (e.g., visualization palettes) and provide workarounds.

