# Architecture Overview

## High-level

```
[Business Systems]     [AI Layer]           [Infrastructure]
CRM / DB / Messengers  →  LLM + RAG      →  Docker / Cloud
        ↑                    ↑                     ↑
        └─── n8n / API orchestration ─────────────┘
```

## Core patterns demonstrated

1. **Automation pipelines** — n8n workflows connecting CRM, databases, messengers and AI APIs.
2. **RAG** — document ingestion → embeddings → vector store (Pinecone) → grounded answers.
3. **Agent orchestration** — multi-step agents with tools (email, search, calendar).
4. **Secure execution** — token-protected API bridges, key handling, optional zeroization.

## Module map (related private code)

| Module | Role |
|--------|------|
| State | Persistent agent memory (JSON) |
| SecureChannel | AES-GCM + HMAC proof-of-life |
| KnowledgeSiphon | Document ingest → vector index |
| SecureOverlay | P2P / ZTNA-style transport stub |
| DynamicHoneypot | Decoy / threat-intel stub |
| Zeroization | Heartbeat-linked secret wipe |

## Deployment sketch

- n8n self-hosted or cloud
- Optional: FastAPI bridge (SSH / internal tools) behind token auth
- Vector DB: Pinecone (or PostgreSQL + pgvector)
- Containerisation: Docker (to be added)
