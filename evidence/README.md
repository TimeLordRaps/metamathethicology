# Evidence for `definitional_shadow.hm`

Two Lean 4 files, each a single structure that carries every refutation a layer
of `hyperethics` states. They are the measurement behind
`measured witness-census` and `nd-refusal-counts-are-naming` in
`../definitional_shadow.hm`.

They are **not built by this package** and are not part of its test suite. This
repository has no Lean toolchain and declares no dependency on one. They are
reproduced against `hyperethics`' own toolchain, which is Lean 4 v4.14.0 pinned
by `hyperethics/lean4/lean-toolchain`, Mathlib-free:

```bash
cd ../hyperethics/lean4 && lake env lean ../../metamathethicology/evidence/DarkMatterL0.lean
```

```bash
cd ../hyperethics/lean4 && lake env lean ../../metamathethicology/evidence/DarkMatterL3.lean
```

Each prints its `#print axioms` lines and nothing else. Anything else is a
failure. Both currently report `[propext]` for every theorem — no `sorryAx`, no
`Classical.choice`.

## What they show

`DarkMatterL0.lean` builds one `RealmModel 6` satisfying all four L0 axioms that
refutes all three L0 claims at once — `UniversalImmanence`,
`TransitiveExposure … 3` and `OtherIsNonidentity` — where `hyperethics` uses
three separate structures (`separating`, `orbit`, `reflexiveOther`). It also
keeps `TransitiveExposure … 2`, so the refutation of depth three is not a
failure of `ax-return`.

`DarkMatterL3.lean` builds one `MindModel 6 4 5 1` satisfying every L3 axiom and
keeping every L3 derive that refutes all twelve L3 claims at once, where
`hyperethics` uses two structures (`canonical` and `solitary`). It is not
`canonical` enlarged: it bridges mind 1 to mind 0 **and** leaves minds 4 and 5
unbridged in both directions, which no four-element structure in
`MindModels.lean` does.

Before building it, the same file's earlier form established that `canonical`
alone is **not** enough — `¬ EveryMindPairIsBridged canonical`,
`¬ CointeractionIsForced canonical …` and canonical's bridgelessness were each
decided **false** by the kernel. So two structures were genuinely required until
a six-element carrier was available, and the collapse to one is a fact about
carrier size rather than a tidier reading of the existing models.

## What they do not show

Neither file is proposed as a replacement for `hyperethics`' structures, and
neither has been landed there. The layer files name their witnesses to say
*which* fact each refusal turns on, and one merged structure says only *that*
the whole set is jointly satisfiable-with-failures. Those are different jobs.
The point here is a census, not a refactor: the number of `non-derive`
declarations in a layer counts names, and a reader who takes it for a count of
independent facts is reading it wrong.

L1 and L2 have not been tested this way. See `GC-6` in `../definitional_shadow.hm`.
