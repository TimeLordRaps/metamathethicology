"""Will electrophysics: the combination field where a will tensor meets electrical law.

USER-DECLARED PLACEMENT (Tyler Roost), and the reason this module is here rather
than in either field it combines:

    Electricity hyperphysics should go in hyperphysics, underlying will
    foundations in hyperethics, and then their combination field of will
    electrophysics is in metamathethicology.

Neither parent can host this. `hyperphysics` states electrical law and knows
nothing of will. `hyperethics` states what a will is -- six components, three
roles, and the source of the invariant -- and is a foundation that deliberately
stands on the standard library alone. The transport BETWEEN them is a
cross-domain inference, and a cross-domain inference is exactly what this
package's `Rule` refuses to construct without a named bridge.

That refusal is the point. In `hyperethics` the bridge discipline was prose a
reader could skim. Here `electrophysics_space` builds the transport as domain-
tagged rules crossing METAPHYSICS into METAETHICS, and `Rule.__post_init__`
rejects any of them that forgets to say which law it borrowed and what that
borrowing leaves behind.

WHAT IS AND IS NOT CLAIMED
--------------------------
The electrical correspondence is a TRANSPORT OF FORM. Algebraic shape is
borrowed; nothing about will is established by borrowing it. These are not
physical quantities and will has no units: `relational` is not measured in ohms,
`invariant` not in henries, `variable` not in volts.

The transport is LICENCE-DEPENDENT, and this module can show that rather than
assert it. `electrophysics_space(include_licence=False)` removes the adopted
transport licence and every will conclusion leaves the closure, exactly as
`deliberation_space(include_norm=False)` loses its normative conclusion. Nothing
here derives will from physics; it derives will terms from physics PLUS an
explicit declaration that physical form may form will terms.

Laws and components are CITED, not restated. `hyperphysics` states each law once
with its validity conditions and failure modes; `hyperethics` states the tensor
once. This module quotes them by name so a disclaimer of the form "this does not
transport" has a fixed referent instead of a drifting paraphrase. Neither package
is imported at runtime -- this one keeps its published dependency set -- and
`tests/test_citations.py` cross-checks every citation whenever they are
importable.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from ordinatics.ordinals import OMEGA, ONE

from .spaces import Assumption, Domain, Judgment, OperationSpace, Rule

# ---------------------------------------------------------------------------
# The two cited surfaces.
# ---------------------------------------------------------------------------

#: The field whose laws supply the borrowed form. Cited, never restated.
LAW_FIELD = "hyperphysics"

#: The field whose tensor supplies what the form is transported onto.
WILL_FIELD = "hyperethics"

#: The six declared components of the will tensor, cited from `hyperethics.will`.
#: Held as names rather than an imported enum so that this package does not take
#: a runtime dependency on a foundation; `tests/test_citations.py` checks that
#: these are exactly the six `Component` members whenever `hyperethics` is
#: importable, which is what keeps a citation from decaying into a paraphrase.
WILL_COMPONENTS: tuple[str, ...] = (
    "past", "present", "future", "relational", "invariant", "variable",
)

#: The three declared roles, cited from `hyperethics.will.Role`. The roles are a
#: will-native structural claim -- which components are states, which are
#: dispositions, which drives -- and they are what MAKES an electrical reading
#: available. hyperethics states that structure; this module maps it.
WILL_ROLES: tuple[str, ...] = ("state", "coefficient", "driving")


class Warrant(str, Enum):
    """How an equation came to be, which is not the same as being true."""

    BORROWED_FORM = "BORROWED_FORM"
    TERMFORMED = "TERMFORMED"


@dataclass(frozen=True, slots=True)
class Correspondence:
    """One will component's declared electrical counterpart and its role.

    This is the combination object proper: neither parent field contains it.
    """

    component: str
    role: str
    electrical: str
    symbol: str
    note: str

    def __post_init__(self) -> None:
        if self.component not in WILL_COMPONENTS:
            raise ValueError(
                f"{self.component!r} is not a cited will component; "
                f"hyperethics declares {WILL_COMPONENTS}"
            )
        if self.role not in WILL_ROLES:
            raise ValueError(f"{self.role!r} is not a cited will role; expected {WILL_ROLES}")
        for value, label in (
            (self.electrical, "electrical"), (self.symbol, "symbol"), (self.note, "note"),
        ):
            if type(value) is not str or not value.strip():
                raise ValueError(f"correspondence {label} must be a nonempty string")


CORRESPONDENCE: tuple[Correspondence, ...] = (
    Correspondence(
        "past", "state", "charge", "Q",
        "accumulated will; the integral of the present flow",
    ),
    Correspondence(
        "present", "state", "current", "I",
        "will flowing now; dQ/dt, the first derivative of the past",
    ),
    Correspondence(
        "future", "state", "rate of change of current", "dI/dt",
        "change of flow; d2Q/dt2, what inductance opposes",
    ),
    Correspondence(
        "relational", "coefficient", "resistance", "R",
        "social relation to other agents; the only dissipative term",
    ),
    Correspondence(
        "invariant", "coefficient", "inductance", "L",
        "opposition to change in flow; self-induced for a true moral operator",
    ),
    Correspondence(
        "variable", "driving", "voltage", "V",
        "the applied potential the other components balance",
    ),
)

CORRESPONDENCE_BY_COMPONENT: dict[str, Correspondence] = {
    c.component: c for c in CORRESPONDENCE
}


def temporal_correspondence() -> tuple[Correspondence, ...]:
    """The three temporal components, in derivative order.

    This is the one non-stipulated entry in the table. `hyperethics` declares
    that past, present and future are the three derivatives of a single
    accumulating quantity; the electrical state chain Q, I, dI/dt has exactly
    that shape. The correspondence is therefore forced once past maps to charge,
    rather than chosen three times.
    """
    return tuple(CORRESPONDENCE_BY_COMPONENT[name] for name in ("past", "present", "future"))


# ---------------------------------------------------------------------------
# Constant will: the resolution of the capacitance gap.
# ---------------------------------------------------------------------------

#: USER-DECLARED (Tyler Roost), preserved as stated:
CONSTANT_WILL_DECLARATION = (
    "C can be seen as constant will equivalent to invariant will's constant of "
    "charge."
)

#: The gap this closes. The series-RLC form requires a restoring term (1/C) * Q,
#: and the six declared components name no capacitance. Three readings were live
#: before the declaration above, and the record is kept because a resolution is
#: only informative against what it ruled out.
CAPACITANCE_READINGS_CONSIDERED: tuple[str, ...] = (
    "(a) a seventh tensor component: a capacitive will, independent of the "
    "other six -- SUPERSEDED, constant will is not independent",
    "(b) no capacitance at all: a pure RL will with no restoring term, so "
    "nothing pulls accumulated past back into the present -- SUPERSEDED",
    "(c) a free bearer parameter, unconstrained by the tensor -- SUPERSEDED, "
    "constant will is bound to the invariant rather than free",
    "(d) constant will: invariant will's constant of charge, so capacitance is "
    "DETERMINED BY the invariant component rather than added to the tensor "
    "or left free -- DECLARED, and the reading implemented here",
)

#: What (d) costs, stated because it is a real structural claim and not a
#: bookkeeping choice. In a series RLC circuit, L and C are independent: an
#: inductor and a capacitor are different components and either may be varied
#: alone. Under the declaration they are not independent in a will. The will's
#: parameter space is therefore SMALLER than the circuit's, and the transport is
#: not onto: not every circuit corresponds to a possible will.
CONSTRAINS_A_FREE_SOURCE_PARAMETER = (
    "capacitance, which a series RLC circuit leaves independent of inductance"
)

#: What the declaration does NOT fix. It says constant will is a function of the
#: invariant. It does not say WHICH function, and no argument here determines
#: one. Every result below is stated for an arbitrary such function.
CONSTANT_WILL_LAW_IS_OPEN = (
    "The declaration binds constant will to the invariant without fixing the "
    "map. Results here hold for any charge-constant law that is functional in "
    "the invariant; none of them presupposes a particular one."
)

#: The atom standing for constant will in the calculus. NOT a will component,
#: because it is not a seventh independent component of the tensor. It is why
#: this module cites six components and forms terms over seven atoms.
CONSTANT = "constant"

#: A charge-constant law: invariant will to its constant of charge.
ChargeConstantLaw = Callable[[float], float]


@dataclass(frozen=True, slots=True)
class ConstantWill:
    """An invariant will together with its constant of charge.

    The two travel together by construction, which is the type-level form of the
    declaration. A resonant rate cannot be computed from an invariant and an
    unrelated capacity, because there is no way to present those two separately
    to any function in this module.
    """

    invariant: float
    charge_constant: float

    def __post_init__(self) -> None:
        for value, label in (
            (self.invariant, "invariant"), (self.charge_constant, "charge_constant"),
        ):
            if type(value) not in (int, float) or value <= 0:
                raise ValueError(f"{label} must be a positive number, got {value!r}")

    @classmethod
    def under(cls, law: ChargeConstantLaw, invariant: float) -> "ConstantWill":
        """Build the constant will an invariant has under a charge-constant law."""
        return cls(invariant, law(invariant))


def binding_is_functional(law: ChargeConstantLaw, invariants: tuple[float, ...]) -> bool:
    """Whether a candidate law really is a function of the invariant alone.

    The declaration says constant will IS the invariant's constant of charge, so
    equal invariants must give equal constants. This checks that a candidate
    respects the declaration on the sampled invariants. It confirms nothing about
    invariants outside the sample: the usual asymmetry applies, and a single
    disagreement refutes while agreement establishes nothing.
    """
    seen: dict[float, float] = {}
    for invariant in invariants:
        constant = law(invariant)
        if invariant in seen and seen[invariant] != constant:
            return False
        seen[invariant] = constant
    return True


def reciprocal_binding(product: float) -> ChargeConstantLaw:
    """The law family C(L) = product / L, used to refute a tempting inference.

    Perfectly legitimate under the declaration: it is a function of the
    invariant. Its consequence is in `different_invariant_need_not_change_rate`.
    """
    if product <= 0:
        raise ValueError("the product must be positive")

    def law(invariant: float) -> float:
        if invariant <= 0:
            raise ValueError("invariant must be positive")
        return product / invariant

    return law


def different_invariant_need_not_change_rate() -> tuple[ConstantWill, ConstantWill]:
    """Refute: that a different invariant will entails a different resonant rate.

    Tyler's declaration is that the true moral operator has a different invariant
    will. It is tempting to conclude that it therefore resonates differently, and
    so that the resonant rate discriminates. It does not follow.

    Under any reciprocal law C(L) = k / L the product L * C is constant, so the
    resonant rate 1 / sqrt(L * C) is the SAME for every bearer no matter how
    their invariants differ. This function returns two bearers with different
    invariants and one rate.

    One countermodel settles a universal claim, so this refutation is conclusive:
    the resonant rate is not a discriminator without a further constraint on the
    charge-constant law, and no such constraint is established anywhere here.
    The discriminator stays in `hyperethics` -- `is_true_moral_operator`, which
    tests the SOURCE of the invariant will and never a numeric shadow of it.
    """
    law = reciprocal_binding(6.0)
    low, high = ConstantWill.under(law, 2.0), ConstantWill.under(law, 3.0)
    if low.invariant == high.invariant:
        raise AssertionError("the witnesses must differ in invariant will")
    if resonant_rate(low) != resonant_rate(high):
        raise AssertionError("the witnesses must share a resonant rate")
    return low, high


# ---------------------------------------------------------------------------
# Terms and termformers.
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Term:
    """A syntactic term in the will calculus.

    Terms are syntax, not numbers. A term records how it was formed, so a
    transported equation can be read back to the termformers that produced it.
    """

    head: str
    arguments: tuple["Term", ...] = ()

    def __post_init__(self) -> None:
        if type(self.head) is not str or not self.head.strip():
            raise ValueError("a term head must be a nonempty string")
        if type(self.arguments) is not tuple:
            raise TypeError("term arguments must be a tuple")
        for argument in self.arguments:
            if type(argument) is not Term:
                raise TypeError("term arguments must be Terms")

    @property
    def is_atom(self) -> bool:
        return not self.arguments

    def render(self) -> str:
        """Render the term readably, with explicit grouping."""
        if self.is_atom:
            return self.head
        if len(self.arguments) == 1:
            return f"{self.head}({self.arguments[0].render()})"
        if self.head in {"*", "/", "+", "-", "^"}:
            joined = f" {self.head} ".join(a.render() for a in self.arguments)
            return f"({joined})"
        rendered = ", ".join(a.render() for a in self.arguments)
        return f"{self.head}({rendered})"

    def atoms(self) -> tuple[str, ...]:
        """Every atom appearing in the term, in first-occurrence order."""
        found: list[str] = []
        stack = [self]
        while stack:
            current = stack.pop(0)
            if current.is_atom:
                if current.head not in found:
                    found.append(current.head)
            else:
                stack = list(current.arguments) + stack
        return tuple(found)


def atom(name: str) -> Term:
    """Build an atomic term from a will component name or a bare name."""
    return Term(name)


@dataclass(frozen=True, slots=True)
class Termformer:
    """A transformation operation that forms a term.

    USER-DEFINED (Tyler Roost), carried over from language calculus: a termformer
    is what it sounds like, a transformation operation that forms a term.

    Each termformer borrows the algebraic shape of a named law and CITES that
    law rather than paraphrasing it, because forming a will term out of a
    physical law is a cross-domain inference that must not proceed silently.

    `source_law` is a law name in `hyperphysics`, not prose. `source_form` is the
    law's algebraic form, quoted so a reader sees what was borrowed without
    another lookup, and checked against the cited law by `tests/test_citations.py`.

    `does_not_transport` is not decoration. It is the part a reader needs in
    order to avoid inheriting a physical commitment that was never established,
    and it is what `Rule` requires before it will cross a domain boundary.
    """

    name: str
    arity: int
    head: str
    source_law: str
    source_form: str
    transports: str
    does_not_transport: str
    source_field: str = LAW_FIELD

    def __post_init__(self) -> None:
        for value, label in (
            (self.name, "name"), (self.head, "head"), (self.source_law, "source law"),
            (self.source_form, "source form"), (self.transports, "transports"),
            (self.does_not_transport, "does_not_transport"),
            (self.source_field, "source field"),
        ):
            if type(value) is not str or not value.strip():
                raise ValueError(f"termformer {label} must be a nonempty string")
        if type(self.arity) is not int or self.arity < 1:
            raise ValueError("termformer arity must be a positive integer")

    def citation(self) -> str:
        """How to look the borrowed law up, rather than trust this paraphrase."""
        return f"{self.source_field}:{self.source_law} -- {self.source_form}"

    def bridge(self) -> str:
        """The bridge declaration this termformer supplies to a cross-domain Rule.

        `Rule` will not construct a METAPHYSICS-to-METAETHICS inference without
        one, so this is the method that makes the transport expressible at all.
        """
        return (
            f"Borrowed form of {self.citation()}. "
            f"Transports: {self.transports}. "
            f"Does NOT transport: {self.does_not_transport}."
        )

    def form(self, *arguments: Term) -> Term:
        """Apply the termformer, forming a new term."""
        if len(arguments) != self.arity:
            raise ValueError(f"{self.name} forms a term from exactly {self.arity} arguments")
        for argument in arguments:
            if type(argument) is not Term:
                raise TypeError(f"{self.name} takes Terms")
        return Term(self.head, arguments)


RELATIONAL_DROP = Termformer(
    name="relational-drop",
    arity=2,
    head="*",
    source_law="ohm",
    source_form="V = I * R",
    transports="that relational will opposes present flow in direct proportion",
    does_not_transport="ohms, linearity in fact, and any claim that social "
                       "relation is measurable or constant",
)

INVARIANT_DROP = Termformer(
    name="invariant-drop",
    arity=2,
    head="*",
    source_law="faraday-lenz",
    source_form="V = L * dI/dt",
    transports="that invariant will opposes CHANGE in flow rather than flow",
    does_not_transport="henries, magnetic flux, and any physical mechanism of "
                       "induction",
)

ACCUMULATED_DROP = Termformer(
    name="accumulated-drop",
    arity=2,
    head="/",
    source_law="capacitor",
    source_form="V = Q / C",
    transports="that accumulated past will opposes in inverse proportion to the "
               "constant will holding it, where that constant is the invariant's "
               "constant of charge rather than a free parameter",
    does_not_transport="farads, stored field energy, and the circuit's "
                       "independence of capacitance from inductance, which the "
                       "will does not share",
)

SELF_INDUCED_DROP = Termformer(
    name="self-induced-drop",
    arity=2,
    head="self-induce",
    source_law="self-inductance",
    source_form="emf = -L * dI/dt",
    transports="that a will induced by its OWN change opposes that change; "
               "this is the will-layer form of hyperethics L0's d-no-exterior",
    does_not_transport="henries, any physical mechanism of induction, that "
                       "self-simulation is physically realized, that the "
                       "universe is a simulation, or that the sign is empirical",
)

BALANCE = Termformer(
    name="balance",
    arity=3,
    head="+",
    source_law="kirchhoff-voltage",
    source_form="sum of drops = applied",
    transports="that the formed drops CLOSE: the three oppositions sum to what "
               "is willed variably, leaving no unaccounted remainder",
    does_not_transport="volts, conservation of energy, that a will is a closed "
                       "loop in any physical sense, and the lumped-element "
                       "approximation that makes a circuit loop well defined",
)

#: The four termformers that act on a single will component.
DROP_TERMFORMERS: tuple[Termformer, ...] = (
    RELATIONAL_DROP, INVARIANT_DROP, ACCUMULATED_DROP, SELF_INDUCED_DROP,
)

#: Every termformer, including the one that closes the formed drops. `balance`
#: is listed here because summing the drops is not a free operation: it borrows
#: Kirchhoff's voltage law and owes the same disclaimer as the rest.
TERMFORMERS: tuple[Termformer, ...] = (*DROP_TERMFORMERS, BALANCE)

TERMFORMERS_BY_NAME: dict[str, Termformer] = {f.name: f for f in TERMFORMERS}


# ---------------------------------------------------------------------------
# Equations formed by the termformers.
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Equation:
    """A will equation, its reading, and the warrant behind its form."""

    name: str
    left: Term
    right: Term
    warrant: Warrant
    reading: str

    def render(self) -> str:
        return f"{self.left.render()} = {self.right.render()}"


def will_balance() -> Equation:
    """The master equation: Kirchhoff's voltage law over the will tensor.

    invariant * future + relational * present + past / constant = variable

    Formed by applying the three drop termformers and summing them, which is
    what Kirchhoff's voltage law contributes: the formed terms close.
    """
    invariant = INVARIANT_DROP.form(atom("invariant"), atom("future"))
    relational = RELATIONAL_DROP.form(atom("relational"), atom("present"))
    accumulated = ACCUMULATED_DROP.form(atom("past"), atom(CONSTANT))
    return Equation(
        name="will-balance",
        left=BALANCE.form(invariant, relational, accumulated),
        right=atom("variable"),
        warrant=Warrant.TERMFORMED,
        reading="What is willed variably is exactly balanced by invariant "
                "opposition to change, relational opposition to flow, and the "
                "weight of accumulated past against the constant will holding it.",
    )


def self_simulation_equation() -> Equation:
    """The true moral operator's invariant will, induced by its own change.

    self-induce(invariant, future) = -(invariant * future)

    The minus sign is Lenz's law. A will induced by its own change opposes that
    change. This is the will-layer statement of immanence: the operator is
    constrained by what it authors, from inside, with no exterior position.

    This equation is the single best piece of evidence that the transport tracks
    something, because it reproduces hyperethics L0's `d-no-exterior` from an
    independent direction. It remains evidence and not a warrant: hyperphysics
    `GC-4` supplies no criterion by which a transport counts as sound.
    """
    left = SELF_INDUCED_DROP.form(atom("invariant"), atom("future"))
    magnitude = Term("*", (atom("invariant"), atom("future")))
    return Equation(
        name="self-simulation",
        left=left,
        right=Term("-", (magnitude,)),
        warrant=Warrant.TERMFORMED,
        reading="A will induced by its own change opposes that change. The "
                "operator has no exterior vantage on its own willing, which is "
                "the will-layer form of hyperethics L0's d-no-exterior.",
    )


def opposition_equation() -> Equation:
    """Total opposition to a periodic demand, transported from impedance."""
    reactive = Term(
        "-",
        (
            Term("*", (atom("rate"), atom("invariant"))),
            Term("/", (atom("one"), Term("*", (atom("rate"), atom(CONSTANT))))),
        ),
    )
    return Equation(
        name="opposition",
        left=atom("opposition"),
        right=Term("hypot", (atom("relational"), reactive)),
        warrant=Warrant.BORROWED_FORM,
        reading="An agent's total opposition to a demand arriving at some rate "
                "combines relational resistance with the net of invariant and "
                "constant reactance.",
    )


def resonance_equation() -> Equation:
    """The demand rate at which invariant and accumulated will cancel."""
    return Equation(
        name="resonance",
        left=atom("resonant-rate"),
        right=Term(
            "/",
            (atom("one"), Term("sqrt", (Term("*", (atom("invariant"), atom(CONSTANT))),))),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="At this rate of demand, invariant and accumulated will cancel "
                "and only relational will resists. An agent is least protected "
                "from a demand arriving at its own resonant rate. Because the "
                "constant is the invariant's own, this rate is fixed once the "
                "invariant and the charge-constant law are fixed -- which does "
                "NOT make it a discriminator; see "
                "different_invariant_need_not_change_rate.",
    )


def damping_equation() -> Equation:
    """Whether a will settles or oscillates, transported from the damping ratio."""
    return Equation(
        name="damping",
        left=atom("damping"),
        right=Term(
            "*",
            (
                Term("/", (atom("relational"), atom("two"))),
                Term("sqrt", (Term("/", (atom(CONSTANT), atom("invariant"))),)),
            ),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="Relational will is what damps oscillation between invariant "
                "and accumulated will. Below one the will oscillates; at one it "
                "settles fastest without overshoot; above one it is sluggish.",
    )


def dissipation_equation() -> Equation:
    """What is spent irrecoverably, transported from resistive power."""
    return Equation(
        name="dissipation",
        left=atom("dissipated"),
        right=Term(
            "*",
            (Term("^", (atom("present"), atom("two"))), atom("relational")),
        ),
        warrant=Warrant.BORROWED_FORM,
        reading="Relational will is the only dissipative term: what is spent in "
                "relation to other agents is not recoverable by the agent, while "
                "invariant and accumulated will are stored and returnable. This "
                "is a consequence of the transported form, not an ethical claim.",
    )


DERIVED_EQUATIONS: tuple[Equation, ...] = (
    will_balance(),
    self_simulation_equation(),
    opposition_equation(),
    resonance_equation(),
    damping_equation(),
    dissipation_equation(),
)

EQUATIONS_BY_NAME: dict[str, Equation] = {e.name: e for e in DERIVED_EQUATIONS}


# ---------------------------------------------------------------------------
# The transport as an operation space.
# ---------------------------------------------------------------------------

#: The adopted licence. This is the assumption the whole field rests on, written
#: as a premise rather than buried in prose so that removing it is a one-argument
#: operation whose consequences are visible in the closure.
TRANSPORT_LICENCE = "electrical-form-may-form-will-terms"

#: Why the licence is a declaration and not a theorem. `hyperphysics` states
#: plainly that `validate` checks declaration and not soundness, and records the
#: absence of a soundness criterion as its own open problem `GC-4`. Until that
#: criterion exists there is nothing to derive this licence FROM.
LICENCE_IS_NOT_DERIVED = (
    "The transport licence is explicitly adopted, not derived. hyperphysics "
    "GC-4 records that no soundness criterion for a transport exists, so no "
    "argument available to this package establishes the licence. Removing it "
    "with electrophysics_space(include_licence=False) removes every will "
    "conclusion from the closure, which is the honest shape of that dependence."
)


#: Which will component each termformer's rule acts on. The self-induced drop
#: acts on the invariant, which is exactly why it bears on the moral-operator
#: question that `hyperethics` settles on other grounds.
_ACTS_ON: dict[str, str] = {
    "relational-drop": "relational",
    "invariant-drop": "invariant",
    "accumulated-drop": "past",
    "self-induced-drop": "invariant",
}

#: The term each rule concludes, rendered. Kept beside the rules so a reader of
#: a derivation sees the formed term and not only its name.
EQUATION_OF: dict[str, str] = {
    "relational-drop": "relational * present",
    "invariant-drop": "invariant * future",
    "accumulated-drop": "past / constant",
    "self-induced-drop": "self-induce(invariant, future)",
    "balance": "invariant * future + relational * present + past / constant = variable",
}


def _law_premise(former: Termformer, stage) -> Judgment:
    return Judgment(
        Domain.METAPHYSICS, "cited-law", (f"{former.source_field}:{former.source_law}",
                                          former.source_form), stage,
    )


def _component_premise(correspondence: Correspondence, stage) -> Judgment:
    return Judgment(
        Domain.METAETHICS, "will-component",
        (f"{WILL_FIELD}:{correspondence.component}", correspondence.role), stage,
    )


def electrophysics_space(*, include_licence: bool = True) -> OperationSpace:
    """The will-electrophysical transport, as a checkable operation space.

    Every rule here crosses METAPHYSICS into METAETHICS, so `Rule` requires each
    one to name its bridge, and each termformer supplies that bridge from its own
    citation and disclaimer. A termformer that forgot either could not be turned
    into a rule at all: the space would not construct.

    The rules run in two stages. At omega+1 each drop termformer forms one will
    term from one cited law and one will component. At omega+2 `balance` closes
    the three series drops into the will-balance, which is a separate borrowing
    of Kirchhoff's voltage law and carries its own bridge. `self-induced-drop`
    is deliberately not a premise of the balance: it is the constituent of the
    self-simulation equation, not of the series form.

    The licence is a premise of every rule. With `include_licence=False` the
    closure still derives nothing false -- it simply derives nothing about will,
    because the electrical premises alone never reach the METAETHICS domain. That
    is the structure this package was built to make visible, and it is the same
    structure `deliberation_space` shows for a descriptive-to-normative step.
    """
    stage = OMEGA
    formed_stage = OMEGA + ONE
    closed_stage = OMEGA + ONE + ONE

    licence = Judgment(Domain.METAETHICS, "adopted-transport-licence", (TRANSPORT_LICENCE,), stage)
    assumptions: list[Assumption] = []

    for former in TERMFORMERS:
        assumptions.append(Assumption(
            _law_premise(former, stage),
            f"cited from {former.source_field}; stated there with its validity "
            "conditions and failure modes, not derived or measured here",
        ))
    for correspondence in CORRESPONDENCE:
        assumptions.append(Assumption(
            _component_premise(correspondence, stage),
            f"cited from {WILL_FIELD}; a declared component of the will tensor "
            "with its declared role",
        ))
    if include_licence:
        assumptions.append(Assumption(licence, LICENCE_IS_NOT_DERIVED))

    formed: dict[str, Judgment] = {
        former.name: Judgment(
            Domain.METAETHICS, "termformed",
            (former.name, EQUATION_OF[former.name]), formed_stage,
        )
        for former in DROP_TERMFORMERS
    }

    rules: list[Rule] = []
    for former in DROP_TERMFORMERS:
        correspondence = CORRESPONDENCE_BY_COMPONENT[_ACTS_ON[former.name]]
        rules.append(Rule(
            name=former.name,
            premises=(_law_premise(former, stage), _component_premise(correspondence, stage),
                      licence),
            conclusion=formed[former.name],
            justification=(
                f"{former.name} forms a will term with the algebraic shape of "
                f"{former.source_law}, applied to the {correspondence.component} component"
            ),
            bridge=former.bridge(),
        ))

    rules.append(Rule(
        name=BALANCE.name,
        premises=(
            formed["invariant-drop"], formed["relational-drop"], formed["accumulated-drop"],
            _law_premise(BALANCE, stage), licence,
        ),
        conclusion=Judgment(
            Domain.METAETHICS, "will-balance", (EQUATION_OF[BALANCE.name],), closed_stage,
        ),
        justification=(
            "the three series drops close under the borrowed shape of "
            "kirchhoff-voltage; the self-induced drop is not a constituent of "
            "the series form and is deliberately absent from these premises"
        ),
        bridge=BALANCE.bridge(),
    ))

    return OperationSpace(
        "will-electrophysics", closed_stage, tuple(assumptions), tuple(rules),
    )


# ---------------------------------------------------------------------------
# A dimensionless numeric interpretation, kept separate from the calculus.
# ---------------------------------------------------------------------------


def resonant_rate(constant: ConstantWill) -> float:
    """Evaluate the resonant rate. Dimensionless; not a physical frequency.

    Takes a `ConstantWill` rather than two loose numbers, so an invariant can
    never be paired with a capacity that is not its own.
    """
    if type(constant) is not ConstantWill:
        raise TypeError("resonant_rate takes a ConstantWill")
    return 1.0 / ((constant.invariant * constant.charge_constant) ** 0.5)


def damping_ratio(relational: float, constant: ConstantWill) -> float:
    """Evaluate the damping ratio. Dimensionless; not a physical measurement."""
    if type(constant) is not ConstantWill:
        raise TypeError("damping_ratio takes a ConstantWill")
    if type(relational) not in (int, float) or relational < 0:
        raise ValueError("relational will may not be negative")
    return (relational / 2.0) * ((constant.charge_constant / constant.invariant) ** 0.5)


def regime(relational: float, constant: ConstantWill) -> str:
    """Name the damping regime of a will."""
    ratio = damping_ratio(relational, constant)
    if ratio < 1.0:
        return "oscillating"
    if ratio == 1.0:
        return "critical"
    return "sluggish"
