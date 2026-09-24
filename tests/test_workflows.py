"""Smoke tests for portfolio n8n workflow JSON files."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / "n8n-workflows"


def workflow_files():
    files = sorted(WF_DIR.glob("*_clean.json"))
    assert files, "expected cleaned workflow JSON files"
    return files


@pytest.mark.parametrize("path", workflow_files(), ids=lambda p: p.name)
def test_workflow_is_valid_json(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    assert "nodes" in data
    assert isinstance(data["nodes"], list)
    assert len(data["nodes"]) >= 1


@pytest.mark.parametrize("path", workflow_files(), ids=lambda p: p.name)
def test_no_credentials_block(path: Path):
    text = path.read_text(encoding="utf-8")
    assert '"credentials"' not in text


@pytest.mark.parametrize("path", workflow_files(), ids=lambda p: p.name)
def test_has_name(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data.get("name"), str)
    assert len(data["name"]) > 0
    assert not data["name"].startswith("!!!")


def test_expected_portfolio_workflows_present():
    names = {p.name for p in WF_DIR.glob("*_clean.json")}
    expected = {
        "RAG_Chatbot_Company_Documents_Gemini_Pinecone_clean.json",
        "Katana_MultiAgent_clean.json",
        "Build_Your_First_AI_Agent_clean.json",
        "Email_Triage_Agent_Gmail_clean.json",
        "Voice_Assistant_Telegram_Gcal_clean.json",
        "Backup_n8n_Workflows_to_Google_Drive_clean.json",
    }
    assert expected.issubset(names)
