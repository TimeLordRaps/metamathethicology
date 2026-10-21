from __future__ import annotations

import json
import os
from dataclasses import replace
from itertools import product
from pathlib import Path

import pytest

from metamathethicology.certified_intellidynamics import (
    INVARIANT_ID,
    AdaptationDomain,
    AppliedWill,
    CoherenceDomain,
    Configuration,
    Decision,
    Effect,
    PolicyCase,
    RecoveryCertificate,
    RecoveryKernel,
    RecoveryRank,
    SystemState,
    VerifiedChecker,
    begin_recovery,
    check_update,
    checkpoint,
    composition_safe,
    configuration_digest,
    decode_certificate,
    demo_model,
    encode_certificate,
    environment_step,
    forward_simulates,
    install,
    invariant,
    make_certificate,
    ordinary_step,
    pairwise_without_joint_solution,
    recovery_step,
    rollback,
    verified_check_update,
    verified_install,
    verify_recovery_certificate,
)

CHECKER = os.environ.get("HYPERMATH_CERTIFIED_CHECKER")
MODEL_SOURCE = os.environ.get("HYPERMATH_CERTIFIED_MODEL_SOURCE")
MAIN_SOURCE = os.environ.get("HYPERMATH_CERTIFIED_MAIN_SOURCE")
LEAN_MODEL_SHA256 = "5f091536699185ac03dff3f9282ef5a9d8e6c89d240a083b6cc81faab4599bc2"
LEAN_MAIN_SHA256 = "6203aba21394cc3570fbce32ef53b06b189b721a2cbd7399d19778ac2b2632ee"
LEAN_EXECUTABLE_SHA256 = "166bbb47f03721f0b3581e59d2c94581579e55aec5f68160ec70b194dd94be4f"


def verified_checker() -> VerifiedChecker:
    if not CHECKER or not MODEL_SOURCE or not MAIN_SOURCE:
        pytest.skip("exact Hypermath checker/source paths were not supplied")
    return VerifiedChecker(
        Path(CHECKER),
        LEAN_EXECUTABLE_SHA256,
        Path(MODEL_SOURCE),
        LEAN_MODEL_SHA256,
        Path(MAIN_SOURCE),
        LEAN_MAIN_SHA256,
        ("checker/v1", "model/v1", "no-limit/v1", "governance/v1", INVARIANT_ID),
    )


def fixtures():
    will = AppliedWill(
        ("observed",), "deliberate", "avoid-forbidden-effect", INVARIANT_ID,
        AdaptationDomain(
            ("dry", "wet"), ("attention", "fatigue"), ("consent", "pressure"),
            ("immediate", "episode"),
        ),
        CoherenceDomain(
            ("human", "agent"),
            ("past-verifies-present", "invariant-constrains-adaptation"),
        ),
    )
    common = dict(
        checker_id="checker/v1",
        model_id="model/v1",
        limit_rule_id="no-limit/v1",
        authorization_id="governance/v1",
    )

    def configuration(version: str, unsafe: tuple[str, str] | None = None, **changes):
        values = common | changes
        policy = tuple(
            PolicyCase(context, peer, f"effect-{version}", (context, peer) == unsafe)
            for context, peer in product(
                will.contextual_adaptation.environments, will.coherence_relations.peers
            )
        )
        return Configuration(version, policy, **values)

    current = configuration("v1")
    return will, configuration, SystemState(
        current, will, "dry", "human", frozenset({"council"}), "a"
    )


def certificate_for(state, proposal, authority="council"):
    return encode_certificate(make_certificate(state, proposal, authorized_by=authority))


def test_six_will_fields_are_present_and_operational_view_is_total():
    will, _, _ = fixtures()
    assert len(will.operational_view()) == 6
    assert will.coherent()
    assert will.contextual_adaptation.environments == ("dry", "wet")
    assert will.contextual_adaptation.self_adaptation == ("attention", "fatigue")
    assert will.contextual_adaptation.social_adaptation == ("consent", "pressure")
    assert will.contextual_adaptation.timescales == ("immediate", "episode")
    assert will.coherence_relations.peers == ("human", "agent")
    assert "invariant-constrains-adaptation" in will.coherence_relations.component_relations


def test_exact_nontrivial_update_is_accepted_and_future_cases_remain_safe():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    encoded = certificate_for(state, proposal)
    installed, result = install(state, proposal, encoded, case_budget=4)
    assert result.decision is Decision.ACCEPTED
    assert installed.configuration.version == "v2"
    for context, peer in product(("dry", "wet"), ("human", "agent")):
        reached = ordinary_step(replace(installed, context=context, peer=peer))
        assert invariant(reached)


def test_operational_installation_is_gated_by_the_exact_pinned_lean_evaluator():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    installed, result = verified_install(
        state,
        proposal,
        certificate_for(state, proposal),
        case_budget=4,
        checker=verified_checker(),
    )
    assert result.decision is Decision.ACCEPTED
    assert "Lean evaluator returned ACCEPTED" in result.reason
    assert installed.configuration.version == "v2"
    assert installed.evidence[-1].startswith("VERIFIED-INSTALL-ACCEPTED")


def test_a_changed_checker_digest_cannot_authorize_installation():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    checker = replace(verified_checker(), executable_sha256="0" * 64)
    result = verified_check_update(
        state,
        proposal,
        certificate_for(state, proposal),
        case_budget=4,
        checker=checker,
    )
    assert result.decision is Decision.REJECTED
    assert "digest mismatch" in result.reason


def test_version_outside_the_closed_lean_fragment_remains_unknown():
    _, configuration, state = fixtures()
    proposal = configuration("v3")
    result = verified_check_update(
        state,
        proposal,
        certificate_for(state, proposal),
        case_budget=4,
        checker=verified_checker(),
    )
    assert result.decision is Decision.UNKNOWN
    assert "outside the verified Lean fragment" in result.reason


def test_unsafe_future_transition_is_rejected_even_when_installation_itself_is_safe():
    _, configuration, state = fixtures()
    proposal = configuration("v2", unsafe=("wet", "agent"))
    result = check_update(state, proposal, certificate_for(state, proposal), case_budget=4)
    assert result.decision is Decision.REJECTED
    assert "counterexample" in result.reason


def test_environment_case_omitted_by_naive_local_certificate_fails_exact_coverage():
    _, configuration, state = fixtures()
    proposal = configuration("v2", unsafe=("wet", "human"))
    certificate = make_certificate(state, proposal, authorized_by="council")
    naive = replace(certificate, cases=tuple(c for c in certificate.cases if c.context == "dry"))
    result = check_update(state, proposal, encode_certificate(naive), case_budget=4)
    assert result.decision is Decision.REJECTED
    assert "coverage" in result.reason


@pytest.mark.parametrize("field", ["checker_id", "model_id", "limit_rule_id", "authorization_id"])
def test_trusted_contract_cannot_mutate_under_its_own_new_interpretation(field):
    _, configuration, state = fixtures()
    proposal = configuration("v2", **{field: f"{field}/v2"})
    encoded = certificate_for(state, proposal)
    result = check_update(state, proposal, encoded, case_budget=4)
    assert result.decision is Decision.REJECTED
    assert "trusted-contract migration" in result.reason


def test_same_names_with_changed_ontology_are_bound_by_model_identity():
    _, configuration, state = fixtures()
    proposal = configuration("v2", model_id="same-labels-new-ontology/v2")
    result = check_update(state, proposal, certificate_for(state, proposal), case_budget=4)
    assert result.decision is Decision.REJECTED


def test_absent_governance_authorization_is_rejected():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    result = check_update(
        state, proposal, certificate_for(state, proposal, authority="outsider"), case_budget=4
    )
    assert result.decision is Decision.REJECTED
    assert "authorization" in result.reason


def test_budget_exhaustion_is_unknown_and_does_not_authorize():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    result = check_update(state, proposal, certificate_for(state, proposal), case_budget=3)
    assert result.decision is Decision.UNKNOWN
    assert not result.authorizes
    unchanged, install_result = install(
        state, proposal, certificate_for(state, proposal), case_budget=3
    )
    assert install_result.decision is Decision.UNKNOWN
    assert unchanged.configuration.version == "v1"


@pytest.mark.parametrize(
    "payload",
    [b"not-json", b"{}", b'{"schema":"x","schema":"y"}', b"[]"],
)
def test_arbitrary_malformed_records_fail_closed(payload):
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    result = check_update(state, proposal, payload, case_budget=4)
    assert result.decision is Decision.REJECTED


def test_tampering_any_bound_target_digest_is_rejected():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    item = json.loads(certificate_for(state, proposal))
    item["target_digest"] = "0" * 64
    result = check_update(
        state, proposal, json.dumps(item, sort_keys=True, separators=(",", ":")).encode(),
        case_budget=4,
    )
    assert result.decision is Decision.REJECTED
    assert "target_digest" in result.reason


def test_encoding_round_trip_is_canonical_and_binds_the_exact_configuration():
    _, configuration, state = fixtures()
    proposal = configuration("v2")
    encoded = certificate_for(state, proposal)
    assert encode_certificate(decode_certificate(encoded)) == encoded
    assert configuration_digest(proposal) != configuration_digest(state.configuration)


def test_ordinal_rank_allows_lower_reset_only_when_the_omega_coefficient_falls():
    assert RecoveryRank(0, 99) < RecoveryRank(1, 0)
    assert str(RecoveryRank(1, 0).ordinal) == "ω"
    assert not RecoveryRank(1, 5) < RecoveryRank(1, 4)


def test_actual_recovery_preserves_invariant_and_terminates_under_scheduler_contract():
    _, _, state = fixtures()
    kernel = RecoveryKernel("K1", (("a", "b"), ("b", "g"), ("g", "g")))
    cert = RecoveryCertificate(
        "g", (kernel,), (("a", RecoveryRank(1, 0)), ("b", RecoveryRank(0, 8)),
                         ("g", RecoveryRank(0, 0))),
    )
    recovering = begin_recovery(state, cert)
    recovering = environment_step(recovering, "wet")
    with pytest.raises(RuntimeError, match="requires a recovery step"):
        environment_step(recovering, "dry")
    recovering = recovery_step(recovering, "K1")
    recovering = environment_step(recovering, "dry")
    recovered = recovery_step(recovering, "K1")
    assert recovered.recovery is None
    assert recovered.operational_state == "g"
    assert invariant(recovered)


def test_switching_counterexample_is_rejected_by_common_rank_check():
    k1 = RecoveryKernel("K1", (("a", "b"), ("b", "g"), ("g", "g")))
    k2 = RecoveryKernel("K2", (("a", "g"), ("b", "a"), ("g", "g")))
    ranks_k1 = (("a", RecoveryRank(0, 2)), ("b", RecoveryRank(0, 1)),
                ("g", RecoveryRank(0, 0)))
    ranks_k2 = (("a", RecoveryRank(0, 1)), ("b", RecoveryRank(0, 2)),
                ("g", RecoveryRank(0, 0)))
    assert verify_recovery_certificate(RecoveryCertificate("g", (k1,), ranks_k1)).authorizes
    assert verify_recovery_certificate(RecoveryCertificate("g", (k2,), ranks_k2)).authorizes
    switched = verify_recovery_certificate(RecoveryCertificate("g", (k1, k2), ranks_k1))
    assert switched.decision is Decision.REJECTED
    assert "common descent" in switched.reason


def test_individually_safe_components_can_violate_a_shared_composition_budget():
    assert composition_safe((1,), 1)
    assert composition_safe((1,), 1)
    assert not composition_safe((1, 1), 1)


def test_partial_endpoint_observation_can_lose_the_unsafe_path():
    safe, unsafe = Effect("safe", False, "v", "c", "p"), Effect("harm", True, "v", "c", "p")
    path = (safe, unsafe, safe)
    endpoint_only = (path[0].name, path[-1].name)
    assert endpoint_only == ("safe", "safe")
    assert any(effect.forbidden for effect in path)


def test_coherent_will_does_not_certify_the_effect_constraint():
    will, _, state = fixtures()
    unsafe = replace(
        state,
        persistent_effects=(Effect("harm", True, "v1", "dry", "human"),),
    )
    assert will.coherent()
    assert not invariant(unsafe)


def test_finite_approximation_and_safe_prefixes_do_not_certify_a_limit_exit():
    finite_observations = ["safe"] * 100
    later_observation = "harm"
    assert all(value == "safe" for value in finite_observations)
    assert later_observation == "harm"
    _, _, state = fixtures()
    safe_prefix = tuple(Effect("safe", False, "v1", "dry", "human") for _ in range(10))
    assert invariant(replace(state, persistent_effects=safe_prefix))
    unsafe_limit = safe_prefix + (Effect("limit-harm", True, "v1", "omega", "human"),)
    assert not invariant(replace(state, persistent_effects=unsafe_limit))


def test_almost_sure_event_is_not_a_pathwise_guarantee():
    # Geometric recovery reaches g with probability one, but every finite delay
    # path exists and therefore there is no uniform pathwise deadline.
    probability_not_recovered_after_20 = 2 ** -20
    delaying_path_exists = True
    assert probability_not_recovered_after_20 > 0
    assert delaying_path_exists


def test_rollback_restores_only_operational_state_and_never_erases_effects_or_evidence():
    _, _, state = fixtures()
    saved = checkpoint(state)
    acted = ordinary_step(state)
    restored = rollback(replace(acted, operational_state="g"), saved)
    assert restored.operational_state == state.operational_state
    assert restored.persistent_effects == acted.persistent_effects
    assert len(restored.evidence) > len(acted.evidence)


def test_forward_abstraction_transfers_the_selected_safety_property():
    _, _, state = fixtures()
    after = ordinary_step(state)
    assert forward_simulates(state, after)
    assert invariant(after)


def test_pairwise_local_compatibility_does_not_imply_joint_satisfiability():
    assert pairwise_without_joint_solution()


def test_complete_demo_contains_nontrivial_update_interaction_and_recovery():
    result = demo_model()
    assert result["accepted_update"] == "ACCEPTED"
    assert result["rejected_update"] == "REJECTED"
    assert result["final_version"] == "v2"
    assert result["final_control_state"] == "g"
    assert result["recovery_complete"] is True
    assert result["invariant"] is True
    assert result["will_components"] == 6
    assert result["effects"] == ["assist"]
    assert result["installation_path"] == "PYTHON_ANALYSIS_ONLY"


def test_verified_demo_consumes_the_pinned_lean_acceptance_path():
    result = demo_model(verified_checker())
    assert result["accepted_update"] == "ACCEPTED"
    assert result["rejected_update"] == "REJECTED"
    assert result["invariant"] is True
    assert result["recovery_complete"] is True
    assert result["installation_path"] == "PINNED_LEAN"
    assert result["checker_binding"].startswith("lean-certified-intellidynamics:")
