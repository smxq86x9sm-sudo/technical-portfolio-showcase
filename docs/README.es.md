# Documentación (ES)

Este repositorio es una **tarjeta de visita técnica** (Universidad de La Laguna / LinkedIn / freelance).

## Qué demuestra

| Competencia | Evidencia |
|-------------|-----------|
| **n8n + agentes IA** | Orquestación multi-agente, tools, Gmail / Telegram / Calendar |
| **RAG** | Google Drive → embeddings (Gemini) → Pinecone → respuestas fundamentadas |
| **Automatización de procesos** | Clasificación de correo, asistente de voz, backups programados |
| **Diseño seguro** | Sin secretos en el repo; patrones de aislamiento de credenciales |
| **Listo para producción** | Workflows importables, CI, Docker, tests |

## Cómo probar (demo)

```bash
# 1. Validar JSON de workflows
python scripts/validate_workflows.py

# 2. Tests
pip install -r requirements.txt && pytest -q

# 3. Docker
docker compose build
docker compose run --rm portfolio

# 4. n8n local (opcional)
docker compose --profile n8n up n8n
# Abrir http://localhost:5678 → Import from File → n8n-workflows/*_clean.json
```

## Mercado español (teletrabajo)

Alineado con roles: *Ingeniero de Automatización*, *Especialista en Integración de IA / RAG*, *AI Solutions Architect*.

## Licencia

MIT — ver [LICENSE](../LICENSE).
