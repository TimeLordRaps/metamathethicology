import json
from dataclasses import replace

import pytest

from metamathethicology import (
    InvalidDerivation,
    close,
    decode_derivation,
    decode_space,
    encode_derivation,
    encode_space,
    replay,
    space_digest,
)
from metamathethicology.examples import deliberation_space
from metamathethicology.representation import MAX_DOCUMENT_BYTES


def test_exact_recovery_preserves_definitions_traces_and_rejection():
    space = deliberation_space()
    proof = close(space)
    recovered_space = decode_space(encode_space(space))
    recovered_proof = decode_derivation(encode_derivation(proof))
    assert recovered_space == space
    assert recovered_proof == proof
    assert encode_space(recovered_space) == encode_space(space)
    assert replay(recovered_space, recovered_proof) == replay(space, proof)
    bad = replace(proof, steps=(replace(proof.steps[0], premises=(1, 0)),))
    with pytest.raises(InvalidDerivation):
        replay(recovered_space, decode_derivation(encode_derivation(bad)))


@pytest.mark.parametrize("attack", ["extra", "schema", "float", "bool", "negative", "zero", "bridge"])
def test_malformed_or_semantically_invalid_definitions_fail_closed(attack):
    item = json.loads(encode_space(deliberation_space()))
    if attack == "extra":
        item["unknown-field"] = "silently ignored?"
    elif attack == "schema":
        item["schema"] = "future-schema"
    elif attack in {"float", "bool", "negative", "zero"}:
        item["stage"] = {"float": [1.0, 1], "bool": [True, 1],
                         "negative": [-1, 1], "zero": [1, 1, 0]}[attack]
    else:
        item["rules"][0]["bridge"] = None
    with pytest.raises((ValueError, TypeError)):
        decode_space(json.dumps(item).encode())


def test_ambiguous_keys_are_rejected_instead_of_last_value_winning():
    with pytest.raises(ValueError, match="duplicate"):
        decode_space(b'{"schema":"one","schema":"two"}')


def test_representation_limits_apply_before_parsing():
    with pytest.raises(ValueError, match="byte limit"):
        decode_space(b" " * (MAX_DOCUMENT_BYTES + 1))
    with pytest.raises(TypeError, match="bytes"):
        decode_space("{}")
    with pytest.raises(ValueError):
        decode_space(b"[" * 2000)


def test_bridge_basis_is_part_of_exact_definition_identity():
    space = deliberation_space()
    altered = replace(space, rules=(replace(space.rules[0], bridge="different norm basis"),))
    assert space_digest(altered) != space_digest(space)


def test_boolean_and_negative_proof_indices_are_rejected():
    item = json.loads(encode_derivation(close(deliberation_space())))
    for indices in [[True, 0], [-1, 0]]:
        item["steps"][0]["premises"] = indices
        with pytest.raises((ValueError, TypeError)):
            decode_derivation(json.dumps(item).encode())
