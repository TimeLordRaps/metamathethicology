# Local validation receipt

Date: 2026-09-20, extended 2026-09-23. Status: the initial implementation and
two combination fields, `will_electrophysics` and `oreality`, are validated for
the bounded claims below. Native self-derivation, the soundness of any transport
or reading, and the complete research target remain open.

This receipt extends the one dated 2026-09-19 rather than replacing it. The
42-test core is unchanged and its wheel and build passes are not repeated here;
the 100 tests added for the combination field were exercised in the source tree
only, and the boundary between the two is stated explicitly under Observed
checks.

## Coordinates

- Repository `metamathethicology`. The validation run below was performed on a
  local checkout at branch `codex/ordinatics-first` with no commit and no remote.
  Those exact validated bytes were subsequently committed unchanged to branch
  `main` and pushed to the private repository `TimeLordRaps/metamathethicology`.
  Publication does not extend the receipt: it records where the validated bytes
  now live, not any additional check performed after the run. The 2026-09-20 pass
  was performed on branch `main` of that checkout before commit, and those exact
  bytes were then committed and pushed unchanged. The same limit applies: the
  push records where they live and is not a further check.
- Python 3.12.8 on Windows. The 2026-09-19 pass used pytest 8.3.5 with
  pytest-timeout 2.4.0. The 2026-09-20 pass used pytest 9.1.1 and ruff 0.16.8
  from an adjacent virtual environment that has no `pytest-timeout`, so it ran
  with `-o addopts=""` and **the project's `--timeout=30` was not in force on
  that pass**. Every test in it completed in well under a second, but the guard
  itself was absent, and that is a difference from the earlier configuration
  rather than a detail.
- The 2026-09-23 pass ran in a separate Git worktree on branch `feat/oreality`,
  created from `b48f580`, before commit. It used Python 3.12.8, pytest 8.3.5 and
  pytest-timeout from the base interpreter the virtual environment inherits, and
  ruff 0.16.8. It ran with the project's own options, so **`--timeout=30` was in
  force on that pass**.
- `hyperphysics` and `hyperethics` are **not** dependencies, pinned or otherwise.
  They are cited by name and cross-checked only when importable. For the citation
  pass they were put on `PYTHONPATH` from adjacent working checkouts, which is a
  weaker coordinate than a Git pin, since those checkouts carried uncommitted
  work at the time of the run. The cross-check therefore establishes agreement
  with the bytes described in those repositories' own receipts of the same date,
  and nothing about any published release of either.
- For the 2026-09-23 pass the cited packages were again put on `PYTHONPATH` from
  adjacent checkouts. The table gives their coordinates. The first two identify
  the imported bytes by Git commit. The third does not: the `will_electrophysics`
  citation checks passed against a `hyperethics` working tree that no commit
  records.

  | Cited package | Commit | Working tree |
  |---|---|---|
  | [hyperprobability](https://github.com/TimeLordRaps/hyperprobability) | `cb1b169d1d3c320b687a1c495bc43824c4ae2c65`, branch `feat/hyperprobability-0.1`, not merged | clean |
  | [hyperphysics](https://github.com/TimeLordRaps/hyperphysics) | `ec9a9a25fdb5a840363e9fa416ac1ac27a900ef9`, `main` | `src/` clean; three uncommitted files outside it, none importable |
  | [hyperethics](https://github.com/TimeLordRaps/hyperethics) | `f64a3b2247b0bf59d37600d5058076a470f7faad`, branch `l4-consent` | uncommitted changes inside `src/` |
- Public source dependencies were exported from the exact commits below for the
  first test pass, then independently fetched and installed from those Git
  revisions for the installed-dependency pass. Existing uncommitted changes in
  adjacent checkouts were not imported as dependency source.

| Dependency | Public Git commit |
|---|---|
| [Ordinatics](https://github.com/TimeLordRaps/ordinatics) | `1564656fc5a740b595c018e96b904781954a85c8` |
| [Grounded Hypercalculi](https://github.com/TimeLordRaps/grounded-hypercalculi) | `e3fd9f803d11b355b257fb7c8270bec414827930` |
| [Grounded Hyperset Theory](https://github.com/TimeLordRaps/grounded-hyperset-theory) | `0e1d836dba07975ce6319ab459ec88ab53564e3a` |

These are Git source coordinates, not claims about current package-index releases.
Changing these revisions, the package source, the runtime, or the representation
schema invalidates this receipt as evidence for the changed configuration.

The tested implementation, tests, and package configuration are byte-bound in
[`validation/source-manifest.json`](validation/source-manifest.json). The digest
of its canonical `files` mapping is
`98fe3b786db087e3b1a9d02231e5a370f150dafb8279b32cbd44c56cc76195be`. It was
`558a4e94710722986e761cfa43677d0c863f3ba6b98ca9456d7da875e28f6871` before line
304 of `will_electrophysics.hm` was corrected from nine inherited failure modes
to the fourteen that `hyperphysics` computes at `ec9a9a2`. Only that file's
entry differs. It was
`c94eaf9241369a45c501cbed25f16fc8a7a18c965c57b4952a1d85247a52419b` when the
second combination field was first committed, before two docstrings in
`oreality.py` were corrected to say what is published rather than what is
committed. It was
`7de4f373c19a106fcc2ecb7b3d0e891e7fce6adb50245bdc3f37391f748f158e` after the
first combination field was added, and
`31c3c83cced376070e4af0d4b31ed6760967d5a15a5bf6bbaf04d1414be13d76` before it.
Since 2026-09-23 every entry is the SHA-256 of the file's LF-normalized bytes,
the form Git stores. The Oreality section below says why the first combination
field's digest is superseded rather than extended.
This manifest identifies tested bytes; it does not sign or independently certify them.

## Observed checks

```console
python -m pytest tests -vv -s --durations=10 --timeout=30
python -m ruff check src tests
python -m metamathethicology
python -m build --no-isolation
```

- **2026-09-19, the core.** 42 tests passed with zero skips against exported
  source pins, installed public dependencies, and the installed wheel. The wheel
  run disabled the source-tree import path (`-o pythonpath=`) and confirmed that
  the import resolved inside the virtual environment's installed package
  directory. Those 42 tests are unchanged and are included in both counts below.
- **2026-09-20, the combination field. The suite was run in two configurations
  and both are reported here.**
  - With neither cited package importable: **116 passed, 1 skipped.** The skip is
    the whole of `tests/test_citations.py`, which requires both `hyperphysics`
    and `hyperethics`. A skip means the citations were NOT checked on that run;
    it does not mean they were checked and passed.
  - With both on the path: **142 passed, zero skips.** The citation cross-checks
    executed. This is the run the combination-field claims below rest on.
  - Lint passed with no findings on both.
- **The 2026-09-20 pass did not repeat the wheel and build runs.** The earlier
  result stands for the bytes it covered and is not extended to the 100 tests
  added since; those were exercised in the source tree only. Nothing here
  establishes that the new module packages or installs correctly.
- **2026-09-23, the second combination field. The suite was run in three
  configurations, all with `--timeout=30` in force, and all three are reported
  here.**
  - With no cited package importable: **213 passed, 70 skipped.** The skips are
    `tests/test_citations.py`, skipped as one module, and the 69 checks in
    `tests/test_oreality_citations.py`.
  - With `hyperprobability` and `hyperphysics` on the path: **282 passed, 1
    skipped.** Every Oreality citation check executed. The skip is
    `tests/test_citations.py`, which also needs `hyperethics`.
  - With all three on the path: **308 passed, zero skips.**
  - The rootdir was the worktree, and `metamathethicology.oreality` imported. That
    module exists only in the worktree, so the package under test was the
    worktree's and not the adjacent checkout's.
  - Lint passed with no findings. Every Python block in `README.md` was executed
    and ran. The wheel and build runs were not repeated.
- The closure oracle independently enumerates every closed superset of a small
  presented theory, then intersects them. All 16 starting assumption sets agree
  with closure/replay. This is bounded test evidence, not a general machine proof.
- Negative cases reject unsupported cycles, absent norms, silent domain transfers,
  downward stage rules, same-stage reflection, wrong definitions, future/reordered
  premises, ambiguous/malformed encodings, and false premise indices.
- Round trips preserve exact definitions and both accepted and rejected traces.
- The integration tests call actual bounded satisfaction, literal proof checking,
  graph bisimulation, finite group closure, and exact rational arithmetic.
- Lint passed. The executable demonstration reports its stronger targets UNKNOWN
  or NOT_ESTABLISHED. Source archive and wheel builds succeeded using setuptools
  84.0.0. Build success does not establish release readiness or reproducibility.

### Will electrophysics, the combination field

- **The licence is load-bearing, and that is checked rather than asserted.**
  `electrophysics_space()` derives four termformed will terms and one
  will-balance. `electrophysics_space(include_licence=False)` derives **zero** of
  either. Nothing false is derived without the licence; nothing about will is
  derived at all. That difference is the whole content of the borrowing, and it
  is the same structure `deliberation_space(include_norm=False)` shows for a
  descriptive-to-normative step.
- **Every rule crosses a domain boundary and every one names a bridge.** All five
  cross METAPHYSICS into METAETHICS, and `Rule` raises on a bridgeless crossing,
  so a termformer that disclaimed nothing could not be turned into a rule and the
  space would fail to construct. A test builds such a termformer and asserts the
  failure rather than trusting the invariant.
- **The closing step is itself a borrowing and says so.** Summing the three
  series drops is Kirchhoff's voltage law, carried as a fifth termformer with its
  own citation and its own disclaimer, not as a bare algebraic move.
- **The self-induced drop is asserted absent from the balance's premises.** It is
  a constituent of the self-simulation equation, not of the series form.
- **The balance lands a stage later than the terms it closes**, so the closure is
  a derivation step and not an identification.
- **An exhausted budget is UNKNOWN rather than false**, and reflection requires a
  strictly later stage. Both are checked on this space, not only on the core ones.
- **Every citation is checked character for character** when both cited packages
  are importable: every cited law exists in `hyperphysics`; every quoted form
  equals the source's exactly; all four series constituents are borrowed,
  including the one that closes them; the declared departure on capacitance is a
  parameter the source really leaves free; and the five borrowings are built into
  real `hyperphysics.Transport` objects and put through that package's own
  `validate` and `audit`.
- **The cited will tensor is checked against `hyperethics`.** The six components
  and the three roles are exactly the ones it declares, every correspondence
  gives a component the role `hyperethics.role_of` gives it, and the temporal
  chain agrees with the one it orders. `Correspondence` rejects a component or
  role the foundation does not declare, so the combination cannot grow a will of
  its own between releases.
- **The split is checked in both directions.** `is_true_moral_operator` and
  `WillProfile` are asserted absent from this module, and `hyperethics.will` is
  asserted to contain no termformer and no correspondence.
- **One universal claim is refuted conclusively.** That a different invariant
  will entails a different resonant rate: under the reciprocal law `C(L) = 6/L`,
  invariants 2 and 3 share the rate `1/sqrt(6)`. One countermodel settles a
  universal claim, so this does not depend on how many cases agreed.
- **The binding of constant will to the invariant is enforced by type.**
  `resonant_rate` and `damping_ratio` reject a loose pair of numbers with
  `TypeError`, so an invariant cannot be paired with a capacity that is not its
  own.
- **Every termformer is asserted to disclaim a unit or a mechanism**, and the
  self-induced drop is additionally asserted to refuse the cosmological claim:
  the transport does not assert that any universe is a simulation.
- The superseded capacitance readings are asserted to be kept rather than erased,
  because a resolution is only informative against what it ruled out.

### Oreality, the second combination field

- **Every reading rests on the licence, and that is checked rather than
  asserted.** `oreality_space()` derives four realm readings: Areality and
  Preality at omega+1, Oreality at omega+2 and our reality at omega+3.
  `oreality_space(include_licence=False)` takes zero steps. Nothing false is
  derived without the licence, and nothing about any realm is derived at all.
- **Every rule crosses METAMATH into METAPHYSICS and names a bridge.** Each
  bridge is built from its realm's citation and disclaimer. A test builds a
  reading rule with no bridge and asserts that `Rule` refuses it.
- **The declaration is held verbatim.** Each realm's fragment is asserted to
  occur in it. A paraphrase, an undeclared realm and a realm that arises from
  itself are each refused at construction.
- **The O's expansion is asserted to carry no weight.** It is labelled
  PROPOSED, and no judgment in the space mentions it.
- **Every citation is checked against hyperprobability's SPEC and package.** All
  14 headings, with their claim labels, occur exactly once. Every quotation
  occurs inside the result it is cited from, and every cited code name resolves.
- **Every recorded value is what the package computes**, for all seven
  presentations: the in-universe law, frequency, hyperprobability and strange
  loops.
  - For every presentation, collapsing every attractor makes the law at omega
    equal the recorded in-universe law (Proposition 2.7(c)).
  - The three Kac records match, including tightness. The clock is tight at 2;
    the coins, at omega, are not.
  - Proposition 4.9 is exercised on the coins over four event and start pairs,
    and Corollary 5.3 on the four witnesses without strange loops.
  - Theorem 5.2 is exercised on LOOP: all the mass that arrives at omega arrives
    through the loop on {a, b}.
  - `hyperprobability` refuses a limit key that is not an attractor. That is the
    one coherence check `Presentation` leaves to it.
- **Two universal claims are refuted conclusively.**
  - That our reality fixes Oreality: LOOP and its collapse share an in-universe
    law, and their guarantees are omega and infinity.
  - That possibility fixes our reality: the fair and biased coins share every
    support and every guarantee, and their frequencies are 1/2 and 1/3.

  Each refutation re-checks its witnesses when called. For each, a test
  substitutes a witness that has lost its shape and asserts that the refutation
  raises instead of passing vacuously.
- **The spring stays OPEN and is checked only as a candidate.**
  - The quoted form equals the `hyperphysics` series-rlc form exactly.
  - `hyperphysics.validate` accepts the candidate's shape as a transport.
  - Adopting it would inherit 14 failure modes: 3 of the law's own and 11 from
    its four constituents, as `inherited_failure_modes` computes them.

  No rule in the space takes a spring premise.
- **The manifest is corrected, not extended.**
  - The 2026-09-20 manifest recorded three entries as SHA-256 digests of CRLF
    bytes: `__init__.py`, `examples.py` and `will_electrophysics.py`. The
    repository stores those files with LF, because `.gitattributes` sets
    `eol=lf`, and the other eleven entries are digests of LF bytes.
  - Converting each committed file to CRLF reproduces the three recorded digests
    exactly. The tested bytes therefore differed from the committed ones in line
    endings only.
  - Every entry is now the digest of the file's LF-normalized bytes, the form
    Git stores.
  - `__init__.py` also changed on 2026-09-23. The new digest identifies
    different bytes by construction and certifies nothing about the old ones.

## Adjacent foundational repair

Grounded Hypercalculi, `main` at `e3fd9f803d11b355b257fb7c8270bec414827930`,
had pre-existing uncommitted work. The new change affects only
`src/grounded_hypercalculi/ordinal_calculus.py` and a new
`tests/test_ordinal_inputs.py`.

The ordinal constructor and finite constructor now reject negative, boolean,
floating, string, and fractional inputs while canonicalizing exact integer
protocol values. Before the patch, 15 of the 16 new tests failed; afterward
all 85 targeted and adjacent checks passed. The full current-working-tree
suite passed **255 tests**, with zero skips, under:

```console
python -m pytest tests -vv -s --durations=10 --timeout=60
python scripts/check_presentation.py
```

The presentation gate and a standard-library-only ordinal import/arithmetic
check passed. The changed tracked file passes `git diff --check`. The full
working-tree whitespace check reports three existing end-of-file blank-line
warnings in unrelated files. Hashes of all seven pre-existing modified tracked
files were identical before and after this work; their edits were preserved.
No library version was changed, and the patch was neither committed nor pushed.
The new project's public dependency pin therefore does not include this local
ordinal repair; its own ranks use Ordinatics directly.

## Exclusions and remaining obligations

- `OS_CAPABILITY_GUARD`: Linux/macOS runtime execution and cross-platform build
  comparison were not run on this Windows host.
- `PERFORMANCE_OR_DURATION_EXCLUSION`: Large resource-stress runs, arbitrary-size
  adversarial inputs, and exhaustive checking of all possible theories were not
  run. Budgets constrain defined inspection steps, not all runtime costs.
- `EXTERNAL_SERVICE_BOUNDARY`: Remote continuous-integration execution, release
  publication, and package-index installation were not performed. Installation
  from the pinned public Git sources was performed.
- No proof-assistant theorem, source-native adequacy proof, empirical physics
  validation, or ethical soundness proof exists for this new calculus. These are
  **unimplemented research obligations**, not skipped passing tests.
- **The soundness of the will transport is not established, and no criterion for
  establishing it exists.** `hyperphysics` records that absence as its own
  `GC-4`. Every will conclusion in `electrophysics_space` rests on an adopted
  licence, and the space is built so that deleting the licence deletes the
  conclusions rather than leaving them standing on something unstated. That the
  declaration is enforced is checked; that the declaration is true is not.
- **That `d-self-simulation` reproduces `hyperethics`' independently derived
  `d-no-exterior` is evidence, not warrant.** Two layers stated without reference
  to each other arriving at "no exterior vantage" is the strongest thing in hand,
  and it is still an agreement rather than a derivation. The user's own statement
  of the transport says "metaphorically analogize" and "somehow"; nothing in this
  repository is more confident than its source.
- **No will quantity has units or an empirical reading.** The numeric functions
  take dimensionless magnitudes and measure nothing. Passing them numbers does
  not make a will measurable, and `UNITS_DO_NOT_TRANSPORT` is the standing rule
  on both sides of the borrowing.
- **The charge-constant law is open.** Constant will is declared to be the
  invariant's constant of charge, which binds it without fixing the map. Every
  result is stated for an arbitrary such function; results depending on a
  particular one are not available and are not claimed.
- **The stage indices of the transport are a convention.** omega, omega+1 and
  omega+2 order availability: a formed term is available only after the law and
  the component it was formed from. No argument is offered that omega is the
  right starting stage for a transport, and these ranks are not time, energy,
  utility, or a measure of how far the transport has been justified.
- **A combination field inherits both parents' open obligations.** `hyperethics`
  records the seam between its layers, its declared role division, the normative
  force of `norm-inhabits`, and the **Universal Consistency Self-Maintenance
  Paradox** as open. Citing a foundation does not discharge that foundation's
  obligations, and a combination cannot be sounder than either side of it.
- **No realm reading is established, and `hyperprobability` defines no realm.**
  Every reading in `oreality_space` rests on an adopted licence. That the licence
  is load-bearing is checked; that any reading is true of its realm is not. The
  SPEC labels its own readings of the user's phrases INTERPRETATION.
- **`hyperprobability`'s results are cited, not re-proved.** Its SPEC says that
  no proof in it is machine-checked, and the cited commit is on a branch that
  has not been merged. The witnesses exhibit its theorems on seven finite
  presentations. They do not prove them, although each of the two refutations
  is conclusive because one countermodel settles a universal claim.
- **The dimension counts, the O's expansion and the spring are unread.** "4D" and
  "5+dimensional" are preserved and attach to nothing, because
  `hyperprobability` has no dimensions. The expansion of the O is PROPOSED, and
  no spring law is adopted.
- **The stage indices of the readings are a convention.** They order when each
  reading becomes available. They do not rank the realms, and they are not time.
- **Other statements of reality kinds are not reconciled.** `oreality.hm` records
  two such points as open rather than resolving them: another expansion the user
  has given for Areality, and a reality-kinds layer drafted for `hyperethics`
  that states no order and no projection. Two of the field's seven graduation
  criteria are discharged.
- Existing Hypermath and Ordinatics calculi were inspected but not edited. Their
  full suites were outside this change; integration tests cover only the listed
  imported operations, not those projects' complete correctness. Those broader
  dependency sweeps and the other Python-version runs are classified
  `PERFORMANCE_OR_DURATION_EXCLUSION`; this receipt covers the stated runtime.

The host checker trusts Python, its dependencies, and ordinary in-process object
integrity. Decoding validates submitted representations, but arbitrary code with
permission to mutate the running interpreter is outside the trust model. Bridge
bases and assumption provenance are declarations; their truth is not certified.

**No preprint exists for this repository**, none is drafted, and no check
here bears on one. A combination field's manuscript would have to argue for
the combination itself, and this receipt establishes nothing about it.
