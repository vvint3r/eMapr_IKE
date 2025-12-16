# Marketing Analytics KG – Current Roadmap

| Epic | Status | Description |
|------|--------|-------------|
| Streamlit hierarchy panel | ✅ done | Sunburst + child table for top-down browsing |
| LangChain RAG chat | ✅ done | Retrieval pipeline + chat UI |
| NLP metadata enrichment | ✅ done | spaCy-driven summaries, tone & learning tags surfaced in UI |
| Aura deployment | ✅ done | Dual-profile config + Aura loader/runbooks |
| Learning content layer | ✅ done | Blueprint generator + Streamlit learning panel |
| Blueprint coverage automation | ⏳ pending | Tie ingestion outputs to blueprint readiness scoring |
| Multi-format preprocess/router | ✅ done | PDF/image/video/URL parsing + doc triage |

## Next Focus: Blueprint Coverage Automation

1. **Coverage Signals**
   - Compare blueprint checklist items with doc-ingestion metadata (chunk counts, summaries, tone/learning tags).
   - Flag nodes lacking formative/summative evidence or missing prerequisite docs.
2. **Router Feedback Loop**
   - Update `doc_ingest_pipeline.py` / router manifest to log which blueprint sections each document fulfills.
   - Recommend priority topics when new documents land (e.g., “fills assessment gap for MA-CC-PAID”).
3. **UI Surfacing**
   - Add readiness badges + TODO counts next to each node in Streamlit.
   - Provide download/export of the coverage table for curriculum planning.

