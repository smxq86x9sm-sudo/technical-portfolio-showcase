#!/usr/bin/env bash
# Full local demo for technical-portfolio-showcase
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Validate n8n workflow JSON"
python3 scripts/validate_workflows.py

echo "==> Install test deps (if needed)"
python3 -m pip install -q -r requirements.txt

echo "==> Run pytest"
python3 -m pytest -q

if command -v docker >/dev/null 2>&1; then
  echo "==> Docker build"
  docker build -t technical-portfolio-showcase:demo .
  echo "==> Docker run"
  docker run --rm technical-portfolio-showcase:demo
else
  echo "==> Docker not found — skip container smoke"
fi

echo ""
echo "Demo OK. Next: import n8n-workflows/*_clean.json into your n8n instance."
echo "Docs: docs/DEMO.md | ES: docs/README.es.md | DE: docs/README.de.md"
