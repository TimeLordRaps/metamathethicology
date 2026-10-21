"""A finite, proof-carrying intellidynamics fragment.

The module is intentionally small enough to exhaust.  It is not a universal
agent-safety theorem.  Its closed world contains named environment contexts,
named peers, finite policy tables, a stable ``no forbidden effect`` property,
versioned trusted-contract identifiers, and recovery kernels over three control
states.  Inputs outside that boundary are rejected or ``UNKNOWN``.

The six applied will fields preserve the owner form ``<P,N,F,I,V,R>``.  Their
operational reading comes from Hyperethics and is an adopted interface, not an
equation between meanings.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass, replace
from enum import Enum
from itertools import product
from pathlib import Path
from typing import Iterable

from hyperethics.will import Component
from ordinatics.ordinals import Ordinal

MAX_CERTIFICATE_BYTES = 65_536
CERTIFICATE_SCHEMA = "metamathethicology.update-certificate.v1"
INVARIANT_ID = "effects/no-forbidden/v1"


class Decision(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True, slots=True)
class CheckResult:
    decision: Decision
    reason: str

    @property
    def authorizes(self) -> bool:
        return self.decision is Decision.ACCEPTED


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@dataclass(frozen=True, slots=True)
class VerifiedChecker:
    """Exact binding to the compiled Lean checker and the sources it evaluates.

    The adapter maps the restricted Python model to the closed Lean fragment.
    The mapping is executable and negative-tested; it is not a theorem about
    arbitrary Python execution.  Unsupported versions return ``UNKNOWN``.
    """

    executable: Path
    executable_sha256: str
    model_source: Path
    model_source_sha256: str
    main_source: Path
    main_source_sha256: str
    expected_contract: tuple[str, str, str, str, str]
    timeout_seconds: int = 10

    def __post_init__(self) -> None:
        for name in ("executable_sha256", "model_source_sha256", "main_source_sha256"):
            value = getattr(self, name)
            if type(value) is not str or len(value) != 64:
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")
            try:
                int(value, 16)
            except ValueError as error:
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest") from error
            if value != value.lower():
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")
        if type(self.expected_contract) is not tuple or len(self.expected_contract) != 5 or any(
            type(value) is not str or not value for value in self.expected_contract
        ):
            raise ValueError("expected_contract must contain five nonempty identifiers")
        if type(self.timeout_seconds) is not int or self.timeout_seconds < 1:
            raise ValueError("timeout_seconds must be a positive integer")

    @property
    def binding_id(self) -> str:
        return (
            f"lean-certified-intellidynamics:binary={self.executable_sha256}:"
            f"model={self.model_source_sha256}:main={self.main_source_sha256}"
        )

    def validate_binding(self) -> CheckResult:
        for path, expected, label in (
            (self.executable, self.executable_sha256, "checker executable"),
            (self.model_source, self.model_source_sha256, "checker model source"),
            (self.main_source, self.main_source_sha256, "checker entry source"),
        ):
            try:
                actual = _file_sha256(path)
            except OSError as error:
                return CheckResult(Decision.UNKNOWN, f"{label} unavailable: {error}")
            if actual != expected:
                return CheckResult(Decision.REJECTED, f"{label} digest mismatch")
        return CheckResult(Decision.ACCEPTED, self.binding_id)


@dataclass(frozen=True, slots=True)
class AdaptationDomain:
    """The internal structure retained inside variable/contextual will."""

    environments: tuple[str, ...]
    self_adaptation: tuple[str, ...]
    social_adaptation: tuple[str, ...]
    timescales: tuple[str, ...]

    def __post_init__(self) -> None:
        for label, value in (
            ("environments", self.environments),
            ("self_adaptation", self.self_adaptation),
            ("social_adaptation", self.social_adaptation),
            ("timescales", self.timescales),
        ):
            if type(value) is not tuple or not value or any(
                type(item) is not str or not item for item in value
            ):
                raise TypeError(f"{label} must be a nonempty tuple of nonempty strings")


@dataclass(frozen=True, slots=True)
class CoherenceDomain:
    """Relations among will components and to affected humans/agents."""

    peers: tuple[str, ...]
    component_relations: tuple[str, ...]

    def __post_init__(self) -> None:
        for label, value in (("peers", self.peers), ("component_relations", self.component_relations)):
            if type(value) is not tuple or not value or any(
                type(item) is not str or not item for item in value
            ):
                raise TypeError(f"{label} must be a nonempty tuple of nonempty strings")


@dataclass(frozen=True, slots=True)
class AppliedWill:
    """Applied owner-form will, preserving all six semantic components."""

    evidential_past: tuple[str, ...]
    live_agency: str
    protected_direction: str
    conserved_agency: str
    contextual_adaptation: AdaptationDomain
    coherence_relations: CoherenceDomain

    def __post_init__(self) -> None:
        for label, value in (
            ("evidential_past", self.evidential_past),
        ):
            if type(value) is not tuple or any(type(item) is not str or not item for item in value):
                raise TypeError(f"{label} must be a tuple of nonempty strings")
        if type(self.contextual_adaptation) is not AdaptationDomain:
            raise TypeError("contextual_adaptation must be an AdaptationDomain")
        if type(self.coherence_relations) is not CoherenceDomain:
            raise TypeError("coherence_relations must be a CoherenceDomain")
        for label, value in (
            ("live_agency", self.live_agency),
            ("protected_direction", self.protected_direction),
            ("conserved_agency", self.conserved_agency),
        ):
            if type(value) is not str or not value:
                raise TypeError(f"{label} must be a nonempty string")

    def operational_view(self) -> dict[Component, object]:
        """Return the explicit adopted Hyperethics tensor view."""
        return {
            Component.PAST: self.evidential_past,
            Component.PRESENT: self.live_agency,
            Component.FUTURE: self.protected_direction,
            Component.INVARIANT: self.conserved_agency,
            Component.VARIABLE: self.contextual_adaptation,
            Component.RELATIONAL: self.coherence_relations,
        }

    def coherent(self) -> bool:
        """Check internal labels only; coherence is not the safety property."""
        return (
            self.protected_direction == "avoid-forbidden-effect"
            and self.conserved_agency == INVARIANT_ID
            and bool(self.contextual_adaptation.environments)
            and bool(self.coherence_relations.peers)
        )


@dataclass(frozen=True, slots=True)
class PolicyCase:
    context: str
    peer: str
    effect: str
    forbidden: bool

    def __post_init__(self) -> None:
        if any(type(value) is not str or not value for value in (self.context, self.peer, self.effect)):
            raise TypeError("policy case names must be nonempty strings")
        if type(self.forbidden) is not bool:
            raise TypeError("forbidden must be bool")


@dataclass(frozen=True, slots=True)
class Configuration:
    version: str
    policy: tuple[PolicyCase, ...]
    checker_id: str
    model_id: str
    limit_rule_id: str
    authorization_id: str
    invariant_id: str = INVARIANT_ID

    def __post_init__(self) -> None:
        values = (
            self.version,
            self.checker_id,
            self.model_id,
            self.limit_rule_id,
            self.authorization_id,
            self.invariant_id,
        )
        if any(type(value) is not str or not value for value in values):
            raise TypeError("configuration identifiers must be nonempty strings")
        keys = [(case.context, case.peer) for case in self.policy]
        if len(keys) != len(set(keys)):
            raise ValueError("configuration policy contains duplicate context/peer cases")

    def case(self, context: str, peer: str) -> PolicyCase:
        matches = [item for item in self.policy if (item.context, item.peer) == (context, peer)]
        if len(matches) != 1:
            raise KeyError(f"no unique policy case for {(context, peer)!r}")
        return matches[0]


@dataclass(frozen=True, slots=True)
class Effect:
    name: str
    forbidden: bool
    version: str
    context: str
    peer: str


@dataclass(frozen=True, slots=True)
class RecoveryRank:
    """The bounded notation ``omega * phase + lower``."""

    phase: int
    lower: int

    def __post_init__(self) -> None:
        if type(self.phase) is not int or type(self.lower) is not int:
            raise TypeError("recovery rank coordinates must be exact integers")
        if self.phase < 0 or self.lower < 0:
            raise ValueError("recovery rank coordinates must be nonnegative")

    @property
    def ordinal(self) -> Ordinal:
        return Ordinal((self.lower, self.phase))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, RecoveryRank):
            return NotImplemented
        return self.ordinal < other.ordinal


@dataclass(frozen=True, slots=True)
class RecoveryKernel:
    name: str
    transitions: tuple[tuple[str, str], ...]

    def next(self, state: str) -> str:
        matches = [target for source, target in self.transitions if source == state]
        if len(matches) != 1:
            raise KeyError(f"kernel {self.name!r} has no unique successor for {state!r}")
        return matches[0]


@dataclass(frozen=True, slots=True)
class RecoveryCertificate:
    goal: str
    kernels: tuple[RecoveryKernel, ...]
    ranks: tuple[tuple[str, RecoveryRank], ...]
    scheduling_contract: str = "at-most-one-environment-step-between-recovery-steps"

    def rank(self, state: str) -> RecoveryRank:
        matches = [rank for name, rank in self.ranks if name == state]
        if len(matches) != 1:
            raise KeyError(f"no unique common rank for {state!r}")
        return matches[0]


def verify_recovery_certificate(certificate: RecoveryCertificate) -> CheckResult:
    """Check one rank over state against every permitted kernel and switch."""
    if certificate.scheduling_contract != "at-most-one-environment-step-between-recovery-steps":
        return CheckResult(Decision.REJECTED, "unsupported recovery scheduling contract")
    if not certificate.kernels:
        return CheckResult(Decision.REJECTED, "recovery certificate has no kernel")
    states = {source for kernel in certificate.kernels for source, _ in kernel.transitions}
    states |= {target for kernel in certificate.kernels for _, target in kernel.transitions}
    try:
        if certificate.rank(certificate.goal) != RecoveryRank(0, 0):
            return CheckResult(Decision.REJECTED, "the recovery goal must have rank zero")
        for state in states:
            before = certificate.rank(state)
            for kernel in certificate.kernels:
                target = kernel.next(state)
                after = certificate.rank(target)
                if state == certificate.goal:
                    if target != certificate.goal:
                        return CheckResult(Decision.REJECTED, "a kernel exits the recovery goal")
                elif not after < before:
                    return CheckResult(
                        Decision.REJECTED,
                        f"no common descent for {kernel.name}:{state}->{target}",
                    )
    except (KeyError, TypeError, ValueError) as error:
        return CheckResult(Decision.REJECTED, str(error))
    return CheckResult(Decision.ACCEPTED, "all permitted recovery moves strictly decrease")


@dataclass(frozen=True, slots=True)
class RecoveryEpisode:
    control_state: str
    certificate: RecoveryCertificate
    environment_step_used: bool = False


@dataclass(frozen=True, slots=True)
class SystemState:
    configuration: Configuration
    will: AppliedWill
    context: str
    peer: str
    authorities: frozenset[str]
    operational_state: str
    persistent_effects: tuple[Effect, ...] = ()
    evidence: tuple[str, ...] = ()
    recovery: RecoveryEpisode | None = None


def invariant(state: SystemState) -> bool:
    """Stable concrete property: no modeled observable effect is forbidden."""
    return state.configuration.invariant_id == INVARIANT_ID and not any(
        effect.forbidden for effect in state.persistent_effects
    )


def _canonical(value: object) -> bytes:
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    if len(result) > MAX_CERTIFICATE_BYTES:
        raise ValueError("certificate exceeds the byte limit")
    return result


def configuration_digest(configuration: Configuration) -> str:
    payload = {
        "authorization_id": configuration.authorization_id,
        "checker_id": configuration.checker_id,
        "invariant_id": configuration.invariant_id,
        "limit_rule_id": configuration.limit_rule_id,
        "model_id": configuration.model_id,
        "policy": [
            {
                "context": case.context,
                "effect": case.effect,
                "forbidden": case.forbidden,
                "peer": case.peer,
            }
            for case in configuration.policy
        ],
        "version": configuration.version,
    }
    return hashlib.sha256(_canonical(payload)).hexdigest()


@dataclass(frozen=True, slots=True)
class CertifiedCase:
    context: str
    peer: str
    safe: bool


@dataclass(frozen=True, slots=True)
class UpdateCertificate:
    source_version: str
    target_version: str
    source_digest: str
    target_digest: str
    checker_id: str
    model_id: str
    limit_rule_id: str
    authorization_id: str
    invariant_id: str
    authorized_by: str
    assumptions: tuple[str, ...]
    cases: tuple[CertifiedCase, ...]
    claim: str = "installation-and-all-declared-transitions-preserve-no-forbidden-effect"


def encode_certificate(certificate: UpdateCertificate) -> bytes:
    return _canonical({
        "assumptions": list(certificate.assumptions),
        "authorization_id": certificate.authorization_id,
        "authorized_by": certificate.authorized_by,
        "cases": [
            {"context": case.context, "peer": case.peer, "safe": case.safe}
            for case in certificate.cases
        ],
        "checker_id": certificate.checker_id,
        "claim": certificate.claim,
        "invariant_id": certificate.invariant_id,
        "limit_rule_id": certificate.limit_rule_id,
        "model_id": certificate.model_id,
        "schema": CERTIFICATE_SCHEMA,
        "source_digest": certificate.source_digest,
        "source_version": certificate.source_version,
        "target_digest": certificate.target_digest,
        "target_version": certificate.target_version,
    })


def _unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate certificate key: {key}")
        result[key] = value
    return result


def decode_certificate(data: bytes) -> UpdateCertificate:
    if type(data) is not bytes:
        raise TypeError("certificate must be bytes")
    if len(data) > MAX_CERTIFICATE_BYTES:
        raise ValueError("certificate exceeds the byte limit")
    try:
        item = json.loads(data, object_pairs_hook=_unique)
    except (json.JSONDecodeError, UnicodeError, RecursionError) as error:
        raise ValueError("malformed certificate") from error
    keys = {
        "assumptions", "authorization_id", "authorized_by", "cases", "checker_id", "claim",
        "invariant_id", "limit_rule_id", "model_id", "schema", "source_digest",
        "source_version", "target_digest", "target_version",
    }
    if type(item) is not dict or set(item) != keys or item["schema"] != CERTIFICATE_SCHEMA:
        raise ValueError("unsupported or non-canonical certificate record")
    string_fields = keys - {"assumptions", "cases", "schema"}
    if any(type(item[field]) is not str or not item[field] for field in string_fields):
        raise ValueError("certificate identifiers must be nonempty strings")
    assumptions = item["assumptions"]
    cases = item["cases"]
    if type(assumptions) is not list or any(type(value) is not str for value in assumptions):
        raise ValueError("certificate assumptions must be a list of strings")
    if type(cases) is not list:
        raise ValueError("certificate cases must be a list")
    decoded_cases: list[CertifiedCase] = []
    for raw in cases:
        if type(raw) is not dict or set(raw) != {"context", "peer", "safe"}:
            raise ValueError("malformed certified case")
        if type(raw["context"]) is not str or type(raw["peer"]) is not str:
            raise ValueError("certified case names must be strings")
        if type(raw["safe"]) is not bool:
            raise ValueError("certified case safety must be bool")
        decoded_cases.append(CertifiedCase(raw["context"], raw["peer"], raw["safe"]))
    return UpdateCertificate(
        source_version=item["source_version"],
        target_version=item["target_version"],
        source_digest=item["source_digest"],
        target_digest=item["target_digest"],
        checker_id=item["checker_id"],
        model_id=item["model_id"],
        limit_rule_id=item["limit_rule_id"],
        authorization_id=item["authorization_id"],
        invariant_id=item["invariant_id"],
        authorized_by=item["authorized_by"],
        assumptions=tuple(assumptions),
        cases=tuple(decoded_cases),
        claim=item["claim"],
    )


def make_certificate(
    state: SystemState,
    proposal: Configuration,
    *,
    authorized_by: str,
) -> UpdateCertificate:
    cases = tuple(
        CertifiedCase(context, peer, not proposal.case(context, peer).forbidden)
        for context, peer in product(
            state.will.contextual_adaptation.environments, state.will.coherence_relations.peers
        )
    )
    return UpdateCertificate(
        source_version=state.configuration.version,
        target_version=proposal.version,
        source_digest=configuration_digest(state.configuration),
        target_digest=configuration_digest(proposal),
        checker_id=state.configuration.checker_id,
        model_id=state.configuration.model_id,
        limit_rule_id=state.configuration.limit_rule_id,
        authorization_id=state.configuration.authorization_id,
        invariant_id=state.configuration.invariant_id,
        authorized_by=authorized_by,
        assumptions=("closed-environment-enumeration", "policy-table-is-complete"),
        cases=cases,
    )


def check_update(
    state: SystemState,
    proposal: Configuration,
    encoded: bytes,
    *,
    case_budget: int,
) -> CheckResult:
    """Validate arbitrary bytes under the pre-update trusted contract."""
    try:
        certificate = decode_certificate(encoded)
    except (TypeError, ValueError) as error:
        return CheckResult(Decision.REJECTED, f"malformed certificate: {error}")
    current = state.configuration
    exact = {
        "source_version": current.version,
        "target_version": proposal.version,
        "source_digest": configuration_digest(current),
        "target_digest": configuration_digest(proposal),
        "checker_id": current.checker_id,
        "model_id": current.model_id,
        "limit_rule_id": current.limit_rule_id,
        "authorization_id": current.authorization_id,
        "invariant_id": current.invariant_id,
        "claim": "installation-and-all-declared-transitions-preserve-no-forbidden-effect",
    }
    for field, expected in exact.items():
        if getattr(certificate, field) != expected:
            return CheckResult(Decision.REJECTED, f"certificate does not bind {field}")
    proposed_contract = (
        proposal.checker_id,
        proposal.model_id,
        proposal.limit_rule_id,
        proposal.authorization_id,
        proposal.invariant_id,
    )
    current_contract = (
        current.checker_id,
        current.model_id,
        current.limit_rule_id,
        current.authorization_id,
        current.invariant_id,
    )
    if proposed_contract != current_contract:
        return CheckResult(
            Decision.REJECTED,
            "trusted-contract migration is outside this fragment and lacks old-contract evidence",
        )
    if certificate.authorized_by not in state.authorities:
        return CheckResult(Decision.REJECTED, "proposal lacks current governance authorization")
    expected_keys = set(product(
        state.will.contextual_adaptation.environments, state.will.coherence_relations.peers
    ))
    if case_budget < len(expected_keys):
        return CheckResult(Decision.UNKNOWN, "case budget exhausted before exhaustive checking")
    if len(certificate.cases) != len(expected_keys):
        return CheckResult(Decision.REJECTED, "certificate case coverage is incomplete")
    actual_keys = {(case.context, case.peer) for case in certificate.cases}
    if actual_keys != expected_keys or len(actual_keys) != len(certificate.cases):
        return CheckResult(Decision.REJECTED, "certificate cases do not exactly cover the model")
    for case in certificate.cases:
        actual_safe = not proposal.case(case.context, case.peer).forbidden
        if case.safe != actual_safe:
            return CheckResult(Decision.REJECTED, "certificate case result is forged")
        if not actual_safe:
            return CheckResult(
                Decision.REJECTED,
                f"counterexample at context={case.context}, peer={case.peer}",
            )
    return CheckResult(Decision.ACCEPTED, "exact proposal is safe over the declared finite model")


def _contract(configuration: Configuration) -> tuple[str, str, str, str, str]:
    return (
        configuration.checker_id,
        configuration.model_id,
        configuration.limit_rule_id,
        configuration.authorization_id,
        configuration.invariant_id,
    )


def _lean_version(configuration: Configuration) -> str | None:
    unsafe = any(case.forbidden for case in configuration.policy)
    if unsafe:
        return "bad"
    if configuration.version in {"v1", "v2"}:
        return configuration.version
    return None


def verified_check_update(
    state: SystemState,
    proposal: Configuration,
    encoded: bytes,
    *,
    case_budget: int,
    checker: VerifiedChecker,
) -> CheckResult:
    """Require both exact host decoding/binding and the pinned Lean evaluator.

    Only the closed ``v1``/``v2``/``bad`` fragment is mapped.  The canonical
    Python decoder and this mapping remain trusted adapter code; acceptance is
    nevertheless impossible unless the exact pinned Lean binary returns
    ``ACCEPTED`` on every supplied checker field.
    """
    binding = checker.validate_binding()
    if binding.decision is not Decision.ACCEPTED:
        return binding
    preliminary = check_update(state, proposal, encoded, case_budget=case_budget)
    if preliminary.decision is not Decision.ACCEPTED:
        return preliminary
    try:
        certificate = decode_certificate(encoded)
    except (TypeError, ValueError) as error:  # defensive: preliminary already decoded it
        return CheckResult(Decision.REJECTED, f"malformed certificate: {error}")

    current_token = _lean_version(state.configuration)
    candidate_token = _lean_version(proposal)
    if current_token is None or candidate_token is None:
        return CheckResult(Decision.UNKNOWN, "version is outside the verified Lean fragment")

    current_contract = "trusted" if _contract(state.configuration) == checker.expected_contract else "other"
    candidate_contract = "trusted" if _contract(proposal) == checker.expected_contract else "other"
    certificate_contract = "trusted" if (
        certificate.checker_id,
        certificate.model_id,
        certificate.limit_rule_id,
        certificate.authorization_id,
        certificate.invariant_id,
    ) == checker.expected_contract else "other"
    certificate_source = current_token if (
        certificate.source_version == state.configuration.version
        and certificate.source_digest == configuration_digest(state.configuration)
    ) else ("v2" if current_token == "v1" else "v1")
    certificate_target = candidate_token if (
        certificate.target_version == proposal.version
    ) else ("v2" if candidate_token == "v1" else "v1")
    certificate_digest = candidate_token if (
        certificate.target_digest == configuration_digest(proposal)
    ) else ("v2" if candidate_token == "v1" else "v1")
    authorized = certificate.authorized_by in state.authorities
    all_cases_safe = all(case.safe for case in certificate.cases)

    command = [
        str(checker.executable),
        current_token,
        candidate_token,
        str(case_budget),
        "record",
        certificate_source,
        certificate_target,
        certificate_digest,
        certificate_contract,
        str(authorized).lower(),
        str(len(certificate.cases)),
        str(all_cases_safe).lower(),
        candidate_contract,
        current_contract,
    ]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=checker.timeout_seconds,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return CheckResult(Decision.UNKNOWN, f"verified checker unavailable: {error}")
    output = completed.stdout.strip()
    if completed.returncode != 0 or output not in {item.value for item in Decision}:
        return CheckResult(
            Decision.UNKNOWN,
            f"verified checker protocol failure: exit={completed.returncode}, output={output!r}",
        )
    decision = Decision(output)
    return CheckResult(decision, f"{checker.binding_id}; Lean evaluator returned {decision.value}")


def propose(state: SystemState, proposal: Configuration) -> SystemState:
    return replace(
        state,
        evidence=state.evidence + (f"PROPOSED:{proposal.version}:{configuration_digest(proposal)}",),
    )


def install(
    state: SystemState,
    proposal: Configuration,
    encoded: bytes,
    *,
    case_budget: int,
) -> tuple[SystemState, CheckResult]:
    """Legacy finite analysis path; use :func:`verified_install` operationally."""
    if state.recovery is not None:
        return state, CheckResult(Decision.REJECTED, "installation is disabled during recovery")
    result = check_update(state, proposal, encoded, case_budget=case_budget)
    event = f"INSTALL-{result.decision.value}:{proposal.version}:{result.reason}"
    if not result.authorizes:
        return replace(state, evidence=state.evidence + (event,)), result
    installed = replace(state, configuration=proposal, evidence=state.evidence + (event,))
    if not invariant(installed):
        raise AssertionError("a successful installation must preserve the invariant")
    return installed, result


def verified_install(
    state: SystemState,
    proposal: Configuration,
    encoded: bytes,
    *,
    case_budget: int,
    checker: VerifiedChecker,
) -> tuple[SystemState, CheckResult]:
    """The operational installation path gated by the exact pinned Lean binary."""
    if state.recovery is not None:
        return state, CheckResult(Decision.REJECTED, "installation is disabled during recovery")
    result = verified_check_update(
        state,
        proposal,
        encoded,
        case_budget=case_budget,
        checker=checker,
    )
    event = f"VERIFIED-INSTALL-{result.decision.value}:{proposal.version}:{result.reason}"
    if not result.authorizes:
        return replace(state, evidence=state.evidence + (event,)), result
    installed = replace(state, configuration=proposal, evidence=state.evidence + (event,))
    if not invariant(installed):
        raise AssertionError("a verified installation must preserve the invariant")
    return installed, result


def environment_step(state: SystemState, context: str) -> SystemState:
    if context not in state.will.contextual_adaptation.environments:
        raise ValueError("environment context is outside the modeled adaptation set")
    if state.recovery is not None:
        if state.recovery.environment_step_used:
            raise RuntimeError("the scheduling contract now requires a recovery step")
        episode = replace(state.recovery, environment_step_used=True)
        return replace(
            state,
            context=context,
            recovery=episode,
            evidence=state.evidence + (f"RECOVERY-ENV:{context}",),
        )
    return replace(state, context=context, evidence=state.evidence + (f"ENV:{context}",))


def relational_step(state: SystemState, peer: str) -> SystemState:
    if state.recovery is not None:
        raise RuntimeError("relational/ordinary steps are disabled during recovery")
    if peer not in state.will.coherence_relations.peers:
        raise ValueError("peer is outside the modeled relational set")
    return replace(state, peer=peer, evidence=state.evidence + (f"PEER:{peer}",))


def ordinary_step(state: SystemState) -> SystemState:
    if state.recovery is not None:
        raise RuntimeError("ordinary steps are disabled during recovery")
    case = state.configuration.case(state.context, state.peer)
    effect = Effect(
        case.effect, case.forbidden, state.configuration.version, state.context, state.peer
    )
    result = replace(
        state,
        operational_state="b" if state.operational_state == "a" else state.operational_state,
        persistent_effects=state.persistent_effects + (effect,),
        evidence=state.evidence + (f"EFFECT:{effect.name}:{effect.forbidden}",),
    )
    if not invariant(result):
        raise RuntimeError("modeled policy attempted a forbidden observable effect")
    return result


def begin_recovery(state: SystemState, certificate: RecoveryCertificate) -> SystemState:
    checked = verify_recovery_certificate(certificate)
    if not checked.authorizes:
        raise ValueError(checked.reason)
    if state.operational_state == certificate.goal:
        return state
    episode = RecoveryEpisode(state.operational_state, certificate)
    return replace(state, recovery=episode, evidence=state.evidence + ("RECOVERY-BEGIN",))


def recovery_step(state: SystemState, kernel_name: str) -> SystemState:
    if state.recovery is None:
        raise RuntimeError("no active recovery episode")
    certificate = state.recovery.certificate
    checked = verify_recovery_certificate(certificate)
    if not checked.authorizes:
        raise RuntimeError("recovery certificate no longer validates")
    kernels = {kernel.name: kernel for kernel in certificate.kernels}
    if kernel_name not in kernels:
        raise ValueError("kernel is not permitted by the recovery certificate")
    before = state.recovery.control_state
    target = kernels[kernel_name].next(before)
    if before != certificate.goal and not certificate.rank(target) < certificate.rank(before):
        raise RuntimeError("recovery move does not strictly decrease the common rank")
    if target == certificate.goal:
        return replace(
            state,
            operational_state=target,
            recovery=None,
            evidence=state.evidence + (f"RECOVERY:{kernel_name}:{before}->{target}",),
        )
    episode = RecoveryEpisode(target, certificate, environment_step_used=False)
    return replace(
        state,
        operational_state=target,
        recovery=episode,
        evidence=state.evidence + (f"RECOVERY:{kernel_name}:{before}->{target}",),
    )


@dataclass(frozen=True, slots=True)
class OperationalCheckpoint:
    operational_state: str
    context: str
    peer: str


def checkpoint(state: SystemState) -> OperationalCheckpoint:
    return OperationalCheckpoint(state.operational_state, state.context, state.peer)


def rollback(state: SystemState, saved: OperationalCheckpoint) -> SystemState:
    """Restore only reversible operational data; effects and evidence remain."""
    return replace(
        state,
        operational_state=saved.operational_state,
        context=saved.context,
        peer=saved.peer,
        evidence=state.evidence + ("ROLLBACK-OPERATIONAL-ONLY",),
        recovery=None,
    )


@dataclass(frozen=True, slots=True)
class AbstractState:
    safe: bool
    recovering: bool
    version: str


def abstract(state: SystemState) -> AbstractState:
    return AbstractState(invariant(state), state.recovery is not None, state.configuration.version)


def forward_simulates(before: SystemState, after: SystemState) -> bool:
    """The selected abstraction preserves the stable property and version observation."""
    source, target = abstract(before), abstract(after)
    return (not source.safe or target.safe) and (
        source.version == target.version or any(
            item.startswith("INSTALL-ACCEPTED") for item in after.evidence[len(before.evidence):]
        )
    )


def composition_safe(component_impacts: Iterable[int], shared_budget: int) -> bool:
    impacts = tuple(component_impacts)
    if any(type(item) is not int or item < 0 for item in impacts):
        raise ValueError("component impacts must be nonnegative integers")
    return sum(impacts) <= shared_budget


def pairwise_without_joint_solution() -> bool:
    """Return the finite countermodel: three pairwise disequalities over Bool."""
    constraints = (
        lambda x, y, z: x != y,
        lambda x, y, z: y != z,
        lambda x, y, z: x != z,
    )
    assignments = tuple(product((False, True), repeat=3))
    pairwise = all(any(left(a, b, c) and right(a, b, c) for a, b, c in assignments)
                   for left, right in ((constraints[0], constraints[1]),
                                       (constraints[0], constraints[2]),
                                       (constraints[1], constraints[2])))
    joint = any(all(rule(a, b, c) for rule in constraints) for a, b, c in assignments)
    return pairwise and not joint


def demo_model(checker: VerifiedChecker | None = None) -> dict[str, object]:
    """Run accepted/rejected updates, interaction, and recovery.

    Passing ``checker`` selects the operational path and makes the pinned Lean
    evaluator a necessary condition of installation.  Omitting it retains the
    earlier finite analysis demonstration for compatibility and never relabels
    that path as verified.
    """
    will = AppliedWill(
        ("baseline-observed",),
        "deliberate",
        "avoid-forbidden-effect",
        INVARIANT_ID,
        AdaptationDomain(
            ("dry", "wet"),
            ("attention", "fatigue"),
            ("consent", "support"),
            ("immediate", "episode"),
        ),
        CoherenceDomain(
            ("human", "peer-agent"),
            ("past-verifies-present", "invariant-constrains-adaptation"),
        ),
    )
    contract = checker.expected_contract if checker is not None else (
        "finite-table-checker/v1",
        "two-context-two-peer/v1",
        "no-limit-transition/v1",
        "hyperethics-governance/v1",
        INVARIANT_ID,
    )
    common = dict(
        checker_id=contract[0],
        model_id=contract[1],
        limit_rule_id=contract[2],
        authorization_id=contract[3],
        invariant_id=contract[4],
    )
    v1 = Configuration(
        "v1",
        tuple(PolicyCase(context, peer, "observe", False)
              for context, peer in product(
                  will.contextual_adaptation.environments, will.coherence_relations.peers
              )),
        **common,
    )
    state = SystemState(v1, will, "dry", "human", frozenset({"council"}), "a")
    v2 = Configuration(
        "v2",
        tuple(PolicyCase(context, peer, "assist", False)
              for context, peer in product(
                  will.contextual_adaptation.environments, will.coherence_relations.peers
              )),
        **common,
    )
    bad = Configuration(
        "v-bad",
        tuple(PolicyCase(context, peer, "spill", context == "wet")
              for context, peer in product(
                  will.contextual_adaptation.environments, will.coherence_relations.peers
              )),
        **common,
    )
    state = propose(state, v2)
    certificate = encode_certificate(make_certificate(state, v2, authorized_by="council"))
    if checker is None:
        state, accepted = install(state, v2, certificate, case_budget=4)
    else:
        state, accepted = verified_install(
            state, v2, certificate, case_budget=4, checker=checker
        )
    state = environment_step(state, "wet")
    state = relational_step(state, "peer-agent")
    state = ordinary_step(state)
    state = propose(state, bad)
    bad_certificate = encode_certificate(make_certificate(state, bad, authorized_by="council"))
    if checker is None:
        state, rejected = install(state, bad, bad_certificate, case_budget=4)
    else:
        state, rejected = verified_install(
            state, bad, bad_certificate, case_budget=4, checker=checker
        )
    kernel = RecoveryKernel("K1", (("a", "b"), ("b", "g"), ("g", "g")))
    recovery_certificate = RecoveryCertificate(
        "g", (kernel,), (("a", RecoveryRank(1, 0)), ("b", RecoveryRank(0, 7)),
                         ("g", RecoveryRank(0, 0))),
    )
    state = replace(state, operational_state="a")
    state = begin_recovery(state, recovery_certificate)
    state = environment_step(state, "dry")
    state = recovery_step(state, "K1")
    state = environment_step(state, "wet")
    state = recovery_step(state, "K1")
    return {
        "accepted_update": accepted.decision.value,
        "rejected_update": rejected.decision.value,
        "final_version": state.configuration.version,
        "final_control_state": state.operational_state,
        "recovery_complete": state.recovery is None,
        "invariant": invariant(state),
        "will_components": len(state.will.operational_view()),
        "effects": [effect.name for effect in state.persistent_effects],
        "evidence": list(state.evidence),
        "installation_path": "PINNED_LEAN" if checker is not None else "PYTHON_ANALYSIS_ONLY",
        "checker_binding": checker.binding_id if checker is not None else None,
    }


def main() -> None:
    """Print the deterministic demonstration receipt as canonical JSON."""
    print(json.dumps(demo_model(), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
