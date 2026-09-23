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

## Combination fields

A **combination field** is a submodule that combines two fields this package does
not depend on. `metamathethicology.will_electrophysics` is the first one, and it
exists because of a placement its author states directly:

> Electricity hyperphysics should go in hyperphysics, underlying will foundations
> in hyperethics, and then their combination field of will electrophysics is in
> metamathethicology.

Neither parent can host it. [`hyperphysics`](https://github.com/TimeLordRaps/hyperphysics)
states electrical law and knows nothing of will;
[`hyperethics`](https://github.com/TimeLordRaps/hyperethics) states what a will is
and is a foundation that stands on the standard library alone. The transport
between them is a cross-domain inference, and `Rule` refuses to construct one
without a named bridge. What a foundation could only document, this field enforces.

```python
from metamathethicology import close, replay
from metamathethicology.will_electrophysics import electrophysics_space

space = electrophysics_space()
derived = replay(space, close(space))
assert sum(1 for j in derived if j.predicate == "termformed") == 4
assert any(j.predicate == "will-balance" for j in derived)

# The transport rests on an adopted licence, not a derived one. Delete it and
# every will conclusion goes with it. Nothing false is derived either way; that
# difference is the entire content of the borrowing.
bare = electrophysics_space(include_licence=False)
assert not any(j.predicate == "termformed" for j in replay(bare, close(bare)))
```

Neither cited package is a declared dependency, so a combination field does not
force a physics package and a foundation into every install.
`tests/test_citations.py` holds both citations to the exact bytes of the source
whenever those packages happen to be importable, and skips loudly when they are
not. **A skip means the citations were not checked on that run**, which is a
different outcome from checking them and passing; `VALIDATION.md` records which
of the two happened.

The layer specification is [`will_electrophysics.hm`](will_electrophysics.hm).
It carries no layer index on purpose: stages are this package's index, and
asserting a second indexing scheme over material that already has one would put
the two in conflict. Soundness of the transport is **NOT ESTABLISHED**, and
`hyperphysics` records that no criterion for establishing it exists. Two of the
six graduation criteria are discharged.

`metamathethicology.oreality` is the second combination field, and its second
parent is a declaration rather than a package:

> And also then this allows for us in metamathethicology through ordinatics to
> define the Oreality, we already should have Areality (Abstraction reality where
> abstract thoughts exist), Oreality springs out from Areality (might actually use
> spring like hyperphysical equations), then also Preality (Possibility reality)
> [holds 5+dimensional objects like the block multiverse]. Our reality is the 4D
> projection of possibility reality through our coherent projections of Areality
> hyperprobabilistically through Oreality.

The mathematical parent is
[`hyperprobability`](https://github.com/TimeLordRaps/hyperprobability). It
states contained universes, the law at every ordinal stage below ω^ω, strange
loops, the least stage that guarantees an event, and the Kac bridge. No
published source states the realms, so the declaration itself is the referent:
every realm quotes it verbatim, and `Realm` refuses a fragment it does not
contain. Under an adopted licence the four realms are read as follows:

- Areality through its coherent projections, which are contained presentations
  whose coherence is checked when they are built;
- Preality as the support graphs and the transfinite runs they allow;
- Oreality as the ordinal-staged law;
- our reality as the in-universe law.

```python
from metamathethicology import close, replay
from metamathethicology.oreality import (
    oreality_space,
    our_reality_does_not_fix_oreality,
    possibility_does_not_fix_our_reality,
)

space = oreality_space()
read = [j for j in replay(space, close(space)) if j.predicate == "realm-reading"]
assert [j.arguments[0] for j in read] == ["Areality", "Preality", "Oreality", "our reality"]

# Two claims the declaration might seem to license are refuted by countermodel.
loop, collapsed = our_reality_does_not_fix_oreality()  # one in_uni; guarantees ω and ∞
fair, biased = possibility_does_not_fix_our_reality()  # one guarantee; frequencies 1/2, 1/3

# As before, the readings rest on the licence, and deleting it deletes them.
assert not close(oreality_space(include_licence=False)).steps
```

Four things are held back on purpose:

- The reading of the O as Ordinal is PROPOSED, not declared, and nothing rests
  on it.
- The dimension counts are preserved and read by nothing, because
  hyperprobability has no dimensions.
- The spring is OPEN. A series-RLC candidate from `hyperphysics` is recorded with
  its citation and four reasons it is not adopted, and no rule takes it as a
  premise.
- Our reality is read as a law, not as one realized run. The reading that was
  passed over is kept.

`tests/test_oreality_citations.py` holds the citations to their sources under the
same skip rule. Each heading, quote, code name and recorded value is checked
against hyperprobability's SPEC and package, and the spring candidate against
`hyperphysics`. The layer specification is [`oreality.hm`](oreality.hm). Two of
its seven graduation criteria are discharged.

## Relation to the proposed libraries

| Surface | Present implementation | Next mathematical obligation |
|---|---|---|
| `ordinatics` | Actual dependency for every stage and ordinal comparison | Broader ordinal notation requires its own sound ordering and semantics |
| `grounded-hypercalculi` | Integration tests exercise language proofs, permutation groups, and exact rational arithmetic | Typed substitutions, disjoint-variable conditions, and proof transport need separate contracts |
| `grounded-hyperset-theory` | Integration tests exercise cyclic graph bisimulation and a refuting graph | Preserve relation witnesses across logical translations; structural self-reference is not truth |
| `grounded-hyperphysics` | Extension contract in [DESIGN.md](DESIGN.md); `will_electrophysics` cites [`hyperphysics`](https://github.com/TimeLordRaps/hyperphysics) laws by name and is held to their exact bytes | Metaphysical definitions, physical dimensions, observables, empirical interpretation |
| `grounded-hyperethics` | A conditional normative inference example, plus `will_electrophysics` transporting electrical form onto the [`hyperethics`](https://github.com/TimeLordRaps/hyperethics) will tensor under a declared, deletable licence | Explicit ethical theories, conflicts, scope, and justified descriptive-to-normative bridges; a soundness criterion for any such transport |
| `grounded-hyperlogic` | Finite rule replay and strictly staged reflection in the common core | Native proof transport from hypersets, hypercalculus, language calculus, and real analysis |
| `hypermath` | Research ancestor; no new native bridge is claimed | Derive representation, execution, and checking from native operations |

The three proposed `grounded-hyper*` projects are **not separately implemented
libraries**. Their common operation-space substrate is implemented here; the
extension contracts retain the intended ancestry without duplicating engines.

`hyperphysics` and `hyperethics` are separate existing packages and are **not**
the proposed `grounded-hyperphysics` and `grounded-hyperethics`. They are cited
by name, never imported, and never restated. A combination field over them
instantiates the relevant extension contract without claiming to discharge it.

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

**No preprint exists for this repository**, and none is drafted. That is
recorded so a reader can tell "not yet" from "not needed": novelty and
native adequacy are unestablished, and they are what a manuscript would
have to argue.

See [DESIGN.md](DESIGN.md) for the exact target distinctions and
[VALIDATION.md](VALIDATION.md) for the local validation coordinate and exclusions.
Novelty, native adequacy, unrestricted self-verification, and completeness remain
unestablished. Code license: [Apache License 2.0](LICENSE).
