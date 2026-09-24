# Demo — full checklist

Run these steps on a clean machine to verify the portfolio works.

## Prerequisites

- Python 3.12+
- Docker (optional, for compose)
- n8n instance (cloud or local) to **import** workflows

## 1. Clone and validate workflows

```bash
git clone https://github.com/smxq86x9sm-sudo/technical-portfolio-showcase.git
cd technical-portfolio-showcase

python scripts/validate_workflows.py
# Expected: All 6 workflow(s) OK
```

## 2. Run automated tests

```bash
pip install -r requirements.txt
pytest -q
# Expected: tests passed (JSON validity, no credentials blocks, expected files present)
```

## 3. Docker smoke

```bash
docker build -t technical-portfolio-showcase:local .
docker run --rm technical-portfolio-showcase:local

docker compose build
docker compose run --rm portfolio
# Lists workflow filenames under /workflows
```

## 4. Optional local n8n

```bash
docker compose --profile n8n up n8n
# Open http://localhost:5678
# Workflows → Import from File → pick any n8n-workflows/*_clean.json
# Re-connect your own credentials (no secrets are stored in this repo)
```

### Suggested import order

1. `Email_Triage_Agent_Gmail_clean.json` — smallest agent flow  
2. `Build_Your_First_AI_Agent_clean.json` — agent + tools pattern  
3. `RAG_Chatbot_Company_Documents_Gemini_Pinecone_clean.json` — full RAG  
4. `Voice_Assistant_Telegram_Gcal_clean.json` — voice + calendar  
5. `Katana_MultiAgent_clean.json` — multi-agent (subworkflow IDs are placeholders)  
6. `Backup_n8n_Workflows_to_Google_Drive_clean.json` — ops / reliability  

## 5. What “good” looks like for a reviewer

| Check | Pass criteria |
|-------|----------------|
| No secrets | `"credentials"` absent in JSON; no live API keys |
| Import | Workflow opens in n8n without parse errors |
| RAG story | Drive → embed → Pinecone → agent is visible in graph |
| CI | GitHub Actions validates JSON + builds Docker image |

## Scripts

| Script | Role |
|--------|------|
| `scripts/validate_workflows.py` | Structural check of all `*_clean.json` |
| `scripts/demo.sh` | One-shot local demo (validate + pytest + optional docker) |
| `tests/test_workflows.py` | Pytest smoke suite |

## ES / DE

- Español: [README.es.md](README.es.md)  
- Deutsch: [README.de.md](README.de.md)  
