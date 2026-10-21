import Hyperethics.Countermodels

open Hyperethics

namespace DarkMatterL0

/-- One L0 structure carrying all three of L0's refutations at once.
`separating`'s non-immanent bearer, `orbit`'s broken three-step return, and
`reflexiveOther`'s self-other, in one carrier with one archetype. -/
abbrev merged : RealmModel 6 :=
  { archetype := 0
    create := mapOf 0 [2, 2, 2, 4, 5, 4]
    other := relOf [(2, 0), (4, 0), (5, 0), (4, 4)]
    inhabits := relOf [(0, 0), (0, 2), (0, 4), (0, 5)]
    returnsOn := relOf [(2, 0), (2, 1), (2, 2), (5, 3), (4, 4), (5, 5)] }

theorem mergedIsModel : IsModel merged := by decide

-- ax-return still supplies what it supplies.
theorem mergedKeepsDepthTwo : TransitiveExposure merged 2 := by decide

-- All three L0 refutations, from this one structure.
theorem r1 : ¬ UniversalImmanence merged := by decide
theorem r2 : ¬ TransitiveExposure merged 3 := by decide
theorem r3 : ¬ OtherIsNonidentity merged := by decide

end DarkMatterL0

#print axioms DarkMatterL0.mergedIsModel
#print axioms DarkMatterL0.r1
#print axioms DarkMatterL0.r2
#print axioms DarkMatterL0.r3
