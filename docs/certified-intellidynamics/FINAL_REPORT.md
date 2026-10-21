# Certified intellidynamics implementation report

## Result

The selected finite fragment is implemented, demonstrated, mechanically proved,
and bound to signed local commits. It is not a proof of general native Hypermath
closure, physical safety, moral legitimacy, unrestricted synthesis, or arbitrary
Python/Lean equivalence.

The original shared checkouts were inspected but not modified. Work was performed
in isolated `codex/certified-intellidynamics` worktrees. The five unpublished
Hyperfield candidates and the private Force-of-Will source were read in place and
not copied, rewritten, published, or changed.

## Delivered by target

| Target | Delivered result | Status |
|---|---|---|
| A | A compiled Lean checker over arbitrary parsed `Wire` values; exact binding of source/target/trusted contract; malformed rejection; unsafe rejection; budget `UNKNOWN`; required CI replay | `PROVED` for the Lean fragment |
| B | Separate environment, proposal, ordinary, checked-installation, and recovery transitions; stable no-forbidden-effect property; one-step, reachability, and arbitrary finite-prefix preservation | `PROVED` for the formal fragment; richer Python instance exhaustively checked |
| C | Well-founded lexicographic `omega*k+n` rank; common-rank checker; K1 termination; K1/K2 switching loop refuted; environment interleaving bounded by an explicit scheduling contract | `PROVED` under the modeled scheduler; no real-time deadline |
| D | One-way concrete-to-abstract forward simulation and safety transfer; shared-budget composition premise; path-loss and unsafe composition counterexamples | `PROVED` for the selected relation; native `==` identification `UNKNOWN` |
| E | Exhaustive finite proposal checking with `ACCEPTED`/`REJECTED`/`UNKNOWN`; unknown cannot authorize; operational-only rollback retaining effects/evidence; pairwise-without-joint counterexample | `PROVED` or checked as named; unrestricted synthesis excluded |

The executable demonstration contains two configuration versions plus one unsafe
proposal, all six will components, environmental and timescale adaptation,
self/social adaptation, relations among components and to a human/peer agent, a
nontrivial accepted update, a rejected unsafe update, an emitted safe effect, and
a completed recovery episode from `a` through `b` to `g`.

## Upstream repairs

- Ordinatics no longer guesses limit values or reports convergence after a failed
  callback. Finite prefixes are not extrapolated to `omega`; nested Veblen terms
  now keep equality and hashing aligned.
- Grounded Hypercalculi modus ponens now requires both premises to be proved
  assertions; a `wff` typing judgment cannot prove a proposition or falsehood.
- Grounded Hyperset Theory rejects overlapping partition blocks and uses tagged
  singleton blocks so a node identifier cannot collide with a user block.
- Hypermath's Python proof/certificate path now binds endpoints, named semantic
  validators, essential hypotheses, disjoint variables, prior theorem order, and
  exact polynomial evaluation.
- Hyperethics exposes distinct typed owner and operational will views with an
  explicit `ADOPTED_INTERFACE` concordance.

## Mechanically checked closure

The Lean module imports only `Std`, not Hypermath L0--L3. `#print axioms` reports:

- no axioms for step/reachability/prefix preservation, rank well-foundedness,
  switching rejection, abstraction, property transfer, or composition;
- `propext` and `Quot.sound` for certificate and common-rank Boolean normalization;
- `propext` for the two concrete common-descent proofs;
- no `sorryAx` or project-specific assertion in the claimed target closure.

The whole Hypermath library still builds with eleven explicit `sorry` declarations
in L0--L3. Those declarations are outside this target closure and remain a named
`BLOCKED_SOURCE` obligation. A successful whole-library build is not presented as
their proof.

## Verification summary

- Ordinatics: 516 passed.
- Grounded Hyperset Theory: 563 passed.
- Grounded Hypercalculi: 257 passed.
- Hyperethics: 399 passed; source manifest regenerated.
- Hypermath Python, isolated with declared `verifier-standard==1.4.0`: 423 passed,
  6 skipped. The skips are the existing external translator checks requiring
  `HM_LEAN` or `HM_MMVERIFY`; the selected Lean module was built and audited
  separately, while the external Metamath target remains unrun.
- Hypermath Lean 4.14.0: library, certified executable, theorem audit, and four
  executable outcomes passed.
- Metamathethicology: 148 passed, 1 skipped. The skip is the existing optional
  Hyperphysics citation check; Hyperphysics is not a premise of the selected
  fragment.
- Metamathethicology wheel and source distribution built successfully.
- Ruff passed on the full changed Hypermath, Hyperethics, and Metamathethicology
  surfaces and on the changed Ordinatics/Hyperset files. Existing unrelated lint
  debt remains in Grounded Hypercalculi and other untouched test files.

The machine-readable receipt records tool versions, exact commands, hashes, and
the initial global Hypermath dependency mismatch that motivated the isolated run.

## Remaining boundaries

1. Arbitrary Python execution is not formally refined to the Lean evaluator. The
   compiled Lean checker is authoritative for the formal fragment; the CLI parser
   and process boundary remain trusted.
2. The finite environment has two contexts and two peers. Unlisted observations,
   malicious sensors, physical dynamics, and open-world coverage remain external.
3. The recovery theorem assumes at most one environment step between required
   recovery steps; authority, installation, relational, and ordinary mutation are
   disabled during recovery.
4. No explicit limit transition is admitted by the demonstration. Safe finite
   prefixes therefore do not establish an unmodeled stage at `omega`.
5. The owner coherence functional remains proposed. Coherence is not moral
   legitimacy and does not imply the selected effect constraint.
6. Native `==`, `=~`, `~~`, and `~=` adequacy and the broader local Hyperfield
   candidates' all-path obligations remain outside the proved fragment.
7. The commits are local signed candidates. Nothing was pushed, released,
   deployed, or published.
