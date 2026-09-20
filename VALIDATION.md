# Local validation receipt

Date: 2026-09-19. Status: initial implementation validated for the bounded
claims below; native self-derivation and the complete research target remain open.

## Coordinates

- Repository `metamathethicology`. The validation run below was performed on a
  local checkout at branch `codex/ordinatics-first` with no commit and no remote.
  Those exact validated bytes were subsequently committed unchanged to branch
  `main` and pushed to the private repository `TimeLordRaps/metamathethicology`.
  Publication does not extend the receipt: it records where the validated bytes
  now live, not any additional check performed after the run.
- Python 3.12.8 on Windows, pytest 8.3.5, pytest-timeout 2.4.0.
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
`31c3c83cced376070e4af0d4b31ed6760967d5a15a5bf6bbaf04d1414be13d76`.
This manifest identifies tested bytes; it does not sign or independently certify them.

## Observed checks

```console
python -m pytest tests -vv -s --durations=10 --timeout=30
python -m ruff check src tests
python -m metamathethicology
python -m build --no-isolation
```

- 42 tests passed with zero skips against exported source pins, installed public
  dependencies, and the installed wheel. The wheel run disabled the source-tree
  import path (`-o pythonpath=`) and confirmed that the import resolved inside
  the virtual environment's installed package directory.
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
- Existing Hypermath and Ordinatics calculi were inspected but not edited. Their
  full suites were outside this change; integration tests cover only the listed
  imported operations, not those projects' complete correctness. Those broader
  dependency sweeps and the other Python-version runs are classified
  `PERFORMANCE_OR_DURATION_EXCLUSION`; this receipt covers the stated runtime.

The host checker trusts Python, its dependencies, and ordinary in-process object
integrity. Decoding validates submitted representations, but arbitrary code with
permission to mutate the running interpreter is outside the trust model. Bridge
bases and assumption provenance are declarations; their truth is not certified.
