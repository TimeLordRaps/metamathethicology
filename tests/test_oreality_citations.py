"""Cross-check Oreality's citations against the packages that state them.

`oreality` reads the declared realms through `hyperprobability` and records one
spring candidate from `hyperphysics`, and it imports neither. This module holds
each citation to its source whenever the source is importable: every heading
and quote to hyperprobability's SPEC, every code name and recorded value to the
package, and the spring candidate to the law it quotes.

Neither package is a declared dependency, for the reason `test_citations.py`
gives. A skip means these citations were NOT checked on that run -- not that
they were checked and passed. `VALIDATION.md` records which of the two happened.
"""

from __future__ import annotations

import re
from fractions import Fraction
from pathlib import Path

import pytest
from ordinatics.ordinals import OMEGA

from metamathethicology.oreality import (
    BIASED_COIN,
    CITATIONS,
    CITED_VALUES,
    FAIR_COIN,
    KAC_WITNESSES,
    LOOP,
    PRESENTATIONS,
    SERIES_SPRING,
    Presentation,
)

#: Where a numbered result of the SPEC begins.
RESULT_HEADING = re.compile(
    r"\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark) \d+\.\d+"
)


@pytest.fixture(scope="module")
def hp():
    return pytest.importorskip(
        "hyperprobability",
        reason="hyperprobability is not installed, so the cited results cannot be checked",
    )


@pytest.fixture(scope="module")
def spec(hp):
    """The SPEC with its whitespace normalized, so line breaks cannot hide a quote."""
    path = Path(hp.__file__).resolve().parents[2] / "SPEC.md"
    if not path.is_file():
        pytest.skip("hyperprobability is installed without its SPEC, so no quote can be checked")
    return _normalized(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def hyperphysics():
    return pytest.importorskip(
        "hyperphysics",
        reason="hyperphysics is not installed, so the spring candidate cannot be checked",
    )


def _normalized(text):
    return " ".join(text.split())


def _section(spec, citation):
    """One result's text: from its heading to the next result's heading."""
    heading = _normalized(citation.heading())
    start = spec.index(heading)
    after = RESULT_HEADING.search(spec, start + len(heading))
    return spec[start:after.start() if after else len(spec)]


def _universe(hp, presentation):
    return hp.Universe(*presentation.universe_arguments())


def _positive(law):
    return tuple(sorted((state, mass) for state, mass in law.items() if mass))


# --- the SPEC ---------------------------------------------------------------


@pytest.mark.parametrize("citation", CITATIONS, ids=lambda c: c.label)
def test_every_cited_heading_is_in_the_spec_exactly_once(spec, citation):
    """The heading carries the claim label, so a relabelled result fails here."""
    assert spec.count(_normalized(citation.heading())) == 1


@pytest.mark.parametrize("citation", CITATIONS, ids=lambda c: c.label)
def test_every_quote_is_in_the_result_it_is_cited_from(spec, citation):
    section = _section(spec, citation)
    for quote in citation.quotes:
        assert _normalized(quote) in section, f"{citation.label} does not say {quote!r}"


@pytest.mark.parametrize("citation", [c for c in CITATIONS if c.code], ids=lambda c: c.label)
def test_every_cited_code_name_exists_in_hyperprobability(hp, citation):
    for name in citation.code:
        target = hp
        for part in name.split("."):
            assert hasattr(target, part), f"{citation.label} cites {name}, which does not exist"
            target = getattr(target, part)


# --- the recorded values ----------------------------------------------------


@pytest.mark.parametrize("presentation", PRESENTATIONS, ids=lambda p: p.name)
def test_every_recorded_value_is_what_hyperprobability_computes(hp, presentation):
    universe = _universe(hp, presentation)
    values = CITED_VALUES[presentation.name]
    event, start = presentation.event, presentation.start
    assert _positive(universe.in_uni(start)) == values.in_universe
    assert hp.frequency(universe, event, start) == values.frequency
    guarantee = hp.hyperprobability(universe, event, start)
    assert (None if guarantee is hp.INFINITY else guarantee) == values.hyperprobability
    loops = tuple((attractor.level, attractor.states) for attractor in hp.strange_loops(universe))
    assert loops == values.strange_loops


@pytest.mark.parametrize("presentation", PRESENTATIONS, ids=lambda p: p.name)
def test_collapsing_every_attractor_makes_the_law_at_omega_our_reality(hp, presentation):
    """Proposition 2.7(c), on every witness: the reading of our reality is exact."""
    law = _universe(hp, presentation.collapsed()).law(presentation.start, OMEGA)
    assert _positive(law) == CITED_VALUES[presentation.name].in_universe


@pytest.mark.parametrize("record", KAC_WITNESSES, ids=lambda k: k.presentation.name)
def test_every_kac_record_is_what_hyperprobability_computes(hp, record):
    universe = _universe(hp, record.presentation)
    bounds = [
        bound for bound in hp.kac(universe, record.presentation.event)
        if bound.attractor.states == record.attractor
    ]
    assert len(bounds) == 1
    (bound,) = bounds
    assert bound.frequency == record.frequency
    assert bound.guarantee == record.return_guarantee
    assert bound.tight is record.tight
    assert bound.holds and record.holds()


@pytest.mark.parametrize("event", ["H", "T"])
@pytest.mark.parametrize("start", ["H", "T"])
def test_the_coins_share_every_hyperprobability(hp, event, start):
    """Proposition 4.9: the same supports give the same guarantees, whatever the weights."""
    fair, biased = _universe(hp, FAIR_COIN), _universe(hp, BIASED_COIN)
    assert hp.hyperprobability(fair, event, start) == hp.hyperprobability(biased, event, start)


@pytest.mark.parametrize(
    "presentation",
    [p for p in PRESENTATIONS if not CITED_VALUES[p.name].strange_loops],
    ids=lambda p: p.name,
)
def test_without_strange_loops_the_guarantee_is_finite_omega_or_never(hp, presentation):
    """Corollary 5.3, which `CitedValues` enforces on the records, holds in the package."""
    universe = _universe(hp, presentation)
    assert not hp.strange_loops(universe)
    guarantee = hp.hyperprobability(universe, presentation.event, presentation.start)
    assert guarantee is hp.INFINITY or guarantee.is_finite or guarantee == OMEGA


def test_the_first_limit_jump_of_the_loop_comes_through_its_strange_loop(hp):
    """Theorem 5.2 on LOOP: all of the mass that arrives at ω arrives through {a, b}."""
    law = hp.TransfiniteLaw(_universe(hp, LOOP), LOOP.event, LOOP.start)
    jumps = {(a.level, a.states): mass for a, mass in law.loops_into(OMEGA).items()}
    assert jumps == {(0, ("a", "b")): Fraction(1)}
    assert law.exactly(OMEGA) == 1


def test_hyperprobability_refuses_a_limit_key_that_is_not_an_attractor(hp):
    """The one coherence check `Presentation` leaves to the package it cites."""
    presentation = Presentation.deterministic(
        "not an attractor", {"a": "b", "b": "a"}, event="a", start="a",
        limits=({("a",): "b"},),
    )
    with pytest.raises(ValueError, match="which is not a level-0 attractor"):
        _universe(hp, presentation)


# --- the spring candidate ---------------------------------------------------


def test_the_spring_candidate_quotes_the_law_it_cites(hyperphysics):
    law = hyperphysics.LAWS_BY_NAME[SERIES_SPRING.source_law]
    assert SERIES_SPRING.source_form == law.form
    assert "d2Q/dt2" in law.form


def test_the_unadopted_spring_would_inherit_every_series_failure_mode(hyperphysics):
    """What adopting the candidate would take on, listed by the source.

    The candidate is not adopted. This checks only that hyperphysics accepts
    its shape as a transport, and that the transport would inherit the failure
    modes of series-rlc and of every law it is built from.
    """
    law = hyperphysics.LAWS_BY_NAME[SERIES_SPRING.source_law]
    transport = hyperphysics.Transport(
        law=SERIES_SPRING.source_law,
        target_field="metamathethicology.oreality",
        target_form=SERIES_SPRING.target_form,
        transports=SERIES_SPRING.transports,
        does_not_transport=SERIES_SPRING.does_not_transport,
        warrant=hyperphysics.Warrant.BORROWED_FORM,
    )
    assert hyperphysics.validate(transport) is transport
    inherited = set(hyperphysics.inherited_failure_modes(transport))
    constituents = {
        mode for constituent in hyperphysics.SERIES_RLC_CONSTITUENTS
        for mode in constituent.fails_when
    }
    assert inherited >= set(law.fails_when) | constituents
    assert len(inherited) > len(law.fails_when)
