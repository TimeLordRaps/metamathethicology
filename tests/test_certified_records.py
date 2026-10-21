from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "validation" / "certified-intellidynamics"


def load(name: str) -> dict:
    return json.loads((RECORDS / name).read_text(encoding="utf-8"))


def test_dependency_graph_has_exact_target_closure_and_resolved_edges():
    graph = load("dependency-graph.json")
    node_ids = {node["id"] for node in graph["nodes"]}
    assert set(graph["target_closure"]) == set("ABCDE")
    assert all(graph["target_closure"][target] for target in "ABCDE")
    assert all(node in node_ids for closure in graph["target_closure"].values() for node in closure)
    assert all(edge["from"] in node_ids and edge["to"] in node_ids for edge in graph["edges"])


def test_obligation_ledger_uses_only_declared_epistemic_statuses_and_unique_ids():
    ledger = load("obligations.json")
    allowed = set(ledger["allowed_statuses"])
    ids = [item["id"] for item in ledger["obligations"]]
    assert len(ids) == len(set(ids))
    assert all(item["status"] in allowed for item in ledger["obligations"])
    assert {item["id"].split("-")[0] for item in ledger["obligations"]} >= set("ABCDE")


def test_open_boundaries_are_not_mislabeled_as_proved():
    ledger = {item["id"]: item for item in load("obligations.json")["obligations"]}
    assert ledger["A-04"]["status"] == "UNKNOWN"
    assert ledger["D-05"]["status"] == "UNKNOWN"
    assert ledger["HM-02"]["status"] == "BLOCKED_SOURCE"
    assert ledger["S-01"]["status"] == "PROPOSED"
