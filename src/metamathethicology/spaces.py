"""Finite ground-rule operation spaces indexed by exact transfinite ordinals.

Ground here means variable-free syntax, not a derivation from Hypermath's ground
primitive. Proofs are relative to explicit assumptions and inference rules.
Stage indices have no physical units. They order language/operation availability;
they neither enumerate infinitely many operations nor supply missing premises.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ordinatics.ordinals import OMEGA, Ordinal


class Domain(str, Enum):
    """The four components of the proposed metamathethicology research program."""

    METAMATH = "metamath"
    METAPHYSICS = "metaphysics"
    METAETHICS = "metaethics"
    METALOGIC = "metalogic"


class InvalidDerivation(ValueError):
    """The supplied finite trace does not follow its exact operation space."""


class BudgetExceeded(RuntimeError):
    """The requested result is UNKNOWN because the checking budget was exhausted."""


def _text(value: object, name: str) -> None:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")


def _stage(value: object) -> None:
    if type(value) is not Ordinal:
        raise TypeError("stage must be an exact Ordinatics Ordinal")
    coefficients = value.coefficients
    if type(coefficients) is not tuple or any(
        type(c) is not int or c < 0 for c in coefficients
    ) or (coefficients and coefficients[-1] == 0):
        raise ValueError("malformed ordinal coefficients")
    if value < OMEGA:
        raise ValueError("operation stages start at omega, the first infinite ordinal")


def _tuple_of(value: object, kind: type, name: str) -> None:
    if type(value) is not tuple or any(type(item) is not kind for item in value):
        raise TypeError(f"{name} must be an immutable tuple of {kind.__name__}")


@dataclass(frozen=True, slots=True)
class Judgment:
    """An uninterpreted, domain-tagged ground proposition available at a stage.

    Arguments are literal names, not executable expressions or substitutions.
    Equal predicates in different domains or at different stages remain distinct.
    """

    domain: Domain
    predicate: str
    arguments: tuple[str, ...]
    stage: Ordinal

    def __post_init__(self) -> None:
        if type(self.domain) is not Domain:
            raise TypeError("domain must be a Domain")
        _text(self.predicate, "predicate")
        _tuple_of(self.arguments, str, "arguments")
        for argument in self.arguments:
            _text(argument, "argument")
        _stage(self.stage)


@dataclass(frozen=True, slots=True)
class Assumption:
    """An explicit premise and its declared basis; the basis is not verified here."""

    judgment: Judgment
    basis: str

    def __post_init__(self) -> None:
        if type(self.judgment) is not Judgment:
            raise TypeError("assumption must name a Judgment")
        _text(self.basis, "basis")


@dataclass(frozen=True, slots=True)
class Rule:
    """A literal inference rule with ordered premises and an explicit justification.

    Rules may preserve or increase stage. A cross-domain inference requires a
    named bridge justification. That declaration exposes an assumption; it does
    not prove a bridge sound, morally justified, or empirically correct.
    Zero-premise rules are represented as Assumptions instead.
    """

    name: str
    premises: tuple[Judgment, ...]
    conclusion: Judgment
    justification: str
    bridge: str | None = None

    def __post_init__(self) -> None:
        _text(self.name, "rule name")
        _text(self.justification, "justification")
        _tuple_of(self.premises, Judgment, "premises")
        if not self.premises:
            raise ValueError("zero-premise assertions must be explicit Assumptions")
        if type(self.conclusion) is not Judgment:
            raise TypeError("conclusion must be a Judgment")
        if any(p.stage > self.conclusion.stage for p in self.premises):
            raise ValueError("a rule cannot move a premise down to an earlier stage")
        if self.bridge is not None:
            _text(self.bridge, "bridge")
        if any(p.domain != self.conclusion.domain for p in self.premises):
            if self.bridge is None:
                raise ValueError("cross-domain inference needs an explicit bridge")


@dataclass(frozen=True, slots=True)
class OperationSpace:
    """A finite presentation of an operation space, with a transfinite stage ceiling.

    This is a reusable classical Horn-style fragment, not a complete logic of
    any domain. Absence from its positive closure is not semantic falsity.
    """

    name: str
    stage: Ordinal
    assumptions: tuple[Assumption, ...]
    rules: tuple[Rule, ...]

    def __post_init__(self) -> None:
        _text(self.name, "space name")
        _stage(self.stage)
        _tuple_of(self.assumptions, Assumption, "assumptions")
        _tuple_of(self.rules, Rule, "rules")
        labels = [rule.name for rule in self.rules]
        if len(set(labels)) != len(labels):
            raise ValueError("rule names must be unique")
        atoms = [a.judgment for a in self.assumptions]
        if len(set(atoms)) != len(atoms):
            raise ValueError("assumption judgments must be unique")
        for rule in self.rules:
            atoms.extend((*rule.premises, rule.conclusion))
        if any(atom.stage > self.stage for atom in atoms):
            raise ValueError("judgment exceeds the operation space's stage")


@dataclass(frozen=True, slots=True)
class Step:
    """Apply one named rule using earlier positions in the retained context."""

    rule: str
    premises: tuple[int, ...]
    conclusion: Judgment

    def __post_init__(self) -> None:
        _text(self.rule, "rule")
        _tuple_of(self.premises, int, "premise indices")
        if any(index < 0 for index in self.premises):
            raise ValueError("premise indices must be nonnegative")
        if type(self.conclusion) is not Judgment:
            raise TypeError("conclusion must be a Judgment")


@dataclass(frozen=True, slots=True)
class Derivation:
    """A finite submitted trace bound to the entire operation-space definition."""

    space_digest: str
    steps: tuple[Step, ...]

    def __post_init__(self) -> None:
        if type(self.space_digest) is not str or len(self.space_digest) != 64 or any(
            char not in "0123456789abcdef" for char in self.space_digest
        ):
            raise ValueError("space_digest must be a lowercase SHA-256 hexadecimal digest")
        _tuple_of(self.steps, Step, "steps")


@dataclass(slots=True)
class _Budget:
    remaining: int

    def __post_init__(self) -> None:
        if type(self.remaining) is not int or self.remaining < 1:
            raise ValueError("max_steps must be a positive integer, excluding bool")

    def take(self, count: int = 1) -> None:
        if self.remaining < count:
            raise BudgetExceeded("step budget exhausted; requested result remains UNKNOWN")
        self.remaining -= count


def replay(
    space: OperationSpace, derivation: Derivation, *, max_steps: int = 10_000,
) -> tuple[Judgment, ...]:
    """Check every premise and conclusion; return the full retained context.

    The digest binds bytes, not truth. Replay establishes derivability only
    relative to the supplied assumptions and rules. The budget counts rule and
    premise inspections; it does not bound serialization or string bit complexity.
    """
    from .representation import space_digest

    budget = _Budget(max_steps)
    if type(space) is not OperationSpace or type(derivation) is not Derivation:
        raise TypeError("replay requires an OperationSpace and Derivation")
    if derivation.space_digest != space_digest(space):
        raise InvalidDerivation("operation-space binding differs")
    budget.take(len(space.assumptions) + len(space.rules))
    context = [a.judgment for a in space.assumptions]
    rules = {rule.name: rule for rule in space.rules}
    for step in derivation.steps:
        budget.take(1 + len(step.premises))
        rule = rules.get(step.rule)
        if rule is None or rule.conclusion != step.conclusion:
            raise InvalidDerivation("unknown rule or mismatched conclusion")
        if any(index >= len(context) for index in step.premises):
            raise InvalidDerivation("premise is forward-referenced or unavailable")
        if tuple(context[index] for index in step.premises) != rule.premises:
            raise InvalidDerivation("ordered premises differ from the rule")
        context.append(step.conclusion)
    return tuple(context)


def close(space: OperationSpace, *, max_steps: int = 10_000) -> Derivation:
    """Compute the least positive closure of a finite ground-rule presentation.

    Each added judgment is the conclusion of a supplied rule, so saturation adds
    at most one new judgment per distinct rule conclusion. Unsupported cycles
    cannot start themselves. Exhaustion raises BudgetExceeded, never False.
    No transfinite sequence is traversed: ordinals constrain admissibility.
    """
    from .representation import space_digest

    if type(space) is not OperationSpace:
        raise TypeError("close requires an OperationSpace")
    budget = _Budget(max_steps)
    budget.take(len(space.assumptions) + len(space.rules))
    context = [a.judgment for a in space.assumptions]
    indices = {judgment: index for index, judgment in enumerate(context)}
    steps: list[Step] = []
    changed = True
    while changed:
        changed = False
        for rule in space.rules:
            budget.take(1 + len(rule.premises))
            if rule.conclusion in indices or any(p not in indices for p in rule.premises):
                continue
            steps.append(Step(rule.name, tuple(indices[p] for p in rule.premises), rule.conclusion))
            indices[rule.conclusion] = len(context)
            context.append(rule.conclusion)
            changed = True
    return Derivation(space_digest(space), tuple(steps))


def reflect(
    space: OperationSpace, derivation: Derivation, conclusion: Judgment,
    *, at: Ordinal, max_steps: int = 10_000,
) -> Judgment:
    """At a strictly later stage, describe an actually replayed derivation.

    The returned predicate is 'derivable-in', not an unrestricted truth predicate.
    It binds the source space, complete trace, and exact selected conclusion.
    Merely writing an atom with this predicate does not constitute reflection
    evidence: use this function to replay the source trace.
    """
    from .representation import derivation_digest, judgment_digest, space_digest

    _stage(at)
    if at <= space.stage:
        raise ValueError("reflection requires a strictly later stage")
    if conclusion not in replay(space, derivation, max_steps=max_steps):
        raise InvalidDerivation("the reflected conclusion is absent from the checked context")
    return Judgment(
        Domain.METALOGIC, "derivable-in",
        (space_digest(space), derivation_digest(derivation), judgment_digest(conclusion)), at,
    )
