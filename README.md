# Metamathethicology

An **experimental local foundation** for Tyler Roost's proposed combination of
**metamath, metaphysics, metaethics, and metalogic**. The spelling
`metamathethicology` is intentional. In this project, `metamath` names the
metamathematical component; compatibility with the separate **Metamath** proof
language is limited to an integration example using the existing literal fragment.

The research target is **truly self-representable, self-definable, self-closing,
self-verifiable self-derivation of the lower-order subjects from transfinite
beginnings**. This implementation provides explicit, testable stepping stones.
It does **not** claim that this target has been achieved.

## Implemented operation space

- Exact Ordinatics stages `omega <= alpha < omega**omega`; omega is the first
  infinite ordinal. These are dimensionless language/operation ranks, not time,
  energy, utility, or other physical quantities.
- Four separate domain tags; equal words across domains do not become equal claims.
- Finite, variable-free inference rules with ordered premises and explicit bases.
- Rules preserve or increase stages; reflection requires a strictly later stage.
- Finite least positive rule closure, with budget exhaustion reported as UNKNOWN
  through an exception. An absent derivation is not a false proposition.
- Replay against the exact operation-space definition, including premises,
  justifications, and cross-domain bridge declarations.
- Recoverable definitions and proof traces in JavaScript Object Notation (JSON).
  Secure Hash Algorithm 256-bit (SHA-256) digests bind their canonical bytes.
  Digests are dimensionless identifiers; they do not establish truth or authority.

"Ground rule" means **variable-free** in this implementation. It is not a claim
that the rule was generated from Hypermath's native ground primitive.

## Try it

Requires Python 3.10 or newer and Git. From this checkout:

```console
python -m pip install '.[dev,ecosystem]'
python -m metamathethicology
python -m pytest tests -vv -s --durations=10 --timeout=30
```

Dependencies are pinned to specific public Git commits in `pyproject.toml`.
The ordinary install needs Ordinatics; the optional `ecosystem` extra adds the
two grounded libraries for the integration tests. The complete test command
requires that extra and fails visibly if it is absent.

```python
from ordinatics.ordinals import OMEGA, ONE
from metamathethicology import close, decode_space, encode_space, reflect, replay
from metamathethicology.examples import deliberation_space

space = deliberation_space()
proof = close(space)
assert decode_space(encode_space(space)) == space
assert space.rules[0].conclusion in replay(space, proof)

record = reflect(space, proof, space.rules[0].conclusion, at=OMEGA + ONE + ONE)
assert record.predicate == "derivable-in"

# Without the explicitly declared norm, the ethical conclusion is underived.
without_norm = deliberation_space(include_norm=False)
assert without_norm.rules[0].conclusion not in replay(without_norm, close(without_norm))
```

The example uses a toy norm as an explicit assumption. It neither selects an
ethical theory nor establishes physical, metaphysical, or moral truth.

## Relation to the proposed libraries

| Surface | Present implementation | Next mathematical obligation |
|---|---|---|
| `ordinatics` | Actual dependency for every stage and ordinal comparison | Broader ordinal notation requires its own sound ordering and semantics |
| `grounded-hypercalculi` | Integration tests exercise language proofs, permutation groups, and exact rational arithmetic | Typed substitutions, disjoint-variable conditions, and proof transport need separate contracts |
| `grounded-hyperset-theory` | Integration tests exercise cyclic graph bisimulation and a refuting graph | Preserve relation witnesses across logical translations; structural self-reference is not truth |
| `grounded-hyperphysics` | Proposed extension described in [DESIGN.md](DESIGN.md) | Metaphysical definitions, physical dimensions, observables, empirical interpretation |
| `grounded-hyperethics` | A conditional normative inference example in the common operation-space language | Explicit ethical theories, conflicts, scope, and justified descriptive-to-normative bridges |
| `grounded-hyperlogic` | Finite rule replay and strictly staged reflection in the common core | Native proof transport from hypersets, hypercalculus, language calculus, and real analysis |
| `hypermath` | Research ancestor; no new native bridge is claimed | Derive representation, execution, and checking from native operations |

The three proposed `grounded-hyper*` projects are **not separately implemented
libraries**. Their common operation-space substrate is implemented here; the
extension contracts retain the intended ancestry without duplicating engines.

## Boundaries and evidence

Finite rule closure at a transfinite index does not perform infinitely many
operations or define a complete truth predicate. A checked reflection says only
that a particular trace is derivable in a specified presented theory. The
checker, parser, ordinal arithmetic, and Python runtime remain external trusted
infrastructure. Supplying a bridge justification is not a proof of its soundness.

Self-representation and reflection are distinct from Gödelian completeness and
Tarski definability. Ordinal progressions have an established research lineage;
see Feferman's primary account, [Turing's Thesis](https://math.stanford.edu/~feferman/papers/turing.pdf).
The separate [Metamath project](https://us.metamath.org/) checks proofs relative
to specified axioms; this package does not implement its full language.

See [DESIGN.md](DESIGN.md) for the exact target distinctions and
[VALIDATION.md](VALIDATION.md) for the local validation coordinate and exclusions.
Novelty, native adequacy, unrestricted self-verification, and completeness remain
unestablished. Code license: [Apache License 2.0](LICENSE).
