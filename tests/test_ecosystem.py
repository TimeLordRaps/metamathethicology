"""Integration examples against the exact public dependency revisions.

Host calculations enter as explicitly identified premises. These tests do not
claim that the new rule language internally derives the imported algorithms.
Install the ecosystem extra to run this required integration file; no silent skip.
"""

from grounded_hypercalculi import GroundedRational, MetamathDatabase, Permutation, PermutationGroup
from grounded_hyperset_theory import AccessiblePointedGraph, bisimilar
from ordinatics.ordinals import OMEGA, ONE
from ordinatics.semantics import Add, Eq, Nat, Truth, evaluate

from metamathethicology import (
    Assumption,
    Domain,
    Judgment,
    OperationSpace,
    Rule,
    close,
    reflect,
    replay,
)


def test_language_satisfaction_hypersets_hypercalculus_and_reals_feed_a_declared_space():
    stage = OMEGA + ONE
    arithmetic = Truth(OMEGA, Eq(Add(Nat(2), Nat(3)), Nat(5)))
    assert evaluate(arithmetic, stage=stage) is True

    database = MetamathDatabase()
    database.add_axiom("given-p", ("|-", "P"))
    database.add_theorem("copy-p", ("|-", "P"), ("given-p",))
    assert database.verify_proof("copy-p") is True
    database.add_theorem("fake-q", ("|-", "Q"), ("given-p",))
    assert database.verify_proof("fake-q") is False

    loop = AccessiblePointedGraph(0, {0: [0]})
    two_cycle = AccessiblePointedGraph(0, {0: [1], 1: [0]})
    empty = AccessiblePointedGraph(0, {0: []})
    assert bisimilar(loop, two_cycle) is True
    assert bisimilar(loop, empty) is False

    group = PermutationGroup([Permutation({1: 2, 2: 1}), Permutation({2: 3, 3: 2})])
    assert group.order() == 6
    assert GroundedRational(1, 3) + GroundedRational(2, 3) == GroundedRational(1)

    descriptions = (
        "bounded quotation at omega of 2+3=5 evaluates true",
        "literal proof copy-p follows given-p and does not prove Q",
        "one-node loop and two-node cycle are bisimilar; loop and empty are not",
        "permutations (1 2) and (2 3) generate a six-element group",
        "exact rational 1/3 + 2/3 equals 1",
    )
    facts = tuple(Judgment(Domain.METAMATH, "host-check", (text,), stage) for text in descriptions)
    joint = Judgment(Domain.METALOGIC, "joint-host-checks", ("fixed-example-v1",), stage)
    space = OperationSpace("public-foundation-example", stage, tuple(
        Assumption(fact, "observed by this integration test; not derived in the object language")
        for fact in facts
    ), (Rule("collect", facts, joint, "finite conjunction of the five supplied premises",
             bridge="metamathematical observations may be collected as a metalogical record"),))
    proof = close(space)
    assert replay(space, proof)[-1] == joint
    assert reflect(space, proof, joint, at=stage + ONE).stage == OMEGA + ONE + ONE


def test_bisimulation_does_not_supply_language_truth_or_normative_premises():
    loop = AccessiblePointedGraph(0, {0: [0]})
    assert bisimilar(loop, loop)
    descriptive = Judgment(Domain.METAPHYSICS, "self-similar-model", ("loop",), OMEGA)
    normative = Judgment(Domain.METAETHICS, "morally-justified", ("loop",), OMEGA)
    space = OperationSpace("no-silent-cast", OMEGA,
                           (Assumption(descriptive, "toy structural interpretation"),), ())
    assert normative not in replay(space, close(space))
