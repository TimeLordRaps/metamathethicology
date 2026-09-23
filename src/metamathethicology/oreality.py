"""Oreality: the combination field where hyperprobability meets the declared realities.

USER-DECLARED (Tyler Roost, 2026-09-23), preserved as stated. "This" is
`hyperprobability`, the package it was said about:

    And also then this allows for us in metamathethicology through ordinatics
    to define the Oreality, we already should have Areality (Abstraction reality
    where abstract thoughts exist), Oreality springs out from Areality (might
    actually use spring like hyperphysical equations), then also Preality
    (Possibility reality) [holds 5+dimensional objects like the block
    multiverse]. Our reality is the 4D projection of possibility reality
    through our coherent projections of Areality hyperprobabilistically through
    Oreality.

The declaration places the field here and supplies its two halves. The
mathematical half is stated in `hyperprobability`: contained universes, the law
at every ordinal stage, strange loops, hyperprobability and the Kac bridge, each
stated once in its SPEC under a claim label. The realm half is not stated
anywhere in committed form, so the declaration itself is the referent. Every
realm below quotes it verbatim, and `Realm` refuses a fragment the declaration
does not contain.

THE DEFINITION
--------------
Read through hyperprobability, under an adopted licence:

- Areality itself is not read. Its coherent projections are: a coherent
  projection is a contained presentation (`Presentation`), and its coherence is
  checked when it is built.
- Preality is what is possible: the support graphs of a presentation, and the
  transfinite runs they allow.
- Oreality is the ordinal-staged law. From a coherent projection the level
  recursion builds the law μK_α at every stage α < ω^ω, and with it the least
  stage that guarantees an event, its hyperprobability ℍ. Oreality springs out
  from Areality in that sense: every stage law is generated from a presentation.
- Our reality is the in-universe law: ordinary probability, which is the law at
  ω once every attractor collapses.

WHAT IS AND IS NOT CLAIMED
--------------------------
The readings are READINGS. hyperprobability's SPEC defines no realm and labels
its own readings of Tyler's phrases INTERPRETATION, so nothing there establishes
that its structure is what any realm is. The readings are therefore
LICENCE-DEPENDENT, and the module shows that rather than asserting it:
`oreality_space(include_licence=False)` removes the licence and every realm
reading leaves the closure.

Four things are held back on purpose. The O's expansion is PROPOSED, not
declared (`O_IS_ORDINAL`). The dimension counts are preserved and not read
(`DIMENSIONS_DO_NOT_TRANSPORT`). The spring is OPEN (`SPRING_LAW_IS_OPEN`): a
hyperphysical candidate is recorded and not adopted. And "our reality" is read
as a law, not as one realized run (`OUR_REALITY_READINGS_CONSIDERED`).

Two claims the declaration might seem to license are refuted by countermodel.
Our reality does not fix Oreality (`our_reality_does_not_fix_oreality`), and
possibility does not fix our reality (`possibility_does_not_fix_our_reality`).
Between them they show that each "through" in the declaration carries
information. The coherent projection carries weight that possibility lacks, and
Oreality carries strange loops that our reality cannot see.

Results are CITED, not restated. Each reading names the SPEC results it rests on
by number and quotes them, and every value recorded from hyperprobability is
held beside the presentation it was computed from. Neither hyperprobability nor
hyperphysics is imported at runtime. `tests/test_oreality_citations.py`
cross-checks every quote, heading, code name and recorded value whenever they
are importable.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction

from ordinatics.ordinals import OMEGA, ONE, Ordinal

from .spaces import Assumption, Domain, Judgment, OperationSpace, Rule

# ---------------------------------------------------------------------------
# The declaration and the two cited surfaces.
# ---------------------------------------------------------------------------

#: USER-DECLARED (Tyler Roost, 2026-09-23), verbatim. Every realm below quotes a
#: fragment of it, and `Realm` rejects a fragment that is not in it.
DECLARATION = (
    "And also then this allows for us in metamathethicology through ordinatics to "
    "define the Oreality, we already should have Areality (Abstraction reality where "
    "abstract thoughts exist), Oreality springs out from Areality (might actually use "
    "spring like hyperphysical equations), then also Preality (Possibility reality) "
    "[holds 5+dimensional objects like the block multiverse]. Our reality is the 4D "
    "projection of possibility reality through our coherent projections of Areality "
    "hyperprobabilistically through Oreality."
)

#: The field whose structure the realms are read through. Cited, never restated.
PROBABILITY_FIELD = "hyperprobability"

#: The field a spring law would be borrowed from, if one is ever adopted.
SPRING_FIELD = "hyperphysics"

#: PROPOSED, not declared. The declaration defines Oreality "through ordinatics"
#: and routes our reality "hyperprobabilistically through Oreality", and both
#: suggest the O is for Ordinal. Tyler has not said so. Every reading below holds
#: whatever the O stands for, and the tests check that no judgment in the space
#: mentions the expansion.
O_IS_ORDINAL = (
    "PROPOSED: the O in Oreality read as Ordinal. Not declared, and no reading "
    "here depends on it."
)

#: The declared counts have nothing to attach to. Stated once so that each realm
#: can decline them against a fixed referent.
DIMENSIONS_DO_NOT_TRANSPORT = (
    "hyperprobability has no dimensions. A universe there is a finite set of "
    "states with exact rational laws, and nothing in it is a spatial or temporal "
    "axis. The declared counts, a 4D projection and 5+dimensional objects, are "
    "preserved as stated and read by nothing here."
)

#: The claim labels of hyperprobability's SPEC, section 0.2.
SPEC_LABELS: tuple[str, ...] = (
    "DEFINITION", "PROVED", "KNOWN", "CHECKED", "INTERPRETATION", "TRANSPORT",
    "CONJECTURE", "OPEN",
)

#: The kinds of numbered result the SPEC states.
RESULT_KINDS: tuple[str, ...] = (
    "Definition", "Lemma", "Proposition", "Theorem", "Corollary", "Remark",
)


def _nonempty(value: object, label: str) -> None:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")


@dataclass(frozen=True, slots=True)
class Citation:
    """One result of hyperprobability's SPEC, cited by number, never restated.

    `status` is the claim label the SPEC gives the result, so a reader can tell a
    stipulation from a theorem from a reading without another lookup. `quotes`
    are exact sentences of the result and `code` names what implements it. Both
    are conveniences, and `tests/test_oreality_citations.py` holds them to the
    SPEC and the package character for character.
    """

    kind: str
    number: str
    title: str | None
    status: str
    quotes: tuple[str, ...]
    code: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.kind not in RESULT_KINDS:
            raise ValueError(f"{self.kind!r} is not a kind of result the SPEC states")
        _nonempty(self.number, "citation number")
        if self.title is not None:
            _nonempty(self.title, "citation title")
        _nonempty(self.status, "citation status")
        labels = set(re.findall(r"\b[A-Z]{2,}\b", self.status))
        if not labels or not labels <= set(SPEC_LABELS):
            raise ValueError(f"{self.status!r} is not a SPEC label; the SPEC uses {SPEC_LABELS}")
        if type(self.quotes) is not tuple or not self.quotes:
            raise ValueError("a citation quotes at least one sentence of its result")
        for quote in self.quotes:
            _nonempty(quote, "quote")
        if type(self.code) is not tuple:
            raise TypeError("citation code names must be a tuple")
        for name in self.code:
            _nonempty(name, "code name")

    @property
    def label(self) -> str:
        return f"{self.kind} {self.number}"

    def heading(self) -> str:
        """The result's heading as the SPEC prints it, so it can be found by search."""
        title = f" ({self.title})" if self.title else ""
        return f"**{self.label}{title}.** {self.status}."


CITATIONS: tuple[Citation, ...] = (
    Citation(
        "Definition", "1.1", "universe", "DEFINITION",
        ("A universe U = (S, K_0, L_1, …, L_d) has:",),
        ("Universe", "Universe.deterministic"),
    ),
    Citation(
        "Definition", "1.2", "levels", "DEFINITION",
        ("K_{k+1}(q, ·) = Σ_{A∈𝒜_k} h_k(q, A)·e_A.",),
        ("Universe.kernel", "Universe.attractors"),
    ),
    Citation(
        "Remark", "1.3", "contained, causal, representable", "INTERPRETATION",
        ("Containment is the constraint.",),
        ("Universe", "exact"),
    ),
    Citation(
        "Definition", "2.1", "law at a stage", "DEFINITION",
        ("The law at stage α of the run from μ is μK_α.",),
        ("Universe.law",),
    ),
    Citation(
        "Definition", "2.6", "in-universe law", "DEFINITION",
        ("in_uni(μ) = Σ_{A∈𝒜_0} (Σ_q μ(q)·h_0(q, A))·π_A.",),
        ("Universe.in_uni", "frequency"),
    ),
    Citation(
        "Proposition", "2.7", None, "KNOWN (a, b); PROVED (c, d)",
        (
            "If L_1 collapses every attractor, the law at ω is in_uni(μ).",
            "Strange loops do not change in_uni, which depends only on K_0.",
        ),
        ("Universe.law", "Universe.in_uni"),
    ),
    Citation(
        "Remark", "2.8", "pathwise runs", "PROVED (sketch)",
        (
            "A random run (X_α)_{α<ω^ω} is built along the countable well-order ω^ω",
            "transfinite induction gives a process whose law at α is μK_α.",
            "A collapsing attractor sends its tail to π_A, forgetting where in A the "
            "tail was.",
        ),
    ),
    Citation(
        "Definition", "3.2", "strange loop", "DEFINITION",
        ("the limit of a run that settles in A does not resolve to A's in-universe law",),
        ("strange_loops", "Attractor.collapses"),
    ),
    Citation(
        "Definition", "4.1", None, "DEFINITION",
        ("ℍ_μ(E) = min{α < ω^ω : F_μ(α) = 1}",),
        ("hyperprobability", "TransfiniteLaw"),
    ),
    Citation(
        "Proposition", "4.9", "possibility dynamics", "PROVED",
        (
            "ℍ_q(E) depends only on E and on the support graphs of K_0, …, K_d.",
            "Reweighting rows and targets without changing their supports changes no "
            "hyperprobability.",
        ),
        ("hyperprobability",),
    ),
    Citation(
        "Theorem", "5.2", "limit jumps come from strange loops", "PROVED",
        (
            "So the law of τ_E can jump at a limit stage only through strange loops "
            "whose exits reach E.",
        ),
        ("TransfiniteLaw.loops_into",),
    ),
    Citation(
        "Corollary", "5.3", "no strange loops", "PROVED",
        (
            "If no attractor at any level is a strange loop, then F_μ is constant on "
            "[ω, ω^ω) and ℍ_μ(E) ∈ ℕ ∪ {ω, ∞}.",
        ),
        ("strange_loops",),
    ),
    Citation(
        "Remark", "5.4", "the collapse", "INTERPRETATION",
        (
            "A collapsing attractor resolves to its in-universe law π_A. This is where "
            "the transfinite reduces to ordinary probability.",
            "So hyperprobability is where transfinite probability finishes collapsing.",
        ),
    ),
    Citation(
        "Theorem", "6.2", "the Kac bridge", "PROVED",
        (
            "π_A(E) ≥ 1/ι(ℍ⁺_A(E)).",
            "Equality holds exactly when ℍ⁺_A(E) = N is finite and every return from "
            "A ∩ E to E takes exactly N steps.",
        ),
        ("kac", "KacBound.holds", "KacBound.tight"),
    ),
)

CITATIONS_BY_LABEL: dict[str, Citation] = {c.label: c for c in CITATIONS}


# ---------------------------------------------------------------------------
# Coherent projections: contained presentations.
# ---------------------------------------------------------------------------

#: A row of the step kernel: each possible successor with its exact weight.
Row = tuple[tuple[str, Fraction], ...]

#: A limit rule: each attractor it redirects, as its sorted states, and the state
#: it sends that attractor to at the limit.
LimitRule = tuple[tuple[tuple[str, ...], str], ...]


def _incoherent(name: object, reason: str) -> ValueError:
    return ValueError(f"{name!r} is not a coherent projection: {reason}")


def _exact(name: str, value: object, where: str) -> Fraction:
    if type(value) is int or type(value) is Fraction:
        return Fraction(value)
    raise _incoherent(name, f"{where} has weight {value!r}, which is not an exact rational")


@dataclass(frozen=True, slots=True)
class Presentation:
    """A contained universe, as a coherent projection of Areality presents it.

    This is the reading of "our coherent projections of Areality". A projection
    is coherent when it presents a universe hyperprobability can contain
    (Definition 1.1, Remark 1.3): finitely many named states, a step kernel whose
    rows are exact positive rationals summing to one over the states, and limit
    rules whose targets are states. Incoherent projections cannot be built.

    `limits[k - 1]` is the level-k limit rule. Its targets are point states only;
    a law as a target, which hyperprobability also allows, is not needed by any
    witness here. Whether each rule's keys are attractors of their level is
    hyperprobability's check, not this one: its `Universe` raises on a key that
    is not, and `tests/test_oreality_citations.py` builds every witness there.

    `of` and `deterministic` store the kernel in sorted order and drop zero
    weights, so two presentations of the same universe compare equal.
    """

    name: str
    kernel: tuple[tuple[str, Row], ...]
    event: str
    start: str
    limits: tuple[LimitRule, ...] = ()

    def __post_init__(self) -> None:
        _nonempty(self.name, "presentation name")
        if type(self.kernel) is not tuple or type(self.limits) is not tuple:
            raise TypeError("kernel and limits must be tuples; use Presentation.of")
        if not self.kernel:
            raise _incoherent(self.name, "it has no states")
        states: list[str] = []
        for entry in self.kernel:
            if type(entry) is not tuple or len(entry) != 2:
                raise TypeError("a kernel entry is a (state, row) pair")
            state = entry[0]
            if type(state) is not str or not state.strip():
                raise _incoherent(self.name, f"state {state!r} is not a nonempty string")
            if state in states:
                raise _incoherent(self.name, f"state {state!r} is listed twice")
            states.append(state)
        for state, row in self.kernel:
            self._check_row(states, state, row)
        if self.event not in states:
            raise _incoherent(self.name, f"the event {self.event!r} is not a state")
        if self.start not in states:
            raise _incoherent(self.name, f"the start {self.start!r} is not a state")
        for level, rule in enumerate(self.limits, 1):
            self._check_limit_rule(states, level, rule)

    def _check_row(self, states: list[str], state: str, row: object) -> None:
        if type(row) is not tuple or not row:
            raise _incoherent(self.name, f"the row of {state!r} is empty")
        successors: list[str] = []
        for pair in row:
            if type(pair) is not tuple or len(pair) != 2:
                raise TypeError("a row entry is a (successor, weight) pair")
            successor, weight = pair
            if successor not in states:
                raise _incoherent(
                    self.name, f"the row of {state!r} steps to {successor!r}, not a state",
                )
            if successor in successors:
                raise _incoherent(self.name, f"the row of {state!r} names {successor!r} twice")
            if type(weight) is not Fraction or weight <= 0:
                raise _incoherent(
                    self.name,
                    f"the row of {state!r} gives {successor!r} the weight {weight!r}, "
                    "which is not a positive exact rational",
                )
            successors.append(successor)
        total = sum((weight for _, weight in row), Fraction(0))
        if total != 1:
            raise _incoherent(self.name, f"the row of {state!r} sums to {total}, not 1")

    def _check_limit_rule(self, states: list[str], level: int, rule: object) -> None:
        if type(rule) is not tuple:
            raise TypeError(f"limit rule {level} must be a tuple of (members, target) pairs")
        keys: list[tuple[str, ...]] = []
        for pair in rule:
            if type(pair) is not tuple or len(pair) != 2:
                raise TypeError("a limit rule entry is a (members, target) pair")
            members, target = pair
            if (
                type(members) is not tuple or not members
                or any(member not in states for member in members)
                or len(set(members)) != len(members)
            ):
                raise _incoherent(
                    self.name, f"limit rule {level} keys {members!r}, not a set of states",
                )
            if target not in states:
                raise _incoherent(
                    self.name, f"limit rule {level} sends {members!r} to {target!r}, "
                               "not a state",
                )
            if members in keys:
                raise _incoherent(self.name, f"limit rule {level} names {members!r} twice")
            keys.append(members)

    @classmethod
    def of(
        cls,
        name: str,
        kernel: Mapping[str, Mapping[str, object]],
        *,
        event: str,
        start: str,
        limits: Sequence[Mapping[Sequence[str], str]] = (),
    ) -> Presentation:
        """Present a universe from a kernel of exact weights and point-target limit rules."""
        if not isinstance(kernel, Mapping):
            raise TypeError("kernel must map each state to its row of successor weights")
        if not isinstance(limits, (list, tuple)):
            raise TypeError("limits must be a sequence of limit rules, one per level")
        if any(type(state) is not str for state in kernel):
            raise _incoherent(name, "states are named by strings")
        rows: list[tuple[str, Row]] = []
        for state in sorted(kernel):
            row = kernel[state]
            if not isinstance(row, Mapping) or any(type(s) is not str for s in row):
                raise _incoherent(name, f"the row of {state!r} does not map states to weights")
            weights = sorted(
                (successor, _exact(name, weight, f"{state!r} -> {successor!r}"))
                for successor, weight in row.items()
            )
            rows.append((state, tuple((s, w) for s, w in weights if w != 0)))
        rules: list[LimitRule] = []
        for rule in limits:
            if not isinstance(rule, Mapping):
                raise TypeError("each limit rule maps attractors to target states")
            entries = []
            for members, target in rule.items():
                if isinstance(members, str) or any(type(m) is not str for m in members):
                    raise _incoherent(name, f"limit key {members!r} is not a set of states")
                entries.append((tuple(sorted(members)), target))
            rules.append(tuple(sorted(entries, key=lambda entry: entry[0])))
        return cls(name, tuple(rows), event, start, tuple(rules))

    @classmethod
    def deterministic(
        cls,
        name: str,
        step: Mapping[str, str],
        *,
        event: str,
        start: str,
        limits: Sequence[Mapping[Sequence[str], str]] = (),
    ) -> Presentation:
        """Present the universe in which each state moves to `step[state]` with certainty."""
        if not isinstance(step, Mapping):
            raise TypeError("step must map each state to its successor")
        return cls.of(
            name, {state: {successor: 1} for state, successor in step.items()},
            event=event, start=start, limits=limits,
        )

    def states(self) -> tuple[str, ...]:
        return tuple(state for state, _ in self.kernel)

    def possibility(self) -> tuple[frozenset[tuple[str, str]], tuple[frozenset, ...]]:
        """What Preality holds of this presentation: which steps and limits are possible.

        The support graph of the step kernel, and each level's limit rule. With
        point targets these fix the support graph of every level, and
        Proposition 4.9 proves that, given the event, hyperprobability depends on
        nothing else.
        """
        edges = frozenset(
            (state, successor) for state, row in self.kernel for successor, _ in row
        )
        return edges, tuple(frozenset(rule) for rule in self.limits)

    def weights(self) -> dict[tuple[str, str], Fraction]:
        """The exact step weights: what a coherent projection adds to possibility."""
        return {
            (state, successor): weight
            for state, row in self.kernel for successor, weight in row
        }

    def collapsed(self) -> Presentation:
        """The same kernel with no limit rules, so that every attractor collapses."""
        return Presentation(f"{self.name}, collapsed", self.kernel, self.event, self.start)

    def universe_arguments(self) -> tuple[dict[str, dict[str, Fraction]], list[dict]]:
        """The arguments `hyperprobability.Universe(kernel, limits)` takes for this.

        Built here and used only by the citation tests, since this module does
        not import hyperprobability. Limit keys are frozensets of states, as
        hyperprobability's limit rules require.
        """
        kernel = {state: dict(row) for state, row in self.kernel}
        limits = [
            {frozenset(members): target for members, target in rule} for rule in self.limits
        ]
        return kernel, limits


# ---------------------------------------------------------------------------
# Witnesses, and what hyperprobability computes for them.
# ---------------------------------------------------------------------------

#: A two-state cycle whose level-0 attractor {a, b} is a strange loop: at the
#: first limit stage it exits to `out` instead of resolving to its own law.
LOOP = Presentation.deterministic(
    "loop", {"a": "b", "b": "a", "out": "out"}, event="out", start="a",
    limits=({("a", "b"): "out"},),
)

#: The same loop exiting to a three-step path into `out`.
CHAIN = Presentation.deterministic(
    "chain", {"a": "b", "b": "a", "x1": "x2", "x2": "x3", "x3": "out", "out": "out"},
    event="out", start="a", limits=({("a", "b"): "x1"},),
)

#: Two fixed points that swap at every ω and exit together at ω^2: strange loops
#: at levels 0 and 1.
SWAP = Presentation.deterministic(
    "swap", {"a": "a", "b": "b", "out": "out"}, event="out", start="a",
    limits=({("a",): "b", ("b",): "a"}, {("a", "b"): "out"}),
)

FAIR_COIN = Presentation.of(
    "fair coin",
    {"H": {"H": Fraction(1, 2), "T": Fraction(1, 2)},
     "T": {"H": Fraction(1, 2), "T": Fraction(1, 2)}},
    event="H", start="T",
)

#: The fair coin's transitions with different weights: the same possibility.
BIASED_COIN = Presentation.of(
    "biased coin",
    {"H": {"H": Fraction(1, 3), "T": Fraction(2, 3)},
     "T": {"H": Fraction(1, 3), "T": Fraction(2, 3)}},
    event="H", start="T",
)

#: A deterministic two-cycle with no limit rules, so it collapses.
CLOCK = Presentation.deterministic(
    "clock", {"tick": "tock", "tock": "tick"}, event="tock", start="tick",
)

PRESENTATIONS: tuple[Presentation, ...] = (
    LOOP, LOOP.collapsed(), CHAIN, SWAP, FAIR_COIN, BIASED_COIN, CLOCK,
)


@dataclass(frozen=True, slots=True)
class CitedValues:
    """What hyperprobability computes for one presentation, recorded and cited.

    Recorded rather than computed because this module does not import
    hyperprobability; `tests/test_oreality_citations.py` recomputes every field
    whenever it can. Each field reads one realm:

    - `in_universe` is our reality: `Universe.in_uni` from the start, nonzero
      entries only (Definition 2.6).
    - `frequency` is the in-universe frequency of the event (Definition 2.6).
    - `hyperprobability` is Oreality's guarantee ℍ of the event from the start
      (Definition 4.1), with None standing for ∞.
    - `strange_loops` lists each strange loop as its level and states
      (Definition 3.2).

    Construction checks the record against two results that hold for every
    presentation, so some transcription errors cannot be built: the frequency is
    the in-universe law's mass on the event (Definition 2.6), and without strange
    loops ℍ lies in ℕ ∪ {ω, ∞} (Corollary 5.3).
    """

    presentation: Presentation
    in_universe: tuple[tuple[str, Fraction], ...]
    frequency: Fraction
    hyperprobability: Ordinal | None
    strange_loops: tuple[tuple[int, tuple[str, ...]], ...] = ()

    def __post_init__(self) -> None:
        if type(self.presentation) is not Presentation:
            raise TypeError("cited values belong to a Presentation")
        name = self.presentation.name
        states = set(self.presentation.states())
        if type(self.in_universe) is not tuple:
            raise TypeError("the in-universe law must be a tuple of (state, weight) pairs")
        law = dict(self.in_universe)
        if (
            len(law) != len(self.in_universe)
            or not set(law) <= states
            or any(type(p) is not Fraction or p <= 0 for p in law.values())
            or sum(law.values(), Fraction(0)) != 1
        ):
            raise ValueError(f"the in-universe law of {name!r} must be a positive exact law")
        if type(self.frequency) is not Fraction:
            raise TypeError("frequency must be an exact Fraction")
        if self.frequency != law.get(self.presentation.event, Fraction(0)):
            raise ValueError(
                "frequency must be the in-universe law's mass on the event (Definition 2.6)"
            )
        if self.hyperprobability is not None and type(self.hyperprobability) is not Ordinal:
            raise TypeError("hyperprobability must be an exact Ordinal, or None for ∞")
        if type(self.strange_loops) is not tuple:
            raise TypeError("strange loops must be a tuple of (level, states) pairs")
        for level, members in self.strange_loops:
            if type(level) is not int or level < 0 or not set(members) <= states:
                raise ValueError(f"{(level, members)!r} is not a strange loop of {name!r}")
        guarantee = self.hyperprobability
        if not self.strange_loops and guarantee is not None and not (
            guarantee.is_finite or guarantee == OMEGA
        ):
            raise ValueError("with no strange loops, ℍ lies in ℕ ∪ {ω, ∞} (Corollary 5.3)")


_HALF = Fraction(1, 2)

CITED_VALUES: dict[str, CitedValues] = {
    values.presentation.name: values
    for values in (
        CitedValues(LOOP, (("a", _HALF), ("b", _HALF)), Fraction(0), OMEGA,
                    ((0, ("a", "b")),)),
        CitedValues(LOOP.collapsed(), (("a", _HALF), ("b", _HALF)), Fraction(0), None),
        CitedValues(CHAIN, (("a", _HALF), ("b", _HALF)), Fraction(0), OMEGA + ONE + ONE + ONE,
                    ((0, ("a", "b")),)),
        CitedValues(SWAP, (("a", Fraction(1)),), Fraction(0), OMEGA * OMEGA,
                    ((0, ("a",)), (0, ("b",)), (1, ("a", "b")))),
        CitedValues(FAIR_COIN, (("H", _HALF), ("T", _HALF)), _HALF, OMEGA),
        CitedValues(BIASED_COIN, (("H", Fraction(1, 3)), ("T", Fraction(2, 3))),
                    Fraction(1, 3), OMEGA),
        CitedValues(CLOCK, (("tick", _HALF), ("tock", _HALF)), _HALF, ONE),
    )
}


@dataclass(frozen=True, slots=True)
class CitedKacBound:
    """One instance of Theorem 6.2, the Kac bridge, as hyperprobability computes it.

    `frequency` is π_A(E), the in-universe frequency of the event inside the
    attractor, and `return_guarantee` is ℍ⁺_A(E), the longest guaranteed return
    to it. The theorem says π_A(E) ≥ 1/ι(ℍ⁺_A(E)), with equality exactly when the
    return guarantee is a finite N and every return takes exactly N steps.

    The bound is PROVED, so a record that violates it is a transcription error
    and cannot be built. Nor can a record whose `tight` flag disagrees with the
    arithmetic: for a finite guarantee N the bound is 1/N, and for an infinite
    one it is a positive infinitesimal, below every positive rational.
    """

    presentation: Presentation
    attractor: tuple[str, ...]
    frequency: Fraction
    return_guarantee: Ordinal
    tight: bool

    def __post_init__(self) -> None:
        if type(self.presentation) is not Presentation:
            raise TypeError("a Kac record belongs to a Presentation")
        if (
            type(self.attractor) is not tuple
            or not set(self.attractor) <= set(self.presentation.states())
            or self.presentation.event not in self.attractor
        ):
            raise ValueError("the attractor must be states of the presentation meeting its event")
        if type(self.frequency) is not Fraction or type(self.return_guarantee) is not Ordinal:
            raise TypeError("a Kac record holds an exact Fraction and an exact Ordinal")
        if self.return_guarantee < ONE:
            raise ValueError("a return takes at least one step")
        if type(self.tight) is not bool:
            raise TypeError("tight must be a bool")
        if not self.holds():
            raise ValueError(
                "a frequency below 1/ι(ℍ⁺_A(E)) contradicts Theorem 6.2, which is PROVED"
            )
        if self.tight != self.is_tight():
            raise ValueError("tight must mean equality with 1/ι(ℍ⁺_A(E)) (Theorem 6.2)")

    def bound(self) -> Fraction | None:
        """1/ι(ℍ⁺_A(E)) when it is rational; None when it is a positive infinitesimal."""
        if self.return_guarantee.is_finite:
            return Fraction(1, self.return_guarantee.to_int())
        return None

    def holds(self) -> bool:
        bound = self.bound()
        return self.frequency > 0 if bound is None else self.frequency >= bound

    def is_tight(self) -> bool:
        bound = self.bound()
        return bound is not None and self.frequency == bound


KAC_WITNESSES: tuple[CitedKacBound, ...] = (
    CitedKacBound(FAIR_COIN, ("H", "T"), _HALF, OMEGA, tight=False),
    CitedKacBound(BIASED_COIN, ("H", "T"), Fraction(1, 3), OMEGA, tight=False),
    CitedKacBound(CLOCK, ("tick", "tock"), _HALF, ONE + ONE, tight=True),
)


# ---------------------------------------------------------------------------
# What each realm fixes, and what it does not.
# ---------------------------------------------------------------------------


def our_reality_does_not_fix_oreality() -> tuple[CitedValues, CitedValues]:
    """Refute: that our reality determines Oreality.

    The declaration routes our reality through Oreality. It is tempting to read
    that backwards, as if Oreality could be recovered from what our reality
    shows. It cannot.

    LOOP and its collapse share one kernel, so they share our reality: from a,
    the in-universe law is 1/2 on a and 1/2 on b, and `out` has frequency 0 in
    both. Their Oreality differs. In LOOP the strange loop on {a, b} exits to
    `out` at the first limit stage, so ℍ(out) = ω. In the collapse nothing ever
    reaches `out`, so ℍ(out) = ∞. Proposition 2.7 says why: strange loops do not
    change in_uni, which depends only on K_0.

    One countermodel settles a universal claim, so this refutation is
    conclusive: our reality is blind to strange loops, and Oreality carries
    information our reality does not. CHAIN is a second witness, with the same
    our reality and ℍ(out) = ω + 3.
    """
    loop, collapsed = CITED_VALUES[LOOP.name], CITED_VALUES[LOOP.collapsed().name]
    if loop.presentation.weights() != collapsed.presentation.weights():
        raise AssertionError("the witnesses must share a kernel")
    if loop.in_universe != collapsed.in_universe or loop.frequency != collapsed.frequency:
        raise AssertionError("the witnesses must share our reality")
    if loop.hyperprobability == collapsed.hyperprobability:
        raise AssertionError("the witnesses must differ in Oreality")
    return loop, collapsed


def possibility_does_not_fix_our_reality() -> tuple[CitedValues, CitedValues]:
    """Refute: that Preality, or Oreality's guarantees, determine our reality.

    The declaration makes our reality a projection of possibility reality
    THROUGH our coherent projections of Areality. The middle term is
    load-bearing, and these witnesses show it.

    The fair and biased coins allow exactly the same transitions, so they share
    their possibility, and by Proposition 4.9 every hyperprobability: from T,
    ℍ(H) = ω in both. Their our reality differs. H has in-universe frequency
    1/2 under the fair coin and 1/3 under the biased one. What separates them is
    weight, and weight is what a coherent projection adds to possibility.

    One countermodel settles a universal claim, so this refutation is
    conclusive: our reality is a function neither of Preality nor of ℍ.
    """
    fair, biased = CITED_VALUES[FAIR_COIN.name], CITED_VALUES[BIASED_COIN.name]
    if fair.presentation.possibility() != biased.presentation.possibility():
        raise AssertionError("the witnesses must share their possibility")
    if fair.hyperprobability != biased.hyperprobability:
        raise AssertionError("the witnesses must share their hyperprobability")
    if fair.in_universe == biased.in_universe or fair.frequency == biased.frequency:
        raise AssertionError("the witnesses must differ in our reality")
    return fair, biased


def oreality_bounds_our_reality() -> tuple[CitedKacBound, ...]:
    """Exhibit the sense in which our reality is reached hyperprobabilistically.

    Theorem 6.2, the Kac bridge, is PROVED in hyperprobability: inside an
    attractor A that meets an event E, π_A(E) ≥ 1/ι(ℍ⁺_A(E)). Oreality bounds our
    reality from below. The witnesses do not establish the bound, which the
    theorem does, but they exhibit its two cases.

    The clock returns to `tock` in exactly two steps every time, so ℍ⁺ = 2 and
    the bound is tight: the frequency is exactly 1/2. The coins return to H with
    certainty but within no bounded number of steps, so ℍ⁺ = ω and the bound is
    the positive infinitesimal 1/ω. It holds strictly, and equally for the
    frequencies 1/2 and 1/3: Oreality bounds our reality without fixing it.
    """
    fair, biased, clock = KAC_WITNESSES
    if fair.return_guarantee != biased.return_guarantee or fair.frequency == biased.frequency:
        raise AssertionError("the coins must share a return guarantee and differ in frequency")
    if not clock.tight or fair.tight or biased.tight:
        raise AssertionError("the clock must be tight and the coins must not")
    return KAC_WITNESSES


# ---------------------------------------------------------------------------
# The realms, as declared and as read.
# ---------------------------------------------------------------------------

#: The realms the declaration names, in the order their readings become
#: available. Reality kinds Tyler has named elsewhere are absent because this
#: declaration does not name them.
REALM_NAMES: tuple[str, ...] = ("Areality", "Preality", "Oreality", "our reality")

#: Two readings of "our reality" were live, and the record is kept because a
#: choice is only informative against what it passed over.
OUR_REALITY_READINGS_CONSIDERED: tuple[str, ...] = (
    "(a) one realized run: our reality is a single history drawn from Preality "
    "-- NOT ADOPTED, because hyperprobability is a theory of laws and nothing "
    "in it selects which run occurs",
    "(b) the in-universe law: what ordinary probability sees from inside a "
    "presentation, the law at ω once every attractor collapses -- ADOPTED, "
    "because the declaration calls our reality a projection and in_uni is one "
    "in two exact senses",
)


@dataclass(frozen=True, slots=True)
class Realm:
    """One declared realm, quoted from the declaration and read through hyperprobability.

    `declared` must occur verbatim in `DECLARATION`: the realm half of this field
    has no other statement, so a paraphrase would leave it with no referent at
    all. `cites` names the SPEC results the reading rests on, and must name
    cited results. `arises_from` records the declared order, in which Oreality
    springs out from Areality and our reality passes through the other three.

    `does_not_transport` is not decoration. It is the part a reader needs in
    order not to inherit a commitment nobody established, and it is what `Rule`
    requires before a METAMATH result may conclude a METAPHYSICS reading.
    """

    name: str
    declared: str
    reads_as: str
    transports: str
    does_not_transport: str
    cites: tuple[str, ...]
    arises_from: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.name not in REALM_NAMES:
            raise ValueError(
                f"{self.name!r} is not a declared realm; the declaration names {REALM_NAMES}"
            )
        for value, label in (
            (self.declared, "declared text"), (self.reads_as, "reading"),
            (self.transports, "transports"), (self.does_not_transport, "does_not_transport"),
        ):
            _nonempty(value, f"realm {label}")
        if self.declared not in DECLARATION:
            raise ValueError(
                f"the declared text of {self.name} is not in the declaration; quote it, "
                "do not paraphrase it"
            )
        if type(self.cites) is not tuple or not self.cites:
            raise ValueError("a realm reading cites at least one result")
        unknown = [label for label in self.cites if label not in CITATIONS_BY_LABEL]
        if unknown:
            raise ValueError(f"{unknown} is not a cited result of {PROBABILITY_FIELD}")
        if (
            type(self.arises_from) is not tuple
            or any(name not in REALM_NAMES for name in self.arises_from)
            or self.name in self.arises_from
        ):
            raise ValueError(f"{self.name} can arise only from other declared realms")

    def citation(self) -> str:
        """Where to look the reading's results up, rather than trust this paraphrase."""
        return f"{PROBABILITY_FIELD}:" + ", ".join(self.cites)

    def bridge(self) -> str:
        """The bridge a METAMATH-to-METAPHYSICS `Rule` needs before it will read a realm."""
        return (
            f"Reading of {self.name} through {self.citation()} -- {self.reads_as}. "
            f"Transports: {self.transports}. "
            f"Does NOT transport: {self.does_not_transport}."
        )


AREALITY = Realm(
    name="Areality",
    declared="Areality (Abstraction reality where abstract thoughts exist)",
    reads_as="not Areality itself but its coherent projections, read as contained "
             "presentations: finitely many states, exact rational rows summing to one, "
             "and limit targets that are states",
    transports="that coherence is containment, which Remark 1.3 calls the constraint, "
               "so whether a projection is coherent is checked when it is built rather "
               "than assumed",
    does_not_transport="which abstract thoughts exist, what a thought is, whether "
                       "Areality also holds incoherent objects, and any claim that a "
                       "presentation is a thought",
    cites=("Definition 1.1", "Remark 1.3"),
)

PREALITY = Realm(
    name="Preality",
    declared="Preality (Possibility reality) [holds 5+dimensional objects like the "
             "block multiverse]",
    reads_as="which transitions are possible: the support graphs of K_0 through K_d, "
             "and the transfinite runs they allow, each run a block of every stage "
             "below ω^ω and the runs of one presentation its block multiverse",
    transports="that possibility is support and not weight: hyperprobability depends "
               "only on the support graphs (Proposition 4.9), so Preality fixes every "
               "guarantee of a presentation and not its in-universe law",
    does_not_transport="the count 5+ or any dimension, block-universe physics, "
                       "identification with any cosmology stated elsewhere, and any "
                       "weight or probability, which belong to presentations",
    cites=("Proposition 4.9", "Remark 2.8"),
)

OREALITY = Realm(
    name="Oreality",
    declared="Oreality springs out from Areality (might actually use spring like "
             "hyperphysical equations)",
    reads_as="the ordinal-staged law: the law μK_α at every stage α below ω^ω, and the "
             "guarantees ℍ it fixes, generated level by level from a coherent projection",
    transports="that Oreality springs out from Areality in that the level recursion "
               "builds every stage law from a presentation (Definitions 1.2 and 2.1); "
               "that at a limit stage it resolves an attractor to anything but that "
               "attractor's in-universe law only at a strange loop (Definition 3.2), "
               "the only way first arrival can jump at a limit (Theorem 5.2); and that "
               "without strange loops the chance of having met an event is constant "
               "from ω on (Corollary 5.3)",
    does_not_transport="what the O stands for, any spring law, time (a stage counts "
                       "evaluations, not seconds), which run is realized, and any claim "
                       "that a universe is a simulation",
    cites=("Definition 1.2", "Definition 2.1", "Definition 3.2", "Definition 4.1",
           "Theorem 5.2", "Corollary 5.3"),
    arises_from=("Areality",),
)

OUR_REALITY = Realm(
    name="our reality",
    declared="Our reality is the 4D projection of possibility reality through our "
             "coherent projections of Areality hyperprobabilistically through Oreality.",
    reads_as="the in-universe law in_uni: ordinary probability, the law at ω once "
             "every attractor collapses",
    transports="that our reality is a projection in two exact senses: it is the law at "
               "ω once every attractor collapses (Proposition 2.7), and a law at a stage "
               "is the one-stage marginal of whole runs (Remark 2.8), so it projects the "
               "runs Preality holds onto one stage; that it passes through Areality "
               "because its weights come from a coherent projection and not from "
               "possibility (Proposition 4.9); that it is reached hyperprobabilistically, "
               "since Oreality bounds it from below (Theorem 6.2) and a collapse is where "
               "the transfinite reduces to it (Remark 5.4); and that it is blind to "
               "strange loops (Proposition 2.7)",
    does_not_transport="the counts 4 and 5+, spacetime, any physics, identification "
                       "with any other named reality, and which run is ours",
    cites=("Definition 2.6", "Proposition 2.7", "Remark 2.8", "Proposition 4.9",
           "Remark 5.4", "Theorem 6.2"),
    arises_from=("Preality", "Areality", "Oreality"),
)

REALMS: tuple[Realm, ...] = (AREALITY, PREALITY, OREALITY, OUR_REALITY)

REALMS_BY_NAME: dict[str, Realm] = {realm.name: realm for realm in REALMS}


# ---------------------------------------------------------------------------
# The spring: OPEN.
# ---------------------------------------------------------------------------

#: USER-DECLARED, the fragment of the declaration that names the spring. The word
#: "might" is preserved because it is accurate. Nothing below upgrades it.
SPRING_DECLARATION = OREALITY.declared


@dataclass(frozen=True, slots=True)
class SpringCandidate:
    """A hyperphysical law the declared spring might borrow, recorded and not adopted.

    Written in the shape of a transport so that adopting it later would be a
    decision rather than a rediscovery. It is not a premise of any rule, and no
    reading depends on it. `not_adopted_because` says what would have to change.
    """

    name: str
    source_law: str
    source_form: str
    target_form: str
    transports: str
    does_not_transport: str
    not_adopted_because: tuple[str, ...]
    source_field: str = SPRING_FIELD

    def __post_init__(self) -> None:
        for value, label in (
            (self.name, "name"), (self.source_law, "source law"),
            (self.source_form, "source form"), (self.target_form, "target form"),
            (self.transports, "transports"), (self.does_not_transport, "does_not_transport"),
            (self.source_field, "source field"),
        ):
            _nonempty(value, f"spring candidate {label}")
        if type(self.not_adopted_because) is not tuple or not self.not_adopted_because:
            raise ValueError("an unadopted candidate says why it is not adopted")
        for reason in self.not_adopted_because:
            _nonempty(reason, "reason")

    def citation(self) -> str:
        """How to look the candidate law up, rather than trust this quotation."""
        return f"{self.source_field}:{self.source_law} -- {self.source_form}"


SERIES_SPRING = SpringCandidate(
    name="series-spring",
    source_law="series-rlc",
    source_form="L * d2Q/dt2 + R * dQ/dt + (1/C) * Q = V",
    target_form="the stage laws of an attractor swing about its rest law π_A; a "
                "collapse returns them to rest at the limit, and a strange loop "
                "releases them to its exit e_A",
    transports="a candidate only: that a periodic attractor's stage laws swing about "
               "the law a collapse returns them to, as a driven oscillator's charge "
               "swings about its equilibrium",
    does_not_transport="the henry, the ohm, the farad, the volt and the coulomb; any "
                       "physical mechanism; continuous time; and any assignment of L, "
                       "R, C or V to part of a universe",
    not_adopted_because=(
        "the declaration says 'might'",
        "series-rlc is second order in continuous time, while stage laws are first "
        "order and discrete: the law at α + 1 is the law at α times K_0",
        "nothing here determines which part of a universe L, R, C or V would be",
        "hyperphysics states no discrete-time law that a stage recursion could "
        "borrow instead",
    ),
)

SPRING_LAW_IS_OPEN = (
    "No spring law is adopted. The declaration says Oreality 'might' use spring "
    "like hyperphysical equations. The series-RLC candidate is recorded with its "
    "citation and its disclaimer; until it is adopted no rule in oreality_space "
    "takes a spring premise, and no reading depends on one."
)


# ---------------------------------------------------------------------------
# The readings as an operation space.
# ---------------------------------------------------------------------------

#: The adopted licence, written as a premise so that removing it is a
#: one-argument operation whose consequences are visible in the closure.
READING_LICENCE = "hyperprobability-structure-may-read-declared-realms"

#: Why the licence is a declaration and not a theorem.
LICENCE_IS_NOT_DERIVED = (
    "The reading licence is explicitly adopted, not derived. hyperprobability's "
    "SPEC defines no realm and labels its own readings of Tyler's phrases "
    "INTERPRETATION, so no result there establishes that its structure is what "
    "any realm is. Removing the licence with oreality_space(include_licence=False) "
    "removes every realm reading from the closure, which is the honest shape of "
    "that dependence."
)


def _cited_premise(citation: Citation, stage: Ordinal) -> Judgment:
    return Judgment(
        Domain.METAMATH, "cited-result",
        (f"{PROBABILITY_FIELD}:{citation.label}", citation.status), stage,
    )


def _declared_premise(realm: Realm, stage: Ordinal) -> Judgment:
    return Judgment(Domain.METAPHYSICS, "declared-realm", (realm.name, realm.declared), stage)


def oreality_space(*, include_licence: bool = True) -> OperationSpace:
    """The four readings, as a checkable operation space.

    Every rule concludes a METAPHYSICS reading from METAMATH results, so `Rule`
    requires each one to name its bridge, and each realm supplies that bridge
    from its own citation and disclaimer. A realm that disclaimed nothing could
    not be turned into a rule, and the space would not construct.

    A reading is available one stage after everything it reads through. Areality
    and Preality are read at ω+1, Oreality at ω+2 because it springs out from
    Areality, and our reality at ω+3 because it passes through all three. The
    stages order when readings become available. They do not rank the realms.

    The licence is a premise of every rule. With `include_licence=False` the
    closure derives nothing false. It derives no reading at all, because the
    cited results and the declaration alone never conclude one.
    """
    stage = OMEGA
    licence = Judgment(
        Domain.METAPHYSICS, "adopted-reading-licence", (READING_LICENCE,), stage,
    )
    assumptions: list[Assumption] = []
    for citation in CITATIONS:
        assumptions.append(Assumption(
            _cited_premise(citation, stage),
            f"cited from {PROBABILITY_FIELD}'s SPEC, where it is labelled "
            f"{citation.status}; quoted, not restated or re-proved here",
        ))
    for realm in REALMS:
        assumptions.append(Assumption(
            _declared_premise(realm, stage),
            "USER-DECLARED (Tyler Roost, 2026-09-23), quoted verbatim; the "
            "declaration is the only statement of this realm",
        ))
    if include_licence:
        assumptions.append(Assumption(licence, LICENCE_IS_NOT_DERIVED))

    readings: dict[str, Judgment] = {}
    rules: list[Rule] = []
    for realm in REALMS:
        earlier = tuple(readings[name] for name in realm.arises_from)
        at = max((reading.stage for reading in earlier), default=stage) + ONE
        readings[realm.name] = Judgment(
            Domain.METAPHYSICS, "realm-reading", (realm.name, realm.reads_as), at,
        )
        after = f", after the readings of {', '.join(realm.arises_from)}" if earlier else ""
        rules.append(Rule(
            name=f"read-{realm.name.lower().replace(' ', '-')}",
            premises=(
                *(_cited_premise(CITATIONS_BY_LABEL[label], stage) for label in realm.cites),
                _declared_premise(realm, stage), *earlier, licence,
            ),
            conclusion=readings[realm.name],
            justification=(
                f"{realm.name} is read through the structure {PROBABILITY_FIELD} states "
                f"in {', '.join(realm.cites)}{after}"
            ),
            bridge=realm.bridge(),
        ))

    closed_stage = max(reading.stage for reading in readings.values())
    return OperationSpace("oreality", closed_stage, tuple(assumptions), tuple(rules))
