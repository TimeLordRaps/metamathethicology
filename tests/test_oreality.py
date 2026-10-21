"""Oreality, the declared realms, and the licence every reading rests on.

These tests check that the combination is stated completely, that the
declaration is quoted rather than paraphrased, and that the readings' dependence
on an adopted licence is visible in the closure rather than only in prose. They
need neither parent package. They establish nothing about any realm and nothing
beyond what hyperprobability states.
"""

from __future__ import annotations

from fractions import Fraction

import pytest
from ordinatics.ordinals import OMEGA, ONE

from metamathethicology import (
    BudgetExceeded,
    Domain,
    Judgment,
    Rule,
    close,
    encode_space,
    oreality,
    reflect,
    replay,
)
from metamathethicology.oreality import (
    AREALITY,
    BIASED_COIN,
    CHAIN,
    CITATIONS,
    CITATIONS_BY_LABEL,
    CITED_VALUES,
    CLOCK,
    DECLARATION,
    DIMENSIONS_DO_NOT_TRANSPORT,
    FAIR_COIN,
    KAC_WITNESSES,
    LICENCE_IS_NOT_DERIVED,
    LOOP,
    O_IS_ORDINAL,
    OREALITY,
    OUR_REALITY,
    OUR_REALITY_READINGS_CONSIDERED,
    PREALITY,
    PRESENTATIONS,
    READING_LICENCE,
    REALM_NAMES,
    REALMS,
    REALMS_BY_NAME,
    SERIES_SPRING,
    SPEC_LABELS,
    SPRING_DECLARATION,
    SPRING_LAW_IS_OPEN,
    SWAP,
    Citation,
    CitedKacBound,
    CitedValues,
    Presentation,
    Realm,
    SpringCandidate,
    oreality_bounds_our_reality,
    oreality_space,
    our_reality_does_not_fix_oreality,
    possibility_does_not_fix_our_reality,
)

HALF = Fraction(1, 2)


def _judgments(space):
    """Every judgment the space mentions: assumptions, premises and conclusions."""
    found = [a.judgment for a in space.assumptions]
    for rule in space.rules:
        found.extend((*rule.premises, rule.conclusion))
    return found


def _realm(**changes):
    fields = dict(
        name="Areality", declared=AREALITY.declared, reads_as="r", transports="t",
        does_not_transport="d", cites=("Definition 1.1",),
    )
    fields.update(changes)
    return Realm(**fields)


# --- the declaration --------------------------------------------------------


def test_the_declaration_is_quoted_whole():
    assert DECLARATION.startswith("And also then this allows for us in metamathethicology")
    assert DECLARATION.endswith("hyperprobabilistically through Oreality.")
    assert "  " not in DECLARATION


@pytest.mark.parametrize("realm", REALMS, ids=lambda r: r.name)
def test_every_realm_quotes_a_fragment_of_the_declaration(realm):
    assert realm.declared in DECLARATION


def test_the_realms_are_exactly_the_ones_the_declaration_names():
    assert tuple(r.name for r in REALMS) == REALM_NAMES
    for name in ("Areality", "Preality", "Oreality", "Our reality"):
        assert name in DECLARATION
    assert set(REALMS_BY_NAME) == set(REALM_NAMES)


def test_the_declaration_names_ordinatics_and_never_expands_the_o():
    assert "through ordinatics" in DECLARATION
    assert "Ordinal" not in DECLARATION


def test_the_o_expansion_is_proposed_and_nothing_rests_on_it():
    """PROPOSED, not declared: no basis cites it and no judgment mentions it."""
    assert O_IS_ORDINAL.startswith("PROPOSED")
    space = oreality_space()
    assert all(O_IS_ORDINAL not in a.basis for a in space.assumptions)
    for judgment in _judgments(space):
        assert not any("Ordinal" in argument for argument in judgment.arguments)
    assert "what the O stands for" in OREALITY.does_not_transport


# --- citations --------------------------------------------------------------


@pytest.mark.parametrize("citation", CITATIONS, ids=lambda c: c.label)
def test_every_citation_carries_a_spec_label_and_a_quote(citation):
    assert any(label in citation.status for label in SPEC_LABELS)
    assert citation.quotes


def test_citation_labels_are_unique():
    assert len(CITATIONS_BY_LABEL) == len(CITATIONS)


def test_a_heading_renders_as_the_spec_prints_it():
    assert CITATIONS_BY_LABEL["Proposition 2.7"].heading() == (
        "**Proposition 2.7.** KNOWN (a, b); PROVED (c, d)."
    )
    assert CITATIONS_BY_LABEL["Theorem 6.2"].heading() == (
        "**Theorem 6.2 (the Kac bridge).** PROVED."
    )


def test_the_cited_readings_are_labelled_as_readings():
    """Two cited results are the SPEC's own INTERPRETATIONs, and they say so here."""
    readings = {c.label for c in CITATIONS if c.status == "INTERPRETATION"}
    assert readings == {"Remark 1.3", "Remark 5.4"}


@pytest.mark.parametrize("realm", REALMS, ids=lambda r: r.name)
def test_every_reading_rests_on_at_least_one_result_that_is_not_a_reading(realm):
    assert any(CITATIONS_BY_LABEL[label].status != "INTERPRETATION" for label in realm.cites)


def test_a_citation_rejects_a_status_the_spec_does_not_use():
    with pytest.raises(ValueError, match="not a SPEC label"):
        Citation("Theorem", "9.9", None, "PROVEN", ("a sentence",))


def test_a_citation_rejects_a_kind_of_result_the_spec_does_not_state():
    with pytest.raises(ValueError, match="not a kind of result"):
        Citation("Axiom", "9.9", None, "PROVED", ("a sentence",))


def test_a_citation_must_quote_its_result():
    with pytest.raises(ValueError, match="quotes at least one sentence"):
        Citation("Theorem", "9.9", None, "PROVED", ())


# --- the realms -------------------------------------------------------------


def test_a_realm_the_declaration_does_not_name_is_refused():
    with pytest.raises(ValueError, match="not a declared realm"):
        _realm(name="Surreality")


def test_a_paraphrased_fragment_is_refused():
    """The declaration is the only referent; a paraphrase would leave none."""
    with pytest.raises(ValueError, match="not in the declaration"):
        _realm(declared="Areality (abstract reality)")


def test_a_realm_cannot_cite_a_result_that_is_not_cited():
    with pytest.raises(ValueError, match="not a cited result"):
        _realm(cites=("Theorem 9.9",))


def test_a_realm_cannot_arise_from_itself_or_from_an_undeclared_realm():
    with pytest.raises(ValueError, match="other declared realms"):
        _realm(arises_from=("Areality",))
    with pytest.raises(ValueError, match="other declared realms"):
        _realm(arises_from=("Surreality",))


def test_a_realm_must_disclaim_something():
    with pytest.raises(ValueError, match="does_not_transport"):
        _realm(does_not_transport="   ")


@pytest.mark.parametrize("realm", REALMS, ids=lambda r: r.name)
def test_every_realm_bridge_names_both_sides_of_the_reading(realm):
    """The bridge string is what `Rule` demands before crossing a domain."""
    bridge = realm.bridge()
    assert realm.citation() in bridge
    assert all(label in bridge for label in realm.cites)
    assert realm.reads_as in bridge
    assert realm.transports in bridge
    assert realm.does_not_transport in bridge
    assert "Does NOT transport" in bridge


def test_the_declared_order_is_recorded_and_nothing_more():
    assert AREALITY.arises_from == PREALITY.arises_from == ()
    assert OREALITY.arises_from == ("Areality",)
    assert set(OUR_REALITY.arises_from) == {"Preality", "Areality", "Oreality"}


def test_areality_is_read_only_through_its_coherent_projections():
    assert AREALITY.reads_as.startswith("not Areality itself")
    assert "which abstract thoughts exist" in AREALITY.does_not_transport


def test_preality_reads_possibility_as_support_and_names_no_cosmology():
    assert "support and not weight" in PREALITY.transports
    assert "block multiverse" in PREALITY.reads_as
    assert "identification with any cosmology stated elsewhere" in PREALITY.does_not_transport


def test_our_reality_is_read_as_a_law_and_the_passed_over_reading_is_kept():
    """A choice is only informative against what it passed over."""
    assert len(OUR_REALITY_READINGS_CONSIDERED) == 2
    rejected = [r for r in OUR_REALITY_READINGS_CONSIDERED if "NOT ADOPTED" in r]
    adopted = [r for r in OUR_REALITY_READINGS_CONSIDERED if "-- ADOPTED" in r]
    assert len(rejected) == len(adopted) == 1
    assert "in-universe law" in adopted[0]
    assert "which run is ours" in OUR_REALITY.does_not_transport


def test_the_dimension_counts_are_preserved_and_not_read():
    assert "4D" in DECLARATION and "5+dimensional" in DECLARATION
    assert "no dimensions" in DIMENSIONS_DO_NOT_TRANSPORT
    assert "5+" in PREALITY.does_not_transport
    assert "4 and 5+" in OUR_REALITY.does_not_transport
    assert all("dimension" not in realm.reads_as for realm in REALMS)


# --- coherent projections ---------------------------------------------------


def test_presentations_of_the_same_universe_compare_equal():
    written = Presentation.of(
        "clock", {"tock": {"tick": Fraction(1)}, "tick": {"tock": 1}},
        event="tock", start="tick",
    )
    assert written == CLOCK


def test_zero_weights_are_not_possibilities():
    presentation = Presentation.of(
        "z", {"a": {"a": 1, "b": 0}, "b": {"b": 1}}, event="a", start="a",
    )
    assert presentation.kernel[0] == ("a", (("a", Fraction(1)),))


@pytest.mark.parametrize(
    ("kernel", "reason"),
    [
        ({}, "no states"),
        ({"a": {"a": HALF}}, "sums to 1/2"),
        ({"a": {"b": 1}}, "not a state"),
        ({"a": {"a": 0.5, "b": 0.5}, "b": {"b": 1}}, "not an exact rational"),
        ({"a": {"a": True}}, "not an exact rational"),
        ({"a": {"a": 2, "b": -1}, "b": {"b": 1}}, "positive exact rational"),
        ({"a": {}}, "is empty"),
    ],
    ids=["empty", "short-row", "outside", "float", "bool", "negative", "empty-row"],
)
def test_an_incoherent_projection_cannot_be_built(kernel, reason):
    with pytest.raises(ValueError, match=f"not a coherent projection: .*{reason}"):
        Presentation.of("bad", kernel, event="a", start="a")


def test_the_event_and_start_must_be_states():
    with pytest.raises(ValueError, match="the event 'z' is not a state"):
        Presentation.deterministic("bad", {"a": "a"}, event="z", start="a")
    with pytest.raises(ValueError, match="the start 'z' is not a state"):
        Presentation.deterministic("bad", {"a": "a"}, event="a", start="z")


@pytest.mark.parametrize(
    ("limits", "reason"),
    [
        (({("a", "z"): "a"},), "not a set of states"),
        (({("a", "b"): "z"},), "not a state"),
        (({("a", "b"): "a", ("b", "a"): "b"},), "twice"),
    ],
    ids=["key-outside", "target-outside", "duplicate-key"],
)
def test_an_incoherent_limit_rule_cannot_be_built(limits, reason):
    with pytest.raises(ValueError, match=f"not a coherent projection: .*{reason}"):
        Presentation.deterministic("bad", {"a": "b", "b": "a"}, event="a", start="a",
                                   limits=limits)


def test_whether_a_limit_key_is_an_attractor_is_left_to_hyperprobability():
    """{a} is not an attractor of a two-cycle; hyperprobability's Universe refuses it."""
    presentation = Presentation.deterministic(
        "not an attractor", {"a": "b", "b": "a"}, event="a", start="a",
        limits=({("a",): "b"},),
    )
    assert presentation.limits == (((("a",), "b"),),)


def test_possibility_is_support_and_weight_is_what_a_projection_adds():
    assert FAIR_COIN.possibility() == BIASED_COIN.possibility()
    assert FAIR_COIN.weights() != BIASED_COIN.weights()


def test_possibility_includes_the_limit_rules():
    assert LOOP.possibility() != LOOP.collapsed().possibility()
    assert LOOP.possibility()[0] == LOOP.collapsed().possibility()[0]


def test_collapsing_keeps_the_kernel_and_drops_every_limit_rule():
    collapsed = LOOP.collapsed()
    assert collapsed.name == "loop, collapsed"
    assert collapsed.kernel == LOOP.kernel
    assert collapsed.limits == ()
    assert (collapsed.event, collapsed.start) == (LOOP.event, LOOP.start)


def test_universe_arguments_have_the_shape_hyperprobability_takes():
    kernel, limits = LOOP.universe_arguments()
    assert kernel == {
        "a": {"b": Fraction(1)}, "b": {"a": Fraction(1)}, "out": {"out": Fraction(1)},
    }
    assert limits == [{frozenset({"a", "b"}): "out"}]
    assert len(SWAP.universe_arguments()[1]) == 2


# --- recorded values --------------------------------------------------------


def test_every_presentation_has_its_recorded_values():
    assert set(CITED_VALUES) == {p.name for p in PRESENTATIONS}
    for presentation in PRESENTATIONS:
        assert CITED_VALUES[presentation.name].presentation == presentation


def test_a_frequency_that_is_not_the_mass_on_the_event_cannot_be_recorded():
    with pytest.raises(ValueError, match="mass on the event"):
        CitedValues(FAIR_COIN, (("H", HALF), ("T", HALF)), Fraction(1, 3), OMEGA)


def test_an_in_universe_law_must_be_a_law_on_the_states():
    with pytest.raises(ValueError, match="positive exact law"):
        CitedValues(FAIR_COIN, (("H", HALF),), HALF, OMEGA)
    with pytest.raises(ValueError, match="positive exact law"):
        CitedValues(FAIR_COIN, (("H", HALF), ("Z", HALF)), HALF, OMEGA)


def test_corollary_5_3_is_enforced_when_no_strange_loop_is_recorded():
    with pytest.raises(ValueError, match="Corollary 5.3"):
        CitedValues(FAIR_COIN, (("H", HALF), ("T", HALF)), HALF, OMEGA + ONE)


def test_every_guarantee_past_omega_comes_with_a_strange_loop():
    """Corollary 5.3, read the other way, on every record."""
    for values in CITED_VALUES.values():
        guarantee = values.hyperprobability
        if guarantee is not None and not guarantee.is_finite and guarantee != OMEGA:
            assert values.strange_loops


def test_an_infinite_guarantee_is_recorded_as_none():
    assert CITED_VALUES["loop, collapsed"].hyperprobability is None


# --- the Kac records --------------------------------------------------------


def test_a_kac_record_that_breaks_the_proved_bound_cannot_be_built():
    with pytest.raises(ValueError, match="contradicts Theorem 6.2"):
        CitedKacBound(CLOCK, ("tick", "tock"), Fraction(1, 3), ONE + ONE, tight=False)
    with pytest.raises(ValueError, match="contradicts Theorem 6.2"):
        CitedKacBound(FAIR_COIN, ("H", "T"), Fraction(0), OMEGA, tight=False)


def test_a_kac_record_cannot_misreport_tightness():
    with pytest.raises(ValueError, match="tight must mean equality"):
        CitedKacBound(CLOCK, ("tick", "tock"), HALF, ONE + ONE, tight=False)
    with pytest.raises(ValueError, match="tight must mean equality"):
        CitedKacBound(FAIR_COIN, ("H", "T"), HALF, OMEGA, tight=True)


def test_a_kac_record_must_name_an_attractor_meeting_the_event():
    with pytest.raises(ValueError, match="meeting its event"):
        CitedKacBound(CLOCK, ("tick",), HALF, ONE + ONE, tight=True)


def test_an_infinite_return_guarantee_bounds_by_an_infinitesimal():
    fair, biased, clock = KAC_WITNESSES
    assert fair.bound() is None and biased.bound() is None
    assert clock.bound() == HALF


# --- what each realm carries ------------------------------------------------


def test_our_reality_does_not_fix_oreality():
    loop, collapsed = our_reality_does_not_fix_oreality()
    assert loop.in_universe == collapsed.in_universe
    assert loop.hyperprobability == OMEGA
    assert collapsed.hyperprobability is None
    assert loop.strange_loops and not collapsed.strange_loops


def test_the_chain_is_a_second_witness_with_the_same_our_reality():
    chain = CITED_VALUES[CHAIN.name]
    assert chain.in_universe == CITED_VALUES[LOOP.name].in_universe
    assert chain.hyperprobability == OMEGA + ONE + ONE + ONE


def test_possibility_does_not_fix_our_reality():
    fair, biased = possibility_does_not_fix_our_reality()
    assert fair.hyperprobability == biased.hyperprobability == OMEGA
    assert (fair.frequency, biased.frequency) == (HALF, Fraction(1, 3))


def test_oreality_bounds_our_reality_in_both_of_its_cases():
    fair, biased, clock = oreality_bounds_our_reality()
    assert clock.tight and clock.return_guarantee == ONE + ONE
    assert not fair.tight and not biased.tight
    assert all(bound.holds() for bound in (fair, biased, clock))


def test_a_refutation_notices_when_its_witnesses_lose_their_shape(monkeypatch):
    """A refutation that could not fail would establish nothing."""
    same = CitedValues(LOOP.collapsed(), (("a", HALF), ("b", HALF)), Fraction(0), OMEGA)
    monkeypatch.setitem(oreality.CITED_VALUES, "loop, collapsed", same)
    with pytest.raises(AssertionError, match="differ in Oreality"):
        our_reality_does_not_fix_oreality()


def test_the_possibility_refutation_notices_a_changed_witness(monkeypatch):
    same = CitedValues(BIASED_COIN, (("H", HALF), ("T", HALF)), HALF, OMEGA)
    monkeypatch.setitem(oreality.CITED_VALUES, "biased coin", same)
    with pytest.raises(AssertionError, match="differ in our reality"):
        possibility_does_not_fix_our_reality()


# --- the spring -------------------------------------------------------------


def test_the_spring_is_declared_tentatively_and_kept_that_way():
    assert "might" in SPRING_DECLARATION
    assert SPRING_DECLARATION in DECLARATION
    assert SPRING_LAW_IS_OPEN.startswith("No spring law is adopted")


def test_the_spring_candidate_cites_a_law_and_says_why_it_is_not_adopted():
    assert SERIES_SPRING.citation() == (
        "hyperphysics:series-rlc -- L * d2Q/dt2 + R * dQ/dt + (1/C) * Q = V"
    )
    assert len(SERIES_SPRING.not_adopted_because) == 4
    assert any("might" in reason for reason in SERIES_SPRING.not_adopted_because)
    assert any("discrete" in reason for reason in SERIES_SPRING.not_adopted_because)


def test_the_spring_candidate_disclaims_units_mechanism_and_time():
    for phrase in ("henry", "mechanism", "continuous time"):
        assert phrase in SERIES_SPRING.does_not_transport


def test_an_unadopted_candidate_must_say_why():
    with pytest.raises(ValueError, match="why it is not adopted"):
        SpringCandidate("s", "series-rlc", "form", "target", "t", "the henry", ())


def test_no_rule_takes_a_spring_premise():
    space = oreality_space()
    for judgment in _judgments(space):
        assert judgment.predicate != "cited-law"
        assert not any("hyperphysics" in argument for argument in judgment.arguments)


# --- the readings as an operation space -------------------------------------


def test_the_space_reads_every_realm_one_stage_after_what_it_reads_through():
    space = oreality_space()
    context = replay(space, close(space))
    stages = {j.arguments[0]: j.stage for j in context if j.predicate == "realm-reading"}
    assert stages == {
        "Areality": OMEGA + ONE,
        "Preality": OMEGA + ONE,
        "Oreality": OMEGA + ONE + ONE,
        "our reality": OMEGA + ONE + ONE + ONE,
    }
    assert space.stage == OMEGA + ONE + ONE + ONE


def test_without_the_adopted_licence_no_realm_is_read():
    """The load-bearing check: every reading rests on a declaration.

    Removing the licence leaves the cited results and the declared realms
    intact and every reading gone. Nothing false is derived -- nothing about
    any realm is derived at all.
    """
    space = oreality_space(include_licence=False)
    proof = close(space)
    assert proof.steps == ()
    assert not [j for j in replay(space, proof) if j.predicate == "realm-reading"]


def test_the_licence_is_recorded_as_adopted_rather_than_derived():
    assert "explicitly adopted, not derived" in LICENCE_IS_NOT_DERIVED
    assert "INTERPRETATION" in LICENCE_IS_NOT_DERIVED
    space = oreality_space()
    basis = next(a.basis for a in space.assumptions
                 if a.judgment.arguments == (READING_LICENCE,))
    assert basis == LICENCE_IS_NOT_DERIVED


def test_every_rule_crosses_from_cited_results_and_carries_its_realms_bridge():
    space = oreality_space()
    assert len(space.rules) == len(REALMS)
    for rule in space.rules:
        realm = REALMS_BY_NAME[rule.conclusion.arguments[0]]
        assert Domain.METAMATH in {p.domain for p in rule.premises}
        assert rule.conclusion.domain is Domain.METAPHYSICS
        assert rule.bridge == realm.bridge()


def test_every_rule_cites_exactly_the_results_its_realm_names():
    space = oreality_space()
    for rule in space.rules:
        realm = REALMS_BY_NAME[rule.conclusion.arguments[0]]
        cited = {p.arguments[0] for p in rule.premises if p.predicate == "cited-result"}
        assert cited == {f"hyperprobability:{label}" for label in realm.cites}


def test_oreality_is_read_after_areality_and_our_reality_after_all_three():
    space = oreality_space()
    rules = {rule.name: rule for rule in space.rules}

    def read_before(name):
        return {p.arguments[0] for p in rules[name].premises if p.predicate == "realm-reading"}

    assert read_before("read-areality") == read_before("read-preality") == set()
    assert read_before("read-oreality") == {"Areality"}
    assert read_before("read-our-reality") == {"Preality", "Areality", "Oreality"}


def test_the_cited_results_enter_the_space_with_their_spec_labels():
    space = oreality_space()
    cited = [a.judgment for a in space.assumptions if a.judgment.predicate == "cited-result"]
    assert len(cited) == len(CITATIONS)
    for judgment in cited:
        label = judgment.arguments[0].split(":", 1)[1]
        assert judgment.arguments[1] == CITATIONS_BY_LABEL[label].status
        assert judgment.domain is Domain.METAMATH


def test_every_declared_realm_enters_the_space_verbatim():
    space = oreality_space()
    declared = [a.judgment for a in space.assumptions if a.judgment.predicate == "declared-realm"]
    assert [j.arguments[0] for j in declared] == list(REALM_NAMES)
    assert all(j.arguments[1] in DECLARATION for j in declared)


def test_a_reading_that_disclaims_nothing_cannot_become_a_rule():
    """A bridge is not optional: the space would not construct without one."""
    cited = Judgment(Domain.METAMATH, "cited-result",
                     ("hyperprobability:Definition 2.6", "DEFINITION"), OMEGA)
    reading = Judgment(Domain.METAPHYSICS, "realm-reading", ("our reality", "in_uni"),
                       OMEGA + ONE)
    with pytest.raises(ValueError, match="cross-domain inference needs an explicit bridge"):
        Rule("no-bridge", (cited,), reading, "read the structure and said nothing else")


def test_the_readings_can_be_reflected_at_a_strictly_later_stage():
    space = oreality_space()
    proof = close(space)
    ours = next(r.conclusion for r in space.rules if r.name == "read-our-reality")
    record = reflect(space, proof, ours, at=space.stage + ONE)
    assert record.predicate == "derivable-in"
    assert record.domain is Domain.METALOGIC


def test_an_exhausted_budget_is_unknown_rather_than_false():
    with pytest.raises(BudgetExceeded):
        close(oreality_space(), max_steps=3)


def test_the_space_encodes_deterministically():
    assert encode_space(oreality_space()) == encode_space(oreality_space())
