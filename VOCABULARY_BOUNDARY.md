# Vocabulary boundary: ten words the corpus already disagrees about

Written 2026-09-21. This is a combination statement — it is about more than one
field at once — so it lives here rather than in any single field, per the
placement rule that a field states its own subject once.

It answers a question that was asked about one repository and returned an answer
about all of them.

## The question, and the answer

`hyperstratum` (public, 9 commits, all 2026-04-25) proposes ~24 terms and
declares itself the upstream ontology for this family. It was to be adopted
**only** if it could be supported holistically, with pros and no cons, and
without weighting the assessment toward adopting.

**Zero terms clear that bar. Adopt nothing.**

The closest miss is worth naming so the judgement can be checked: `mira-`
(representation-from-a-position) is the one coinage pointing at something
English has no single word for. Its cons are that the formal apparatus already
exists as agent-indexed epistemic models, and that its own grammar collapses
(below). Under the bar as stated it is a reject; under a relaxed bar it would be
an operator `mira_p(G)`, not a prefix, and informal-notes-only.

## The part that outlives the question

Even if `hyperstratum` is deleted tomorrow, **ten words in this corpus already
carry conflicting senses across repositories.** (Six were found by the
hyperstratum audit; four more were found later, and are in the second table.) This is a live hazard with no
dependency on whether anything is adopted.

Measured 2026-09-21 by counting files per repository:

| word | hyperstratum | formal-universality | hypergrammar | hypermath |
|---|---|---|---|---|
| `hyperfield` | 4 | **2** | 0 | 0 |
| `hypertopology` | 4 | **5** | **8** | 0 |
| `hyperstructure` | 4 | **16** | **92** | 2 |
| `hypernode` | 8 | 0 | **2** | 0 |

And the senses genuinely differ:

- **`Form`** — `formal-universality/reasoning/dictionary/Form.txt` is
  **`Status: LOCKED after creation`** and its "WHAT IT IS NOT" section says
  *"Not a shape or geometric figure. Structure here means: generated-by-apply."*
  That sentence rules out "identifiable structure" explicitly. Verified by
  reading the file.
- **`Frame` / `FRAME`** — in this family FRAME is a *closure-status label*: an
  articulated derivation block with a named forward dependency and a discharge
  layer. It is not an aperture, an opening, or a point of view. Every `.hm`
  layer in the family already uses it in the closure sense.
- **`hyperstructure`** — 92 files in `hypergrammar`, with Vougiouklis cited in
  3 of them: it is the Hv-structure of algebraic hyperstructure theory
  (Marty 1934, Vougiouklis 1994).
- **`hyperfield`** — `formal-universality/reasoning/term_formation/` holds the
  2x3 hyperfield pair; the literature holds the Krasner hyperfield (1956) and
  Baker-Bowler matroids over hyperfields.
- **`hypertopology`** — three repositories, three senses, and a fourth in the
  literature (hyperspace topologies: Vietoris, Fell, Wijsman).
- **`hypernode`** — a Mermaid-diagram dataclass in `hypergrammar`; and in the
  literature, Poulovassilis & Levene's nested-graph node (ACM TOIS 12(1), 1994).

`Form` and `Frame` are the acute pair: both are load-bearing here, and both
appear in hyperstratum's first five definitions.

## The prefix convention is the root cause

`hyper-` is used in **two incompatible ways** inside one author's corpus.

- In `hypergrammar` and the literature it cites, `hyper-` means
  **arity-raised / multi-valued** — one input, a nonempty class as output.
  That is hyperoperation, hypergraph, hyperstructure, hyperfield.
- In `hyperstratum`, `hyper-` means **recursive across levels**.

Both cannot be canonical. Every `hyper*` term inherits this as a con before any
other con is counted. **The family's own convention is the arity-raising one**,
because it is the one with published mathematics behind it and the one already
used across 92 files.

## The avoidance discipline was applied once and backfired

`hyperstratum` avoids `hypergraph` because it is taken, then coins
`recursive-graph` — which is also taken, in computability theory, for a graph
with decidable vertex and edge relations. Meanwhile the same check was not run
on `hypertopology`, `hypermanifold`, `hyperfield`, `hyperstructure`, or
`hypernode`, all of which are taken. The abstention is also unilateral:
`hypergrammar` uses `hypergraph` freely and correctly.

Lesson, generally applicable: **run the collision check on every coinage or on
none.** Running it on one term produces false confidence about the rest.

## The prefix grammar collapses, and its own consumer proved it

`self-` / `mira-` / `recursive-` are declared as three non-collapsing prefixes.
They are not three dimensions. If `Reality` is defined as a slice seen *from
within a frame* — as hyperstratum defines it — then representation is always
positioned, so `mira-` is the default rather than a modifier, and `self-` is
`mira_p` with p = x. One parameter at two values.

`recursive-` is genuinely orthogonal (depth, not index), and `recursive-` is the
one that is taken.

The empirical confirmation is that the grammar's only consumer already
re-derived the collapse. `force-of-will-formalism/docs/formalism.md` line 360
reads, in full:

> self-mira-graph and social-mira-graph

It drops `recursive-` — which occurs **zero** times in that file — and uses
`self-`/`social-` as *arguments to* `mira-` rather than as co-equal prefixes,
which is exactly what `hyperstratum/docs/03-graph-prefix-grammar.md` says must
not happen. `social-` is not in the declared prefix set at all. That file also
never names `hyperstratum`, so the collapse was not a disagreement with the
grammar; the only user re-derived a different structure without consulting it.

Verified against the repository on GitHub 2026-09-21 (the tree is not local).

## The upstream claim does not hold

`hyperstratum`'s README names four downstream frameworks. Verified by grep
2026-09-21:

| claimed downstream | files mentioning "hyperstratum" |
|---|---|
| `hypergrammar` | **0** |
| `formal-universality` | **0** |
| `taxonomy-of-deception` | **0** |
| `force-of-will-formalism` | **1**, in the README only |

Three of four are false, and the fourth is a see-also rather than an import.
`docs/glossary.md` mentions `hyperstratum` zero times while **re-defining**
`Hypernode` on its own terms ("a local recursive agency-node that can be modeled
through the six-will structure"), and README line 70 says outright: *"This repo
stands on its own."*

An upstream ontology that nothing imports is a con by itself. An upstream
ontology whose siblings use six of its words to mean other things is a larger
one.

## What already does this work, better

For every concept hyperstratum names, this family already has a term with a
signature or an axiom attached:

| concept | hyperstratum | what the family already uses |
|---|---|---|
| level of a stack | `base` / `meta` | `layer` (`:: Nat -> Set(Form)`) + `orbital` |
| closure of identity | `Hyperform` | `form-closure` (`:: Form -> Prop`) |
| what a form carries | `Hyperfield` | `substance` (`:: Form -> Prop`, `ax-sub-nec`) |
| reachability | `Hyperconnection`/`Hyperrelation` | `derives` (directional, finite chain) |
| representation | `Meta`, `Hyperrepresentation` | `syntax`/`substance`/`semantics` with three axioms |
| degrees of sameness | seven unordered "nearnesses" | `~~` / `=~` / `==`, an ordered filtration |

The right-hand column states *when* something holds. The left-hand column does
not: "closed or closing" is satisfied by every hyperstructure, and
`Hyperemergent` has no stabilization criterion, so nothing can fail to be one.

That is this family's own standard, applied to a candidate vocabulary:
**a constraint that cannot fail is not being checked.**

## What in hyperstratum is worth keeping

Two things, neither of them vocabulary:

1. **"Reception is not identity."** A real claim with real literature behind it
   — Cooley's looking-glass self (1902), Tajfel & Turner on personal vs. social
   identity.
2. **The six-will structure**, which already lives in `force-of-will-formalism`
   and does not need hyperstratum to state it.

## Provenance

`hyperstratum` was cloned read-only to assess it. Nothing was pushed to it and
nothing was copied out of it. The file counts above were measured directly in
this repository's sibling trees on 2026-09-21 and can be re-measured.

## Four more, found after the hyperstratum audit (2026-09-21)

The first six came out of assessing a candidate vocabulary. These four came out
of ordinary work, which is the more worrying provenance: they were not found by
looking for collisions.

Measured 2026-09-21, files per repository.

| word | hypermath | hyperlogic | hyperethics | metamathethicology | hyperphysics |
|---|---|---|---|---|---|
| `shadow` | **63** | **42** | **50** | 14 | 2 |
| `mirror` | **76** | **39** | **40** | 7 | 0 |
| `frame` (lowercase) | **51** | 2 | 6 | 4 | — |
| `anchor` | **7** | 0 | 0 | 0 | — |

**7. `frame`** — `Frame`/`FRAME` was already listed above in its closure-status
sense. The lowercase word is a *second* problem: in PPL "base frames" means the
component constraint sets of a joint problem, which is neither the closure label
nor a point of view. 51 hypermath files use it.

**8. `anchor`** — the acute one, because it is multivalent **inside a single
repository**. hypermath already uses it for at least four different things: an
external commit/seal anchor, a name anchor (First Form), a relation-level anchor
(syntax), and `W-anchor` as one of the three W-forms. The religion work's
"anchor point" (a dominator in a tradition graph) would be a fifth, and it is
not related to any of the four. **Do not adopt "anchor point" without renaming.**

**9/10. `shadow` and `mirror`** — the highest-traffic words on this page, and
the only ones with a **user-declared** sense. `definitional_shadow.hm:44` quotes
Tyler directly:

> hyperphysics self-derivational chain is a mirror of hypermaths, and
> hyperethics is a shadow of hypermaths

Two further senses exist already. I introduced `ShadowForm` in the P0 layers
myself, which is a third. PPL's `SHADOW_PARADOX`/`MIRROR_PARADOX`
(`satisfaction-suffices/logic/cycle_detector.py`) are a fourth. **Importing
PPL's names would therefore be a fourth sense of a word that already has a
declared one** — so the recommendation to adopt them is withdrawn. Refer to the
lattice states by their bit codes (`010`, `011`) or qualify them explicitly as
PPL verdicts.

One observation worth keeping, flagged rather than asserted: the *contrast axis*
is the same in all four senses. A mirror is faithful and a shadow is a lossy
projection, and in PPL the mirror state converges while the shadow state does
not. That may be a genuine structural echo — a shadow really is a projection
that loses a dimension — or it may be English connotation doing the work twice.
It is not currently checked either way. See `paradox_lattice_tower.hm`.

## Running total

Ten words, and the trend is the point: the first six were found by auditing a
vocabulary proposal, the last four by tripping over them. The corpus has no
collision check of its own, so the count is a lower bound.

## `symmetric` / `asymmetric` — measured 2026-09-21, and NOT words 11 and 12

Tyler's 2026-09-21 abstraction promotes `shadow` and `mirror` to species of
`asymmetric form` and `symmetric form`. That put two new words on the critical
path, so they were censused before adoption, the same way words 7–10 were.

| word | hypermath | hyperethics | metamathethicology | hyperlogic | hyperphysics |
|---|---|---|---|---|---|
| `symmetr*` | **38** | 14 | 4 | 3 | 0 |
| `asymmetr*` | 16 | 13 | 2 | 2 | 0 |

*(files mentioning; each field's own tree, `references/` and `.git/` excluded)*

**On the count alone these are the worst collision in the file** — 38 files in
hypermath against `shadow`'s 63 and `mirror`'s 76, but concentrated in the one
repo the whole shadow relation is measured against. I was ready to rule them
taken.

**Reading the sense inverts the verdict, and that is the entry worth keeping.**
hypermath uses `symmetric` in exactly the relation-theoretic sense the
abstraction needs, and *discharges it as proof*:

- `L0:541` — "The derives relation is not symmetric."
- `L0:57` — `derive similar-symmetric as FORM:` … x ~~ y → y ~~ x
- `L1:476` — `derive(derives-is-directional)` — derives asymmetric. FORM. Discharges L0-40.
- `L2:430` — `abstracted-path-is-reflexive-and-symmetric` — ~= is reflexive and symmetric on DerivationPath.

hyperethics uses the same abstract sense on different objects (proof asymmetry,
the bridge asymmetry, the two-register asymmetry). **One sense, five repos.**

So these are **the first words this file has measured that came back clean** —
high frequency, single sense, already load-bearing, already proved. Adopting
them is *reuse*, not overloading, and they do not become words 11 and 12. The
ten stand.

**METHOD NOTE, which is why this section exists at all.** Words 7–10 were
caught by counting. These two would have been *mis*-caught by counting: the
count is the detection step and it said COLLISION; reading six lines of source
said REUSE. A frequency census can tell you a word is worth checking. It can
never tell you a word is taken. Every future entry here needs the sense read
before the verdict is written — including, retroactively, the ten above, of
which only `frame` and `anchor` have had their senses read line-by-line.
