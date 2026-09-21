# Local validation receipt

Date: 2026-09-20. Status: the initial implementation and the first combination
field, `will_electrophysics`, are validated for the bounded claims below. Native
self-derivation, the soundness of any transport, and the complete research target
remain open.

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
- `hyperphysics` and `hyperethics` are **not** dependencies, pinned or otherwise.
  They are cited by name and cross-checked only when importable. For the citation
  pass they were put on `PYTHONPATH` from adjacent working checkouts, which is a
  weaker coordinate than a Git pin, since those checkouts carried uncommitted
  work at the time of the run. The cross-check therefore establishes agreement
  with the bytes described in those repositories' own receipts of the same date,
  and nothing about any published release of either.
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
`7de4f373c19a106fcc2ecb7b3d0e891e7fce6adb50245bdc3f37391f748f158e`, and was
`31c3c83cced376070e4af0d4b31ed6760967d5a15a5bf6bbaf04d1414be13d76` before the
combination field was added.
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
