# Contributing

Thanks for interest in this portfolio repository.

## Scope

This repo is a **public technical business card**: sanitized n8n workflows and docs for academic / LinkedIn / freelance review.

It is **not** a product monorepo. Private production code stays elsewhere.

## How to contribute

1. **Issues** — bug reports (broken JSON, missing docs, CI failures) are welcome.  
2. **Pull requests** — keep changes small and focused:
   - Fix validation / tests
   - Improve documentation (EN / ES / DE)
   - Add demo steps without adding secrets
3. **Do not** commit credentials, API keys, real Drive folder IDs, or personal webhook paths.

## Development

```bash
python scripts/validate_workflows.py
pip install -r requirements.txt && pytest -q
bash scripts/demo.sh
```

## Code style

- Workflow JSON: no `"credentials"` blocks; placeholders only (`REPLACE_*`, `YOUR_*`).  
- Docs: English primary; Spanish and German under `docs/`.  
- Commits: clear, imperative messages (e.g. `Fix RAG folder placeholder`).

## Security

If you find a leaked secret in history or files, open an issue **without** pasting the secret in public comments, or contact the maintainer privately.

## License

By contributing, you agree that your contributions are licensed under the MIT License (see [LICENSE](LICENSE)).
