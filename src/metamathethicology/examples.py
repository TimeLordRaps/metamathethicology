"""Small, declared model spaces; their premises are not claims about the world."""

from __future__ import annotations

from ordinatics.ordinals import OMEGA, ONE

from .representation import decode_space, encode_space
from .spaces import Assumption, Domain, Judgment, OperationSpace, Rule, close, reflect, replay
from .will_electrophysics import electrophysics_space


def deliberation_space(*, include_norm: bool = True) -> OperationSpace:
    """A toy derivation that needs both a descriptive premise and a stated norm.

    The norm is a defeasible model assumption, not an endorsed ethical theory.
    An ordinal increase makes a rule available; it never justifies that norm.
    """
    avoids_harm = Judgment(Domain.METAPHYSICS, "avoids-harm-in-model", ("act",), OMEGA)
    norm = Judgment(Domain.METAETHICS, "adopted-harm-avoidance-norm", ("model",), OMEGA)
    ought = Judgment(Domain.METAETHICS, "ought-in-model", ("act",), OMEGA + ONE)
    assumptions = [Assumption(avoids_harm, "stipulated descriptive premise of the toy model")]
    if include_norm:
        assumptions.append(Assumption(norm, "explicitly adopted conditional norm of the toy model"))
    rule = Rule(
        "apply-declared-norm", (avoids_harm, norm), ought,
        "This toy theory defines the conclusion conditionally on both premises.",
        bridge="Declared descriptive-to-normative bridge; no claim of universal ethical validity.",
    )
    return OperationSpace("conditional-deliberation", OMEGA + ONE, tuple(assumptions), (rule,))


def electrophysics_demo() -> dict[str, object]:
    """Show that the will-electrophysical transport rests on an adopted licence.

    With the licence the drops form and close into the will balance. Without it
    the electrical premises stay exactly where they are, in METAPHYSICS, and no
    will conclusion is derivable at all. Nothing false appears either way; the
    difference is the whole content of the borrowing.
    """
    will_predicates = {"termformed", "will-balance"}
    licensed = electrophysics_space()
    unlicensed = electrophysics_space(include_licence=False)
    derived = [j for j in replay(licensed, close(licensed)) if j.predicate in will_predicates]
    without = [j for j in replay(unlicensed, close(unlicensed)) if j.predicate in will_predicates]
    bridged = sum(1 for rule in licensed.rules if rule.bridge is not None)
    return {
        "will_conclusions_with_licence": len(derived),
        "will_conclusions_without_licence": len(without),
        "rules_crossing_a_domain_boundary": f"{bridged} of {len(licensed.rules)}",
        "every_crossing_names_a_bridge": bridged == len(licensed.rules),
        "transport_soundness": "NOT_ESTABLISHED (hyperphysics GC-4)",
        "will_units": "NONE (the numeric reading is dimensionless)",
    }


def demo() -> dict[str, object]:
    """Exercise closure, exact recovery, a missing norm, and next-stage reflection."""
    space = deliberation_space()
    proof = close(space)
    context = replay(space, proof)
    recovered = decode_space(encode_space(space))
    without_norm = deliberation_space(include_norm=False)
    incomplete_context = replay(without_norm, close(without_norm))
    reflection = reflect(space, proof, space.rules[0].conclusion, at=OMEGA + ONE + ONE)
    return {
        "initial_stage": str(OMEGA),
        "definition_recovered_exactly": recovered == space,
        "conditional_conclusion_derived": space.rules[0].conclusion in context,
        "conclusion_without_norm": "DERIVED" if space.rules[0].conclusion in incomplete_context
        else "NOT_DERIVED (truth UNKNOWN)",
        "reflection_stage": str(reflection.stage),
        "reflection_predicate": reflection.predicate,
        "native_self_derivation": "UNKNOWN",
        "unrestricted_self_truth": "NOT_ESTABLISHED",
        "will_electrophysics": electrophysics_demo(),
    }
