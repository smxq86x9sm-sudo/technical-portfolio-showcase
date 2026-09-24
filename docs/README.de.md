# Dokumentation (DE)

Dieses Repository ist eine **technische Visitenkarte** (Universidad de La Laguna / LinkedIn / Freelance).

## Was wird gezeigt

| Kompetenz | Nachweis |
|-----------|----------|
| **n8n + KI-Agenten** | Multi-Agent-Orchestrierung, Tools, Gmail / Telegram / Calendar |
| **RAG** | Google Drive → Embeddings (Gemini) → Pinecone → begründete Antworten |
| **Prozessautomatisierung** | E-Mail-Triage, Sprachassistent, geplante Backups |
| **Sicheres Design** | Keine Secrets im Repo; Credential-Isolation |
| **Produktionsnähe** | Importierbare Workflows, CI, Docker, Tests |

## Demo

```bash
# 1. Workflow-JSON prüfen
python scripts/validate_workflows.py

# 2. Tests
pip install -r requirements.txt && pytest -q

# 3. Docker
docker compose build
docker compose run --rm portfolio

# 4. lokales n8n (optional)
docker compose --profile n8n up n8n
# http://localhost:5678 → Import from File → n8n-workflows/*_clean.json
```

## Spanischer Markt (Teletrabajo)

Passend zu: *Ingeniero de Automatización*, *Especialista en Integración de IA / RAG*, *AI Solutions Architect*.

## Lizenz

MIT — siehe [LICENSE](../LICENSE).
