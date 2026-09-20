from dataclasses import replace
from itertools import combinations

import pytest
from ordinatics.ordinals import OMEGA, ONE, Ordinal

from metamathethicology import (
    Assumption,
    BudgetExceeded,
    Derivation,
    Domain,
    InvalidDerivation,
    Judgment,
    OperationSpace,
    Rule,
    Step,
    close,
    reflect,
    replay,
    space_digest,
)
from metamathethicology.examples import deliberation_space, demo


def atom(name, stage=OMEGA, domain=Domain.METAMATH):
    return Judgment(domain, name, (), stage)


def chain():
    a, b, c = (atom(name) for name in ("a", "b", "c"))
    return OperationSpace("chain", OMEGA, (Assumption(a, "declared axiom"),), (
        Rule("bc", (b,), c, "declared implication"),
        Rule("ab", (a,), b, "declared implication"),
    ))


def test_reverse_ordered_rules_retain_context_between_passes():
    space = chain()
    proof = close(space)
    assert [s.rule for s in proof.steps] == ["ab", "bc"]
    assert [s.premises for s in proof.steps] == [(0,), (1,)]
    assert replay(space, proof) == (atom("a"), atom("b"), atom("c"))


def test_unsupported_cycles_cannot_prove_their_own_premises():
    space = replace(chain(), assumptions=(), rules=(
        Rule("ab", (atom("a"),), atom("b"), "hypothesis"),
        Rule("ba", (atom("b"),), atom("a"), "hypothesis"),
    ))
    assert close(space).steps == ()
    assert replay(space, close(space)) == ()


def test_cross_domain_rule_needs_explicit_bridge():
    with pytest.raises(ValueError, match="bridge"):
        Rule("is-to-ought", (atom("is"),), atom("ought", domain=Domain.METAETHICS), "claim")


def test_missing_norm_remains_underived_even_at_a_higher_ordinal():
    with_norm = deliberation_space()
    assert with_norm.rules[0].conclusion in replay(with_norm, close(with_norm))
    without_norm = replace(deliberation_space(include_norm=False), stage=OMEGA**2)
    assert without_norm.rules[0].conclusion not in replay(without_norm, close(without_norm))


def test_same_spelling_in_different_domains_is_not_the_same_premise():
    space = OperationSpace("domains", OMEGA, (Assumption(atom("a"), "axiom"),), (
        Rule("b", (atom("a", domain=Domain.METAETHICS),),
             atom("b", domain=Domain.METAETHICS), "conditional"),
    ))
    assert close(space).steps == ()


@pytest.mark.parametrize("stage", [0, True, 1.5, (0, 1)])
def test_stage_requires_an_ordinal_not_a_coerced_numeric_label(stage):
    with pytest.raises(TypeError, match="Ordinal"):
        atom("x", stage)


def test_operation_spaces_start_transfinitely():
    with pytest.raises(ValueError, match="omega"):
        atom("x", Ordinal.from_int(100))
    assert atom("x", OMEGA**10).stage == OMEGA**10


def test_stage_order_prevents_downward_inference_and_future_premises():
    with pytest.raises(ValueError, match="earlier"):
        Rule("lower", (atom("a", OMEGA + ONE),), atom("b"), "invalid lowering")
    with pytest.raises(ValueError, match="exceeds"):
        OperationSpace("future", OMEGA, (Assumption(atom("x", OMEGA + ONE), "future"),), ())


def test_earlier_atom_is_not_silently_relabelled_as_later_atom():
    space = OperationSpace("no-implicit-lift", OMEGA + ONE,
                           (Assumption(atom("a"), "axiom"),), (
        Rule("later", (atom("a", OMEGA + ONE),), atom("b", OMEGA + ONE), "conditional"),
    ))
    assert close(space).steps == ()


@pytest.mark.parametrize("change", ["basis", "stage", "justification", "name"])
def test_replay_binds_the_entire_definition(change):
    space = chain()
    proof = close(space)
    if change == "basis":
        altered = replace(space, assumptions=(replace(space.assumptions[0], basis="new"),))
    elif change == "stage":
        altered = replace(space, stage=OMEGA + ONE)
    elif change == "justification":
        altered = replace(space, rules=(replace(space.rules[0], justification="new"), space.rules[1]))
    else:
        altered = replace(space, name="new")
    with pytest.raises(InvalidDerivation, match="binding"):
        replay(altered, proof)


@pytest.mark.parametrize("attack", ["conclusion", "forward", "missing", "order", "unknown"])
def test_invalid_traces_are_rejected(attack):
    space = chain()
    proof = close(space)
    first, second = proof.steps
    if attack == "conclusion":
        steps = (replace(first, conclusion=atom("c")), second)
    elif attack == "forward":
        steps = (replace(first, premises=(1,)), second)
    elif attack == "missing":
        steps = (second,)
    elif attack == "order":
        steps = (second, first)
    else:
        steps = (replace(first, rule="unknown"), second)
    with pytest.raises(InvalidDerivation):
        replay(space, replace(proof, steps=steps))


def test_repeated_ordered_premises_are_preserved():
    a, b = atom("a"), atom("b")
    space = OperationSpace("ordered", OMEGA, (Assumption(a, "axiom"), Assumption(b, "axiom")), (
        Rule("join", (a, b, a), atom("c"), "ordered conjunction-like rule"),
    ))
    proof = close(space)
    assert proof.steps[0].premises == (0, 1, 0)
    for indices in [(0, 1), (1, 0, 0)]:
        changed = replace(proof, steps=(replace(proof.steps[0], premises=indices),))
        with pytest.raises(InvalidDerivation, match="premises"):
            replay(space, changed)


def test_replay_acceptance_does_not_claim_saturation():
    space = chain()
    prefix = Derivation(space_digest(space), ())
    assert replay(space, prefix) == (atom("a"),)
    assert atom("c") not in replay(space, prefix)
    assert atom("c") in replay(space, close(space))


def test_reflection_replays_and_requires_strictly_later_stage():
    space = chain()
    proof = close(space)
    reflected = reflect(space, proof, atom("c"), at=OMEGA + ONE)
    assert reflected.domain is Domain.METALOGIC
    assert reflected.predicate == "derivable-in"
    assert reflected.stage == OMEGA + ONE
    assert reflected.arguments[0] == space_digest(space)
    with pytest.raises(ValueError, match="strictly later"):
        reflect(space, proof, atom("c"), at=OMEGA)
    with pytest.raises(InvalidDerivation, match="absent"):
        reflect(space, proof, atom("unproved"), at=OMEGA + ONE)
    with pytest.raises(InvalidDerivation):
        reflect(space, replace(proof, steps=proof.steps[::-1]), atom("c"), at=OMEGA + ONE)


def test_budgets_raise_unknown_instead_of_returning_false():
    space = chain()
    with pytest.raises(BudgetExceeded, match="UNKNOWN"):
        close(space, max_steps=1)
    with pytest.raises(BudgetExceeded, match="UNKNOWN"):
        replay(space, close(space), max_steps=1)
    for budget in [0, -1, True, 2.0]:
        with pytest.raises(ValueError, match="positive integer"):
            close(space, max_steps=budget)


def test_duplicate_rules_and_unstated_axioms_are_rejected():
    space = chain()
    with pytest.raises(ValueError, match="unique"):
        replace(space, rules=(space.rules[0], space.rules[0]))
    with pytest.raises(ValueError, match="Assumptions"):
        Rule("free-truth", (), atom("p"), "unjustified")
    with pytest.raises(TypeError):
        Step("bad-index", (True,), atom("p"))


def test_closure_matches_intersection_of_all_closed_supersets():
    # Independent finite semantic oracle, not a copy of forward chaining.
    atoms = tuple(atom(name) for name in "abcd")
    rules = (
        Rule("ab", (atoms[0],), atoms[1], "implication"),
        Rule("bcd", (atoms[1], atoms[2]), atoms[3], "conjunction implication"),
        Rule("dc", (atoms[3],), atoms[2], "cycle implication"),
    )
    subsets = [set(c) for n in range(5) for c in combinations(atoms, n)]
    for initial in subsets:
        models = [m for m in subsets if initial <= m and all(
            not set(rule.premises) <= m or rule.conclusion in m for rule in rules
        )]
        expected = set.intersection(*models)
        space = OperationSpace("finite-model-check", OMEGA,
                               tuple(Assumption(a, "axiom") for a in atoms if a in initial), rules)
        assert set(replay(space, close(space))) == expected


def test_demo_keeps_stronger_research_targets_unknown():
    result = demo()
    assert result["definition_recovered_exactly"]
    assert result["conditional_conclusion_derived"]
    assert result["conclusion_without_norm"] == "NOT_DERIVED (truth UNKNOWN)"
    assert result["native_self_derivation"] == "UNKNOWN"
