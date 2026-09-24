#!/usr/bin/env python3
"""Validate n8n workflow JSON files in n8n-workflows/."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / "n8n-workflows"


def main() -> int:
    files = sorted(WF_DIR.glob("*_clean.json"))
    if not files:
        print("ERROR: no *_clean.json in n8n-workflows/", file=sys.stderr)
        return 1

    errors = 0
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"FAIL {path.name}: invalid JSON ({e})")
            errors += 1
            continue

        if not isinstance(data, dict):
            print(f"FAIL {path.name}: root must be object")
            errors += 1
            continue

        nodes = data.get("nodes")
        if not isinstance(nodes, list) or len(nodes) < 1:
            print(f"FAIL {path.name}: missing nodes")
            errors += 1
            continue

        raw = path.read_text(encoding="utf-8")
        if '"credentials"' in raw:
            print(f"FAIL {path.name}: credentials block still present")
            errors += 1
            continue

        if "connections" not in data:
            print(f"WARN {path.name}: no connections key")

        print(f"OK   {path.name}: {len(nodes)} nodes, name={data.get('name', '?')!r}")

    if errors:
        print(f"\n{errors} file(s) failed")
        return 1
    print(f"\nAll {len(files)} workflow(s) OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
