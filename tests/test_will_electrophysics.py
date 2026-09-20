"""The will-electrophysical transport, and the licence the whole of it rests on.

These tests check that the combination is stated completely and that its
dependence on an adopted declaration is visible in the closure rather than only
in prose. They establish nothing about will and nothing about physics.
"""

from __future__ import annotations

import pytest
from ordinatics.ordinals import OMEGA, ONE

from metamathethicology import (
    BudgetExceeded,
    Domain,
    close,
    reflect,
    replay,
)
from metamathethicology.will_electrophysics import (
    ACCUMULATED_DROP,
    BALANCE,
    CAPACITANCE_READINGS_CONSIDERED,
    CONSTANT,
    CONSTANT_WILL_DECLARATION,
    CONSTANT_WILL_LAW_IS_OPEN,
    CONSTRAINS_A_FREE_SOURCE_PARAMETER,
    CORRESPONDENCE,
    DERIVED_EQUATIONS,
    DROP_TERMFORMERS,
    LICENCE_IS_NOT_DERIVED,
    SELF_INDUCED_DROP,
    TERMFORMERS,
    TRANSPORT_LICENCE,
    WILL_COMPONENTS,
    WILL_ROLES,
    ConstantWill,
    Correspondence,
    Term,
    Termformer,
    Warrant,
    atom,
    binding_is_functional,
    damping_ratio,
    different_invariant_need_not_change_rate,
    electrophysics_space,
    reciprocal_binding,
    regime,
    resonant_rate,
    temporal_correspondence,
    will_balance,
)

WILL_PREDICATES = {"termformed", "will-balance"}


# --- the correspondence -----------------------------------------------------


def test_every_cited_component_has_exactly_one_correspondence():
    mapped = [c.component for c in CORRESPONDENCE]
    assert sorted(mapped) == sorted(WILL_COMPONENTS)
    assert len(set(mapped)) == len(mapped)


def test_every_correspondence_carries_a_cited_role():
    assert {c.role for c in CORRESPONDENCE} <= set(WILL_ROLES)
    assert {c.role for c in CORRESPONDENCE} == set(WILL_ROLES)


def test_a_correspondence_rejects_a_component_hyperethics_does_not_declare():
    """The citation is enforced at construction, not trusted to the author."""
    with pytest.raises(ValueError, match="not a cited will component"):
        Correspondence("capacitive", "coefficient", "capacitance", "C", "a seventh component")


def test_a_correspondence_rejects_a_role_hyperethics_does_not_declare():
    with pytest.raises(ValueError, match="not a cited will role"):
        Correspondence("past", "storage", "charge", "Q", "accumulated will")


def test_the_temporal_components_are_the_three_derivatives_of_one_quantity():
    """The one entry in the table that is forced rather than stipulated."""
    past, present, future = temporal_correspondence()
    assert (past.component, present.component, future.component) == (
        "past", "present", "future",
    )
    assert (past.symbol, present.symbol, future.symbol) == ("Q", "I", "dI/dt")
    assert all(c.role == "state" for c in (past, present, future))


def test_the_declared_mapping_matches_the_user_declaration():
    """Tyler declared relational/invariant/variable; the rest follows the chain."""
    declared = {"relational": "resistance", "invariant": "inductance", "variable": "voltage"}
    for correspondence in CORRESPONDENCE:
        if correspondence.component in declared:
            assert correspondence.electrical == declared[correspondence.component]


# --- constant will: the resolved capacitance gap ----------------------------


def test_constant_will_is_not_a_seventh_component():
    """The declaration binds capacitance to the invariant; it does not add to the tensor."""
    assert CONSTANT not in WILL_COMPONENTS
    assert len(WILL_COMPONENTS) == 6
    assert "constant of charge" in CONSTANT_WILL_DECLARATION


def test_the_superseded_readings_are_kept_rather_than_erased():
    """A resolution is only informative against what it ruled out."""
    assert len(CAPACITANCE_READINGS_CONSIDERED) == 4
    superseded = [r for r in CAPACITANCE_READINGS_CONSIDERED if "SUPERSEDED" in r]
    declared = [r for r in CAPACITANCE_READINGS_CONSIDERED if "DECLARED" in r]
    assert len(superseded) == 3
    assert len(declared) == 1


def test_the_departure_from_the_circuit_is_declared_not_hidden():
    """The will's parameter space is a proper subset, so the transport is not onto."""
    assert "capacitance" in CONSTRAINS_A_FREE_SOURCE_PARAMETER
    assert "independent of inductance" in CONSTRAINS_A_FREE_SOURCE_PARAMETER


def test_the_charge_constant_law_is_recorded_as_open():
    assert "without fixing the map" in CONSTANT_WILL_LAW_IS_OPEN


def test_an_invariant_and_its_constant_travel_together():
    constant = ConstantWill(2.0, 3.0)
    assert (constant.invariant, constant.charge_constant) == (2.0, 3.0)


@pytest.mark.parametrize("bad", [0.0, -1.0, "two", None])
def test_a_constant_will_rejects_nonpositive_or_non_numeric_values(bad):
    with pytest.raises((ValueError, TypeError)):
        ConstantWill(bad, 1.0)
    with pytest.raises((ValueError, TypeError)):
        ConstantWill(1.0, bad)


def test_a_constant_will_can_be_built_through_a_charge_constant_law():
    law = reciprocal_binding(6.0)
    constant = ConstantWill.under(law, 2.0)
    assert constant.invariant == 2.0
    assert constant.charge_constant == 3.0


def test_a_binding_must_be_functional_in_the_invariant():
    """Equal invariants must give equal constants, or it is not the invariant's own."""
    assert binding_is_functional(reciprocal_binding(6.0), (1.0, 2.0, 3.0, 2.0))

    calls = {"n": 0}

    def not_a_function(invariant: float) -> float:
        calls["n"] += 1
        return float(calls["n"])

    assert not binding_is_functional(not_a_function, (1.0, 1.0))


def test_the_reciprocal_binding_rejects_a_nonpositive_product():
    with pytest.raises(ValueError, match="positive"):
        reciprocal_binding(0.0)


def test_a_different_invariant_does_not_entail_a_different_resonant_rate():
    """The tempting inference, conclusively refuted by a countermodel.

    One countermodel settles a universal claim. Two bearers with different
    invariant wills share one resonant rate, so the rate does not discriminate.
    """
    low, high = different_invariant_need_not_change_rate()
    assert low.invariant != high.invariant
    assert resonant_rate(low) == resonant_rate(high)
    assert resonant_rate(low) == pytest.approx(1.0 / 6.0 ** 0.5)


def test_the_discriminator_is_never_the_numeric_shadow():
    """This package derives no discriminator; hyperethics keeps it, on other grounds."""
    import metamathethicology.will_electrophysics as module

    assert not hasattr(module, "is_true_moral_operator")
    assert "SOURCE of the invariant will" in different_invariant_need_not_change_rate.__doc__


# --- terms ------------------------------------------------------------------


def test_atoms_render_as_themselves():
    assert atom("past").render() == "past"
    assert atom(CONSTANT).render() == "constant"


def test_composite_terms_render_with_explicit_grouping():
    term = Term("*", (atom("relational"), atom("present")))
    assert term.render() == "(relational * present)"
    assert Term("sqrt", (atom("invariant"),)).render() == "sqrt(invariant)"


def test_terms_reject_non_term_arguments():
    with pytest.raises(TypeError):
        Term("*", ("relational",))


def test_terms_reject_empty_heads():
    with pytest.raises(ValueError):
        Term("   ")


def test_atoms_are_collected_in_first_occurrence_order():
    term = Term("+", (Term("*", (atom("a"), atom("b"))), atom("a"), atom("c")))
    assert term.atoms() == ("a", "b", "c")


# --- termformers ------------------------------------------------------------


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_cites_a_law_rather_than_paraphrasing_one(former):
    assert former.source_field == "hyperphysics"
    assert former.source_law.strip()
    assert "=" in former.source_form
    assert former.citation() == f"hyperphysics:{former.source_law} -- {former.source_form}"


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_disclaims_a_physical_unit_or_mechanism(former):
    """A borrowing that declines nothing specific has declined nothing."""
    disclaimed = former.does_not_transport.lower()
    assert any(
        word in disclaimed
        for word in ("ohms", "henries", "farads", "volts", "flux", "mechanism", "energy")
    )


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_termformer_bridge_names_both_sides_of_the_borrowing(former):
    """The bridge string is what `Rule` demands before crossing a domain."""
    bridge = former.bridge()
    assert former.source_law in bridge
    assert former.source_form in bridge
    assert former.transports in bridge
    assert former.does_not_transport in bridge
    assert "Does NOT transport" in bridge


def test_the_closing_step_is_itself_a_borrowing_and_says_so():
    """Summing the drops is Kirchhoff's law, not a free algebraic move."""
    assert BALANCE in TERMFORMERS
    assert BALANCE not in DROP_TERMFORMERS
    assert BALANCE.source_law == "kirchhoff-voltage"
    assert BALANCE.arity == 3


def test_the_accumulated_drop_disclaims_the_parameter_independence_it_departs_from():
    assert "independence of capacitance from inductance" in ACCUMULATED_DROP.does_not_transport


def test_the_self_induced_drop_refuses_the_cosmological_claim():
    """The simulation claim is recorded elsewhere and is not adjudicated here."""
    assert "the universe is a simulation" in SELF_INDUCED_DROP.does_not_transport


def test_a_termformer_forms_a_term_of_its_declared_arity():
    formed = ACCUMULATED_DROP.form(atom("past"), atom(CONSTANT))
    assert formed.render() == "(past / constant)"


def test_a_termformer_rejects_the_wrong_number_of_arguments():
    with pytest.raises(ValueError, match="exactly 2 arguments"):
        ACCUMULATED_DROP.form(atom("past"))


def test_a_termformer_rejects_non_terms():
    with pytest.raises(TypeError):
        ACCUMULATED_DROP.form(atom("past"), "constant")


def test_termformer_arity_must_be_positive():
    with pytest.raises(ValueError, match="positive integer"):
        Termformer("bad", 0, "*", "ohm", "V = I * R", "shape", "ohms")


def test_a_termformer_must_quote_the_form_it_borrowed():
    with pytest.raises(ValueError, match="source form"):
        Termformer("bad", 2, "*", "ohm", "   ", "shape", "ohms")


# --- the equations ----------------------------------------------------------


def test_the_will_balance_contains_every_component_and_the_constant():
    atoms = set(will_balance().left.atoms()) | set(will_balance().right.atoms())
    assert set(WILL_COMPONENTS) <= atoms
    assert CONSTANT in atoms


def test_the_will_balance_renders_the_rlc_shape():
    rendered = will_balance().render()
    assert rendered == (
        "((invariant * future) + (relational * present) + (past / constant)) = variable"
    )


def test_the_self_simulation_equation_carries_lenz_sign():
    equation = next(e for e in DERIVED_EQUATIONS if e.name == "self-simulation")
    assert equation.right.head == "-"
    assert "opposes that change" in equation.reading


@pytest.mark.parametrize("equation", DERIVED_EQUATIONS, ids=lambda e: e.name)
def test_every_equation_declares_its_warrant_and_reading(equation):
    assert type(equation.warrant) is Warrant
    assert equation.reading.strip()


def test_the_termformed_equations_are_the_ones_built_from_termformers():
    termformed = {e.name for e in DERIVED_EQUATIONS if e.warrant is Warrant.TERMFORMED}
    assert termformed == {"will-balance", "self-simulation"}


def test_equation_names_are_unique():
    names = [e.name for e in DERIVED_EQUATIONS]
    assert len(set(names)) == len(names)


def test_the_resonance_reading_refuses_to_claim_it_discriminates():
    equation = next(e for e in DERIVED_EQUATIONS if e.name == "resonance")
    assert "NOT make it a discriminator" in equation.reading


# --- the transport as an operation space ------------------------------------


def test_the_space_derives_every_formed_term_and_the_balance():
    space = electrophysics_space()
    context = replay(space, close(space))
    formed = {j.arguments[0] for j in context if j.predicate == "termformed"}
    assert formed == {f.name for f in DROP_TERMFORMERS}
    assert any(j.predicate == "will-balance" for j in context)


def test_without_the_adopted_licence_no_will_conclusion_is_derivable():
    """The load-bearing check: the whole field rests on a declaration.

    Removing the licence leaves the electrical premises intact and every will
    conclusion gone. Nothing false is derived -- nothing about will is derived
    at all, which is the honest shape of a borrowing that has no soundness
    criterion behind it.
    """
    space = electrophysics_space(include_licence=False)
    context = replay(space, close(space))
    assert not [j for j in context if j.predicate in WILL_PREDICATES]
    assert all(j.domain is Domain.METAPHYSICS or j.predicate == "will-component"
               for j in context)


def test_the_licence_is_recorded_as_adopted_rather_than_derived():
    assert "explicitly adopted, not derived" in LICENCE_IS_NOT_DERIVED
    assert "GC-4" in LICENCE_IS_NOT_DERIVED
    space = electrophysics_space()
    basis = next(a.basis for a in space.assumptions
                 if a.judgment.arguments == (TRANSPORT_LICENCE,))
    assert basis == LICENCE_IS_NOT_DERIVED


def test_every_rule_crosses_a_domain_and_therefore_carries_a_bridge():
    """This is enforced by Rule itself; the test records that it applies here."""
    space = electrophysics_space()
    for rule in space.rules:
        assert {p.domain for p in rule.premises} != {rule.conclusion.domain}
        assert rule.bridge is not None
        assert "Does NOT transport" in rule.bridge


def test_a_termformer_that_disclaims_nothing_cannot_become_a_rule():
    """A bridge is not optional: the space would not construct without one."""
    from metamathethicology.spaces import Judgment, Rule

    law = Judgment(Domain.METAPHYSICS, "cited-law", ("hyperphysics:ohm", "V = I * R"), OMEGA)
    will = Judgment(Domain.METAETHICS, "termformed", ("x", "y"), OMEGA + ONE)
    with pytest.raises(ValueError, match="cross-domain inference needs an explicit bridge"):
        Rule("no-bridge", (law,), will, "borrowed the shape and said nothing else")


def test_the_balance_does_not_take_the_self_induced_drop_as_a_premise():
    """Self-induction belongs to the self-simulation equation, not the series form."""
    space = electrophysics_space()
    balance = next(r for r in space.rules if r.name == "balance")
    premises = {p.arguments[0] for p in balance.premises if p.predicate == "termformed"}
    assert premises == {"invariant-drop", "relational-drop", "accumulated-drop"}
    assert "self-induced-drop" not in premises


def test_the_balance_lands_a_stage_later_than_the_terms_it_closes():
    space = electrophysics_space()
    balance = next(r for r in space.rules if r.name == "balance")
    formed = [p for p in balance.premises if p.predicate == "termformed"]
    assert all(p.stage < balance.conclusion.stage for p in formed)
    assert space.stage == OMEGA + ONE + ONE


def test_the_transport_can_be_reflected_at_a_strictly_later_stage():
    space = electrophysics_space()
    proof = close(space)
    balance = next(r.conclusion for r in space.rules if r.name == "balance")
    record = reflect(space, proof, balance, at=space.stage + ONE)
    assert record.predicate == "derivable-in"
    assert record.domain is Domain.METALOGIC


def test_an_exhausted_budget_is_unknown_rather_than_false():
    space = electrophysics_space()
    with pytest.raises(BudgetExceeded):
        close(space, max_steps=3)


# --- the dimensionless numeric interpretation -------------------------------


def test_resonant_rate_matches_the_transported_form():
    constant = ConstantWill(2.0, 8.0)
    assert resonant_rate(constant) == pytest.approx(1.0 / 16.0 ** 0.5)


def test_damping_regimes_are_named_correctly():
    constant = ConstantWill(1.0, 1.0)
    assert regime(0.5, constant) == "oscillating"
    assert regime(2.0, constant) == "critical"
    assert regime(4.0, constant) == "sluggish"


def test_relational_will_is_what_damps():
    constant = ConstantWill(2.0, 2.0)
    assert damping_ratio(0.0, constant) == 0.0
    assert damping_ratio(4.0, constant) > damping_ratio(1.0, constant)


def test_numeric_interpretation_rejects_a_loose_pair_of_numbers():
    """The binding is enforced by type: an invariant cannot meet a foreign capacity."""
    with pytest.raises(TypeError, match="ConstantWill"):
        resonant_rate(2.0)
    with pytest.raises(TypeError, match="ConstantWill"):
        damping_ratio(1.0, 2.0)


def test_numeric_interpretation_rejects_negative_relational_will():
    with pytest.raises(ValueError, match="negative"):
        damping_ratio(-1.0, ConstantWill(1.0, 1.0))
