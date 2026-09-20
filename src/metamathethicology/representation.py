"""Recoverable, versioned JavaScript Object Notation (JSON) representations.

Secure Hash Algorithm 256-bit (SHA-256) digests identify canonical bytes. They
establish neither truth nor authenticity. No Python code is loaded by decoding.
Documents are limited to one mebibyte (1,048,576 bytes) before parsing.
"""

from __future__ import annotations

import hashlib
import json

from ordinatics.ordinals import Ordinal

from .spaces import Assumption, Derivation, Domain, Judgment, OperationSpace, Rule, Step

MAX_DOCUMENT_BYTES = 1_048_576


def _bytes(value: object) -> bytes:
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    if len(result) > MAX_DOCUMENT_BYTES:
        raise ValueError("representation exceeds the document byte limit")
    return result


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _atom(judgment: Judgment) -> dict:
    return {
        "domain": judgment.domain.value,
        "predicate": judgment.predicate,
        "arguments": list(judgment.arguments),
        "stage": list(judgment.stage.coefficients),
    }


def encode_space(space: OperationSpace) -> bytes:
    """Represent the complete definition, including assumptions and bridge bases."""
    return _bytes({
        "schema": "metamathethicology.space.v1",
        "name": space.name,
        "stage": list(space.stage.coefficients),
        "assumptions": [
            {"judgment": _atom(a.judgment), "basis": a.basis} for a in space.assumptions
        ],
        "rules": [
            {
                "name": rule.name,
                "premises": [_atom(p) for p in rule.premises],
                "conclusion": _atom(rule.conclusion),
                "justification": rule.justification,
                "bridge": rule.bridge,
            } for rule in space.rules
        ],
    })


def encode_derivation(derivation: Derivation) -> bytes:
    """Represent ordered proof steps without discarding premise order or repetition."""
    return _bytes({
        "schema": "metamathethicology.derivation.v1",
        "space_digest": derivation.space_digest,
        "steps": [
            {"rule": step.rule, "premises": list(step.premises), "conclusion": _atom(step.conclusion)}
            for step in derivation.steps
        ],
    })


def space_digest(space: OperationSpace) -> str:
    """Identify the canonical, complete operation-space representation."""
    return _digest(encode_space(space))


def derivation_digest(derivation: Derivation) -> str:
    """Identify the submitted trace, including its operation-space binding."""
    return _digest(encode_derivation(derivation))


def judgment_digest(judgment: Judgment) -> str:
    """Identify a domain, predicate, arguments, and stage together."""
    return _digest(_bytes(_atom(judgment)))


def _unique(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate representation key: {key}")
        result[key] = value
    return result


def _load(data: bytes) -> object:
    if type(data) is not bytes:
        raise TypeError("representation must be bytes")
    if len(data) > MAX_DOCUMENT_BYTES:
        raise ValueError("representation exceeds the document byte limit")
    try:
        return json.loads(data, object_pairs_hook=_unique)
    except (UnicodeError, RecursionError) as error:
        raise ValueError("malformed or excessively nested representation") from error


def _record(value: object, keys: set[str]) -> dict:
    if type(value) is not dict or set(value) != keys:
        raise ValueError(f"representation must have exactly these fields: {sorted(keys)}")
    return value


def _list(value: object) -> list:
    if type(value) is not list:
        raise ValueError("representation field must be a list")
    return value


def _ordinal(value: object) -> Ordinal:
    coefficients = _list(value)
    if any(type(c) is not int or c < 0 for c in coefficients) or (
        coefficients and coefficients[-1] == 0
    ):
        raise ValueError("stage must have canonical exact ordinal coefficients")
    return Ordinal(tuple(coefficients))


def _judgment(value: object) -> Judgment:
    item = _record(value, {"domain", "predicate", "arguments", "stage"})
    return Judgment(
        Domain(item["domain"]), item["predicate"], tuple(_list(item["arguments"])),
        _ordinal(item["stage"]),
    )


def decode_space(data: bytes) -> OperationSpace:
    """Recover a definition while rechecking all constructor constraints."""
    item = _record(_load(data), {"schema", "name", "stage", "assumptions", "rules"})
    if item["schema"] != "metamathethicology.space.v1":
        raise ValueError("unsupported operation-space schema")
    assumptions = []
    for raw in _list(item["assumptions"]):
        assumption = _record(raw, {"judgment", "basis"})
        assumptions.append(Assumption(_judgment(assumption["judgment"]), assumption["basis"]))
    rules = []
    for raw in _list(item["rules"]):
        rule = _record(raw, {"name", "premises", "conclusion", "justification", "bridge"})
        rules.append(Rule(
            rule["name"], tuple(_judgment(p) for p in _list(rule["premises"])),
            _judgment(rule["conclusion"]), rule["justification"], rule["bridge"],
        ))
    return OperationSpace(
        item["name"], _ordinal(item["stage"]), tuple(assumptions), tuple(rules),
    )


def decode_derivation(data: bytes) -> Derivation:
    """Recover a submitted trace; acceptance still requires replay against its space."""
    item = _record(_load(data), {"schema", "space_digest", "steps"})
    if item["schema"] != "metamathethicology.derivation.v1":
        raise ValueError("unsupported derivation schema")
    steps = []
    for raw in _list(item["steps"]):
        step = _record(raw, {"rule", "premises", "conclusion"})
        steps.append(Step(
            step["rule"], tuple(_list(step["premises"])), _judgment(step["conclusion"]),
        ))
    return Derivation(item["space_digest"], tuple(steps))
