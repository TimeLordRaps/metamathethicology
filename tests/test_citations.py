"""Cross-check both cited surfaces against the packages that state them.

`will_electrophysics` combines two fields it does not import. `hyperphysics`
states each electrical law once, with its validity conditions and failure modes;
`hyperethics` states the will tensor once. This module holds them to those
statements whenever either package happens to be importable, because a citation
nobody checks is a paraphrase with extra steps, and paraphrases drift.

Neither package is a declared dependency. That is deliberate: the combination
field should not force a foundation and a physics package into every install of
an operation-space library. The cost is that these checks can be skipped, and a
skip means the citations were NOT checked on that run -- not that they were
checked and passed. `VALIDATION.md` records which of the two happened.
"""

from __future__ import annotations

import pytest

from metamathethicology.will_electrophysics import (
    ACCUMULATED_DROP,
    BALANCE,
    CONSTRAINS_A_FREE_SOURCE_PARAMETER,
    CORRESPONDENCE,
    DROP_TERMFORMERS,
    TERMFORMERS,
    WILL_COMPONENTS,
    WILL_ROLES,
    electrophysics_space,
)

hyperphysics = pytest.importorskip(
    "hyperphysics",
    reason="hyperphysics is not installed, so the cited laws cannot be checked",
)
hyperethics = pytest.importorskip(
    "hyperethics",
    reason="hyperethics is not installed, so the cited will tensor cannot be checked",
)


# --- the cited laws ---------------------------------------------------------


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_cited_law_exists_in_hyperphysics(former):
    """A citation with no referent is the failure this interface exists to catch."""
    assert former.source_law in hyperphysics.LAWS_BY_NAME, (
        f"{former.name} cites '{former.source_law}', which hyperphysics does not state"
    )


@pytest.mark.parametrize("former", TERMFORMERS, ids=lambda f: f.name)
def test_every_quoted_form_matches_the_law_it_quotes(former):
    """The quoted form is a convenience, so it must not drift from the source."""
    law = hyperphysics.LAWS_BY_NAME[former.source_law]
    assert former.source_form == law.form


def test_the_will_balance_borrows_every_constituent_of_the_series_form():
    """All four series constituents are cited, including the one that closes them."""
    constituents = {law.name for law in hyperphysics.SERIES_RLC_CONSTITUENTS}
    borrowed = {f.source_law for f in TERMFORMERS}
    assert constituents <= borrowed
    assert BALANCE.source_law in constituents


def test_self_and_mutual_induction_are_the_distinction_hyperethics_discriminates_on():
    """hyperphysics records that the two differ only in source, not in form."""
    self_law = hyperphysics.LAWS_BY_NAME["self-inductance"]
    mutual = hyperphysics.LAWS_BY_NAME["mutual-inductance"]
    renamed = self_law.form.replace("L", "M").replace("dI/dt", "dI_1/dt")
    assert renamed == mutual.form.replace("emf_2", "emf")


def test_the_declared_departure_is_a_parameter_the_source_really_leaves_free():
    """Constraining capacitance is a departure only because a circuit leaves it free."""
    assert hyperphysics.Quantity.CAPACITANCE in hyperphysics.PARAMETERS_ARE_INDEPENDENT
    assert "capacitance" in CONSTRAINS_A_FREE_SOURCE_PARAMETER


def test_the_borrowing_satisfies_the_transport_interface():
    """Build hyperphysics Transports from the termformers and validate them."""
    transports = tuple(
        hyperphysics.Transport(
            law=former.source_law,
            target_field="metamathethicology.will_electrophysics",
            target_form=former.head,
            transports=former.transports,
            does_not_transport=former.does_not_transport,
            warrant=hyperphysics.Warrant.BORROWED_FORM,
            constrains_parameters=(
                (hyperphysics.Quantity.CAPACITANCE,) if former is ACCUMULATED_DROP else ()
            ),
            constraint_reason=(
                CONSTRAINS_A_FREE_SOURCE_PARAMETER if former is ACCUMULATED_DROP else ""
            ),
        )
        for former in TERMFORMERS
    )
    for transport in transports:
        assert hyperphysics.validate(transport) is transport
    assert hyperphysics.audit(transports)


def test_transporting_the_capacitor_relation_inherits_its_failure_modes():
    """What the combination takes on by borrowing, listed by the source."""
    transport = hyperphysics.Transport(
        law=ACCUMULATED_DROP.source_law,
        target_field="metamathethicology.will_electrophysics",
        target_form="past / constant",
        transports=ACCUMULATED_DROP.transports,
        does_not_transport=ACCUMULATED_DROP.does_not_transport,
        warrant=hyperphysics.Warrant.BORROWED_FORM,
    )
    modes = hyperphysics.inherited_failure_modes(transport)
    assert any("dielectric" in mode for mode in modes)


def test_units_do_not_transport_is_the_standing_rule_on_every_side():
    assert "do not attach to the algebraic form" in hyperphysics.UNITS_DO_NOT_TRANSPORT


def test_the_licence_this_field_adopts_is_the_one_hyperphysics_leaves_open():
    """hyperphysics says plainly that validation is not a soundness check."""
    assert "does not check that the transport is sound" in hyperphysics.validate.__doc__


# --- the cited will tensor --------------------------------------------------


def test_the_cited_components_are_exactly_the_ones_hyperethics_declares():
    """The citation that keeps the combination from inventing a will of its own."""
    declared = tuple(c.value for c in hyperethics.Component)
    assert set(WILL_COMPONENTS) == set(declared)
    assert len(WILL_COMPONENTS) == len(declared) == 6


def test_the_cited_roles_are_exactly_the_ones_hyperethics_declares():
    declared = {r.value for r in hyperethics.Role}
    assert set(WILL_ROLES) == declared


def test_every_correspondence_gives_a_component_the_role_hyperethics_gives_it():
    """A component's role is hyperethics' claim; this field may map it, not change it."""
    declared = {c.value: hyperethics.role_of(c).value for c in hyperethics.Component}
    for correspondence in CORRESPONDENCE:
        assert correspondence.role == declared[correspondence.component]


def test_the_temporal_chain_agrees_with_the_one_hyperethics_orders():
    ordered = tuple(c.value for c in hyperethics.temporal_chain())
    assert ordered == ("past", "present", "future")


def test_the_self_induced_drop_names_the_hyperethics_derivation_it_reproduces():
    """The transport's best evidence is that it lands on an independently derived result."""
    from metamathethicology.will_electrophysics import SELF_INDUCED_DROP

    assert "d-no-exterior" in SELF_INDUCED_DROP.transports
    assert hyperethics.d_no_exterior is not None


def test_hyperethics_keeps_the_discriminator_and_this_field_does_not_move_it():
    """The moral-operator test is a will question and stays in the will foundation."""
    import metamathethicology.will_electrophysics as module

    assert hasattr(hyperethics, "is_true_moral_operator")
    assert not hasattr(module, "is_true_moral_operator")
    assert not hasattr(module, "WillProfile")


def test_hyperethics_does_not_import_this_combination_back():
    """The dependency runs one way; a foundation that imported its combination would cycle."""
    import hyperethics.will as will_module

    source = will_module.__doc__ or ""
    assert "metamathethicology" in source
    assert not hasattr(will_module, "Termformer")
    assert not hasattr(will_module, "CORRESPONDENCE")


# --- the two citations meeting ---------------------------------------------


def test_the_space_premises_name_the_field_each_one_is_cited_from():
    """Every assumption in the transport is traceable to the package that states it."""
    space = electrophysics_space()
    laws = [a for a in space.assumptions if a.judgment.predicate == "cited-law"]
    components = [a for a in space.assumptions if a.judgment.predicate == "will-component"]
    assert len(laws) == len(TERMFORMERS)
    assert len(components) == len(CORRESPONDENCE)
    for assumption in laws:
        name = assumption.judgment.arguments[0].split(":", 1)[1]
        assert name in hyperphysics.LAWS_BY_NAME
    for assumption in components:
        name = assumption.judgment.arguments[0].split(":", 1)[1]
        assert name in {c.value for c in hyperethics.Component}


def test_each_drop_borrows_a_distinct_law():
    """Four drops, four different laws: none is doing two jobs quietly."""
    borrowed = [f.source_law for f in DROP_TERMFORMERS]
    assert len(set(borrowed)) == len(borrowed)
    assert all(name in hyperphysics.LAWS_BY_NAME for name in borrowed)
