# Technical Portfolio Showcase

Professional demonstration of AI automation, secure agent design, and n8n production workflows.

Prepared as a clean technical business card (Universidad de La Laguna / LinkedIn / freelance).

**Languages:** [English](README.md) · [Español](docs/README.es.md) · [Deutsch](docs/README.de.md)

**Quick demo:** `bash scripts/demo.sh` — see [docs/DEMO.md](docs/DEMO.md)

**Community:** [CONTRIBUTING](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md)

---

## What this repository demonstrates

| Skill | Evidence |
|-------|----------|
| **n8n + AI Agents** | Multi-agent orchestration, tool calling, Telegram/Gmail/Calendar integrations |
| **RAG systems** | Google Drive → embeddings (Gemini) → Pinecone vector store → grounded answers |
| **Process automation** | Email triage, voice assistant, scheduled backups, CRM-style flows |
| **Secure design patterns** | Credential isolation, token-protected bridges, zeroization concepts (see related private work) |
| **Production readiness** | Importable workflows, clear structure, no secrets |

---

## n8n Workflows (ready to import)

All files are **sanitized** (credentials removed). Import → reconnect your own credentials.

| File | Purpose | Relevance for Spanish market |
|------|---------|------------------------------|
| `RAG_Chatbot_Company_Documents_Gemini_Pinecone_clean.json` | Full RAG pipeline over company documents | Especialista en Integración de IA / RAG |
| `Katana_MultiAgent_clean.json` | Multi-agent system with tool workflows (email, contact, search) | AI Automation Engineer / AI Solutions Architect |
| `Build_Your_First_AI_Agent_clean.json` | Clean AI agent + tools pattern | Junior → Mid Automation roles |
| `Email_Triage_Agent_Gmail_clean.json` | Intelligent email classification & routing | Process automation / customer ops |
| `Voice_Assistant_Telegram_Gcal_clean.json` | Voice + Telegram + Google Calendar agent | End-to-end automation demos |
| `Backup_n8n_Workflows_to_Google_Drive_clean.json` | Scheduled infrastructure backup | DevOps / reliability mindset |

### How to use
1. Open n8n → **Import from File**
2. Select any `*_clean.json`
3. Re-connect credentials (OpenAI / Gemini / Pinecone / Gmail / Telegram etc.)
4. Activate

### Full local demo

```bash
bash scripts/demo.sh
# validate JSON → pytest → docker smoke
```

Details: [docs/DEMO.md](docs/DEMO.md)

---

## Project structure

```
.
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── Dockerfile / docker-compose.yml
├── n8n-workflows/     # Sanitized importable workflows
├── docs/               # PURPOSE, DEMO, ARCHITECTURE, ES/DE
├── scripts/            # validate_workflows.py, demo.sh
├── tests/
└── .github/workflows/  # CI
```

---

## Author

Technical automation & secure AI systems work.  
Location: Canarias (Spain) · Open to teletrabajo / B2B contracts.

---

## License

MIT — see [LICENSE](LICENSE)
