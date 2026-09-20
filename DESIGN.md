# Mathematical contract and research ancestry

Status: proposed research architecture plus an implemented finite reference
calculus. Date: 2026-09-20. This is not a proof of the full research program.

## Transfinite beginnings

Every operation-space stage is an actual `ordinatics.ordinals.Ordinal`, beginning
at omega and strictly below omega**omega. Finite arithmetic can be an object of
such a language without being the indexing foundation. No integer label is
silently promoted to an ordinal, and no floating infinity substitutes for one.

A judgment is `(domain, predicate, arguments, alpha)`. It has no physical unit;
its alpha is a dimensionless availability rank. A space has ceiling lambda,
explicit assumptions A, and a finite ordered rule list R. All judgments must
have ranks at most lambda. Every rule must have a conclusion rank at least as
large as each premise rank. Cross-domain rules need a declared bridge basis.
Increasing the space ceiling does not relabel judgments or create premises.

At a limit ceiling such as omega**2, the engine still consumes a **finite supplied
presentation**. It does not infer an infinite union, a cofinal family, or a limit
theorem from a finite sample. General transfinite recursion and limit-stage
closure need a separate, source-adequate semantics before implementation.

## Exact finite calculus

Let C0 = A and let C(n+1) add the conclusion of every rule whose premises are
already in C(n). These are finite iterations at a fixed ordinal stage ceiling;
n counts engine passes and is not a replacement for the ordinal language rank.
Since the only possible additions are the finite list of rule conclusions,
saturation terminates in at most as many additions as distinct conclusions.

`close` implements an ordered, in-place version of this monotone construction.
Each accepted step cites earlier context positions and its named rule. By
induction on the trace, replayed conclusions follow from A under R. A final
pass without additions is closed under R. The resulting set is contained in
every R-closed superset of A, hence is its least positive closure. This is a
mathematical argument for this finite calculus, not a proof-assistant theorem
about the Python implementation. The tests compare it with the intersection
of all closed supersets in an independently enumerated finite example.

Premise repetition and order are retained. Rules do not consume premises, so
this is not linear logic. There is no variable substitution, quantification,
negation-as-failure, contradiction resolution, or logical explosion rule.
`not-p` would merely be another uninterpreted predicate. Typed domain tags do
not establish that user-provided axioms are consistent or sound.

The budget charges assumption/rule counts and rule/premise inspections. It
does not bound integer/string bit complexity, construction cost, or canonical
serialization. Encoded documents have a one-mebibyte limit. Callers need an
external process limit for hostile in-memory objects or resource isolation.

## The five target distinctions

| User's target | Implemented foothold | Stronger unresolved obligation |
|---|---|---|
| Self-representable | Complete space and trace representations recover exactly through the host codec | A representation derived and interpreted inside the native object language |
| Self-definable | Assumptions, rules, domain boundaries, and stage ranks have explicit recoverable definitions | Internal definitions with an adequacy theorem for their native interpretation |
| Self-closing | Least finite positive closure under explicitly supplied rules | Native generation and appropriate transfinite/limit closure for richer subjects |
| Self-verifiable | An external checker replays retained proof steps; later-stage reflection binds that replay | Internal checker realization, a soundness theorem, and a precisely limited reflection principle |
| Self-derivation | Derived judgments retain their exact premise ancestry | Source-native derivation of the generating/checking machinery and lower-order subjects |

No implemented foothold is silently identified with the full target. The
research phrase "closest thing to Gödelian completeness and Tarski definability"
is a motivation, not a theorem or a comparative novelty claim.

`reflect` replays a lower-space proof and creates a later-stage `derivable-in`
judgment bound to the full space, trace, and chosen conclusion. Its strict
inequality is checked even at limit ordinals. It is not an unrestricted truth
schema. Manually constructing a similarly named atom proves nothing: assumptions
and rules remain declarations, and actual replay is the acceptance mechanism.

## Domain extensions, with their requested ancestry preserved

### Grounded hyperphysics

Base on Grounded Hypercalculi, with Ordinatics stages from the start. First
define a typed vocabulary for entities, states, relations, grounding, modality,
and observables. These proposed metaphysics definitions need declared model
semantics. Physical quantities require dimensions and units in addition to
logical ranks; neither ontology nor ordinal stage is a measurement. Use exact
real-analysis representations where available and distinguish finite numerical
screens from convergence proofs. An empirical law needs observation evidence
beyond a syntactic derivation. None of this is supplied by the toy ontology tag.

`will_electrophysics` exercises the citation half of this contract without
claiming the rest of it. It names five laws in `hyperphysics`, quotes each
form, and is held to those exact bytes by `tests/test_citations.py`. It supplies
no dimensions, no units, and no observables: `UNITS_DO_NOT_TRANSPORT` is the
standing rule on both sides, and every borrowed term declines a specific unit or
mechanism of the law it cites. A transport that declines nothing specific has
declined nothing.

### Grounded hyperethics

Base on the Grounded Hypercalculi language calculus and extend it through explicit
typing and proof obligations. Keep descriptive propositions, adopted norms,
obligations, permissions, and theory-relative judgments distinct. A declared
bridge must explain why its descriptive premises license its normative
conclusion within the selected theory. Conflict-sensitive consequence and
scope must be formalized before adding inconsistent norm sets. The initial
example only implements a conditional implication under one stipulated norm.

`will_electrophysics` implements the bridge requirement rather than describing
it. Every rule there crosses METAPHYSICS into METAETHICS, so `Rule` refuses to
construct any of them without a named bridge, and each bridge is assembled from
its termformer's own citation and disclaimer. A termformer that disclaimed
nothing could not become a rule and the space would fail to build. What that
buys is narrow and worth stating exactly: the declaration is enforced, the
declaration's truth is not. See the next section.

### Combination fields

A combination field is a submodule that combines two fields this package does not
depend on. It is placed here rather than in either parent, and the reason is
structural rather than editorial: a field that states a law cannot also state
what borrows the law without becoming the borrower, and a foundation that had to
cite another field to say what its own subject matter is would not be a
foundation. The combination is a third thing, and it belongs where cross-domain
inference is already a checked notion.

`will_electrophysics` is the first, following a placement its author states
directly: electricity hyperphysics in `hyperphysics`, the will foundation in
`hyperethics`, the combination in this package. It carries four constraints that
any later combination field should carry too.

1. **Cite, do not restate.** A law is stated once, in the field that owns it, and
   quoted here by name. A disclaimer of the form "this does not transport farads"
   needs a fixed referent, and a paraphrase is not one. Restating would produce
   four slightly different Ohm's laws in four repositories inside two years.
2. **Enforce the citation at construction.** `Correspondence` rejects a component
   or role the cited foundation does not declare, so the combination cannot
   quietly grow a will of its own. Cross-package agreement is then a test, not a
   convention.
3. **Make the licence deletable.** The transport rests on an adopted premise, and
   that premise is an argument rather than prose: `include_licence=False` removes
   it, and the closure then contains no will conclusion at all. Nothing false is
   derived without it. This mirrors `deliberation_space(include_norm=False)`, and
   the mirroring is not decorative. Both are declared bridges and both are worth
   exactly as much as their declarations.
4. **Do not import either parent.** A combination field should not force its two
   subjects into every install of an operation-space library, and a foundation
   that imported its own combination field would cycle. The cost is that the
   cross-checks can be skipped, so a skip is reported as a skip and recorded in
   `VALIDATION.md`, never silently counted as a pass.

None of this establishes that a transport is sound. `hyperphysics` records the
absence of any soundness criterion for a transport as its own principal open
problem, so there is currently nothing to derive such a licence from. A
combination field also inherits every open obligation of both parents; citing a
foundation does not discharge that foundation's obligations, and the combination
cannot be sounder than either side of it.

### Grounded hyperlogic

Build from Grounded Hyperset Theory's graph/quotient machinery and connect to
Grounded Hypercalculi's hypercalculus, language calculus, and real-analysis
modules. First identify the relation each translation preserves: bisimulation,
syntax identity, proof derivability, or numerical equality are different.
Finite cyclic graphs can model structural self-reference without supplying
truth, derivability, ordinal ranks, or moral justification. A future logic or
hyperlogic calculus needs proof rules and countermodels for each transport.

### Metamathethicology

The combination shares stages, explicit assumptions, domain-tagged judgments,
replay, recoverable representation, and reflection. Domain calculi should be
modules/adapters over those mechanisms until independent mathematical contracts
justify separate distributions. This preserves the combined subject rather
than equating its four components or declaring four separate foundations by name.

## Next proof obligations

1. Give source-native encoders and decoders and prove recovery preserves rejected
   as well as accepted records. Host serialization alone does not discharge this.
2. Derive an internal checking operation and prove correspondence with replay,
   including the exact premise context and all domain/stage restrictions.
3. Specify limit-stage interpretation and evidence transport without extrapolating
   arbitrary infinite behavior from finite prefixes.
4. Add substitutions to the shared language calculus only with variable typing,
   capture/disjointness conditions, and falsifying proof examples.
5. Supply a worked native derivation of a lower-order subject under those rules.

These gates are additive research work, not permission to assume an unproved
principle or weaken an existing countermodel. No native Hypermath theorem was
added, edited, or proved by this initial implementation.
