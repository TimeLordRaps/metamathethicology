import Hyperethics.MindModels

open Hyperethics.MindModels

namespace DarkMatter

/-- Every element of `Fin 6`, listed, and the proof that the list is exhaustive. -/
def every6 : List (Fin 6) := [0, 1, 2, 3, 4, 5]
theorem every6IsComplete : ∀ i : Fin 6, every6.contains i = true := by decide

/-- THE CANDIDATE DARK MATTER.

`canonical` on mediums 0-3, `solitary`'s two isolated minds carried in at 4 and
5. Nothing relates the two halves. If this satisfies every axiom and refutes
everything `canonical` and `solitary` refute between them, then L3's twelve
refutations rest on ONE structure and not two. -/
abbrev merged : MindModel 6 4 5 1 :=
  { conscious := memberOf [0, 1, 2, 4, 5]
    converges := memberOf [0, 1, 3, 4, 5]
    minds := memberOf [0, 1, 4, 5]
    models := relOf [(0, 0), (1, 1), (1, 0), (4, 4), (5, 5)]
    cointeracts := relOf [(0, 0), (1, 0)]
    cointeractsEntity := relOf [(1, 0)]
    willfieldModeled := relOf [(1, 0)]
    bridge := relOf [(1, 0)]
    bridgeAt := tripleOf []
    mediumOf := mapOf 3 [0, 3, 3, 3]
    bearerOf := mapOf 0 [0, 1, 0]
    kindOf := mapOf areality [areality, areality, surreality, preality, baseReality]
    constructs := relOf [(1, 0), (4, 0)]
    projects := relOf [(0, 0)]
    languageOf := fun _ _ => 0
    base := Hyperethics.EntityModels.canonical }

-- Does it satisfy every axiom, and keep every derive?
theorem mergedIsModel : IsMindModel merged every6 := by decide
theorem mergedKeepsTheDerives : KeepsTheDerives merged every6 := by decide

-- The nine `canonical` carries.
theorem m1 : ¬ ConsciousConverges merged := by decide
theorem m2 : ¬ ConvergenceIsConscious merged := by decide
theorem m3 : ¬ SelfModelingIsOtherModeling merged every6 := by decide
theorem m4 : ¬ BridgeIsPointwise merged := by decide
theorem m5 : ¬ BridgeIsSymmetric merged := by decide
theorem m6 : ¬ EveryEntityIsMinded merged := by decide
theorem m7 : ¬ ConsciousnessIsTimed merged := by decide
theorem m8 : ¬ EveryMindThinks merged every5 := by decide
theorem m9 : ¬ ArealityIsThought merged every1 := by decide

-- The three only `solitary` could carry.
theorem m10 : ¬ EveryMindPairIsBridged merged := by decide
theorem m11 : ¬ CointeractionIsForced merged every6 every4 := by decide
theorem m12 :
    merged.projects 0 0 = true ∧
      merged.constructs 4 0 = true ∧
      (every6.any (fun a => merged.bridge 4 a || merged.bridge a 4)) = false := by
  decide

end DarkMatter

-- Kernel receipts: no sorry, no extra axiom, and the two halves really differ.
#print axioms DarkMatter.mergedIsModel
#print axioms DarkMatter.m5
#print axioms DarkMatter.m10
-- `merged` is NOT `canonical` in disguise: it bridges mind 1 to mind 0 AND
-- leaves minds 4,5 unbridged, which no 4-element structure above does.
example : DarkMatter.merged.bridge 1 0 = true && DarkMatter.merged.bridge 4 5 = false && DarkMatter.merged.bridge 5 4 = false := by decide
