# Neo4j Aura Deployment Guide

This guide walks through provisioning a Neo4j Aura instance, loading the marketing analytics knowledge graph, and wiring the Streamlit explorer to switch between local Docker and Aura-hosted clusters.

---

## 1. Create an Aura Database

1. Sign in at [https://console.neo4j.io](https://console.neo4j.io) and choose **Create Database** → **Aura Free**.
2. Pick a region close to your workload, name the instance (e.g., `marketing-analytics-kg`), and confirm.
3. Aura generates a **Bolt URI**, **username**, and **password**. Copy them immediately; the password is only shown once (you can rotate later).

You should end up with a connection string similar to:

```
neo4j+s://<random-id>.databases.neo4j.io
```

The `neo4j+s` / `neo4j+ssc` prefixes enforce TLS, which is required for Aura.

---

## 2. Set Environment Variables

Update your `.env` (or shell exports) so the project detects both local and Aura profiles:

```bash
# Existing local defaults (optional overrides)
export KG_NEO4J_URI=bolt://localhost:7687
export KG_NEO4J_USER=neo4j
export KG_NEO4J_PASSWORD=neo4jkg123

# Aura profile (adds a second option to the Streamlit sidebar)
export KG_AURA_URI=neo4j+s://<random-id>.databases.neo4j.io
export KG_AURA_USER=neo4j        # or the custom user you created
export KG_AURA_PASSWORD=<your-aura-password>
export KG_AURA_DATABASE=neo4j    # Aura Free only exposes the default DB
export KG_AURA_PROFILE_NAME="Neo4j Aura (Prod)"
```

> Tip: if you manage more than two clusters, set `KG_CONNECTION_PROFILES_JSON` to a JSON array of `{ "name": "...", "uri": "...", "user": "...", "password": "...", "database": "..." }` and they will appear automatically in the sidebar selector.

Reload your shell (`source .venv/bin/activate` or restart Cursor) so the new variables take effect.

---

## 3. Push the KG into Aura

Aura is empty by default. Load the JSON taxonomy via the existing loader:

```bash
python scripts/kg_loader.py \
  --kg artifacts/marketing_analytics_kg.json \
  push-neo4j \
  --uri "$KG_AURA_URI" \
  --user "$KG_AURA_USER" \
  --password "$KG_AURA_PASSWORD" \
  --database "$KG_AURA_DATABASE" \
  --wipe
```

Notes:

- The `--wipe` flag clears any prior `MA_Node` graph before inserting the fresh taxonomy.
- Aura Free enforces a small write quota. If you hit rate limits, rerun the command after a minute; the loader is idempotent.

---

## 4. Use Aura from Streamlit

1. Ensure the environment variables in section 2 are set.
2. Launch the app (forward the port if running remotely):
   ```bash
   streamlit run app/streamlit_app.py --server.port 8900 --server.headless true
   ```
3. In the left sidebar, open **Connection** → **Neo4j profile** and pick the Aura profile. The UI will reconnect automatically and the caption will show the active URI.
4. All downstream features (PyVis graph, hierarchy, Chroma retrieval, LangChain chat) now operate against the Aura graph.

You can switch back to Local Docker at any time using the same selector—no code changes or restarts required.

---

## 5. Optional: Neo4j Desktop & Bloom

- **Neo4j Desktop:** Use the Aura Bolt URI and credentials from the console. Desktop handles the TLS certificate automatically.
- **Neo4j Bloom:** Aura Free includes Bloom Lite. Open the Aura console, click **Open Bloom**, and import the included perspective. Bloom Enterprise features (custom palettes, persistence) require a paid tier.

---

## 6. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Failed to establish secure connection` | Ensure you kept the `neo4j+s` (TLS) prefix in the URI. |
| `authentication failure` | Rotate the Aura password from the console and update `KG_AURA_PASSWORD`. |
| Streamlit still shows local nodes | Restart Streamlit after changing env vars or confirm the sidebar profile switch. |
| Loader timeout or rate limit | Aura Free throttles bursts. Re-run `push-neo4j`—the script resumes where it left off. |

With Aura online, the KG is reachable from anywhere with internet access, making it easier to share the explorer, RAG chat, or future automation with stakeholders.***


