"""Re-measure the declaration census that ``definitional_shadow.hm`` asserts.

That file states a relation between three fields it does not import: hypermath
declares only interior (``relation``, ``close``) and no boundary; hyperethics
declares only boundary (``non-derive``, ``open``) and no interior; hyperlogic L0
carries both. The whole content of the word "shadow" there is that complement,
so the numbers are the claim and not an illustration of it.

The sibling checkouts are not a declared dependency and are found by path, one
level above this repository. When they are absent every test here skips, and a
skip means the census was NOT checked on that run -- not that it was checked and
passed. ``VALIDATION.md`` records which of the two happened.

The L3 row of ``measured per-layer`` is deliberately asserted as an inequality.
Three layers align exactly and the fourth does not, the file says so, and a test
that only pinned the three agreements would hide the one disagreement that keeps
``nd-count-alignment-is-law`` honest.

The L3 row moved on 2026-09-21, from 23 to 28, when hyperethics added a
reflection section carrying five more refusals. L0 and L2 then moved on
2026-09-23 as the corrected operations-and-values declaration exposed three
new L0 boundaries and eight new L2 boundaries. The numbers here measure sibling
repositories that change independently of this one; a number that moves is a
fact about the sibling, not by itself a broken implementation.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

SIBLINGS = Path(__file__).resolve().parents[2]

FIELDS = {
    "hypermath": ["L0_ground", "L1_relations", "L2_operations", "L3_ordinatics"],
    "hyperlogic": ["L0_triangle"],
    "hyperethics": ["L0_creation", "L1_entity", "L2_will", "L3_consciousness"],
}

INTERIOR = ("relation", "close")
BOUNDARY = ("non-derive", "open")

# A declaration keyword starts a line in column zero. Prose about closing is
# indented under a comment marker, which is exactly the distinction hyperethics
# relies on when it writes "SHARPENED, NOT CLOSED" fifty-one times and declares
# no close at all.
_DECLARATION = re.compile(r"^([a-z][a-z-]*)\b", re.MULTILINE)


def _layer(field: str, stem: str) -> Path:
    return SIBLINGS / field / f"{stem}.hm"


def _census(path: Path) -> dict[str, int]:
    if not path.is_file():
        pytest.skip(f"{path} is not present, so its census cannot be measured")
    counts: dict[str, int] = {}
    for keyword in _DECLARATION.findall(path.read_text(encoding="utf-8")):
        counts[keyword] = counts.get(keyword, 0) + 1
    return counts


def _field_census(field: str) -> dict[str, int]:
    total: dict[str, int] = {}
    for stem in FIELDS[field]:
        for keyword, n in _census(_layer(field, stem)).items():
            total[keyword] = total.get(keyword, 0) + n
    return total


def _sum(census: dict[str, int], keywords: tuple[str, ...]) -> int:
    return sum(census.get(keyword, 0) for keyword in keywords)


def test_hypermath_declares_interior_and_never_declares_boundary():
    """COUNT CORRECTED 2026-09-21: closes 13 -> 16.

    Renumbering is correct here. The claim this test makes is the *disjointness*
    -- hypermath declares interior vocabulary and no boundary vocabulary -- and
    that half (``_sum(census, BOUNDARY) == 0``) never moved. The close total is
    a census pin, and a census pin is supposed to move in the same change as the
    thing it counts; it did not, because the closes happened in another
    repository. The three are `path-trace` and `path-length` (L2_operations) and
    `finite-apply-from-ground` (L3_ordinatics), all uncommitted in hypermath.
    """
    census = _field_census("hypermath")
    assert census.get("relation", 0) == 4
    assert census.get("close", 0) == 16
    assert _sum(census, BOUNDARY) == 0


def test_hyperethics_declares_boundary_and_never_declares_interior():
    census = _field_census("hyperethics")
    assert census.get("non-derive", 0) == 51
    assert census.get("open", 0) == 1
    assert _sum(census, INTERIOR) == 0


def test_hyperlogic_carries_both_censuses():
    census = _field_census("hyperlogic")
    assert census.get("relation", 0) == 3
    assert census.get("close", 0) == 3
    assert census.get("non-derive", 0) == 3
    assert census.get("open", 0) == 1


def test_the_two_censuses_are_disjoint_across_the_two_fields():
    """COUNT CORRECTED 2026-09-21: hypermath interior 17 -> 20, same three closes.

    Both zeroes -- the load-bearing half of the disjointness -- are unchanged.
    """
    body = _field_census("hypermath")
    shadow = _field_census("hyperethics")
    assert (_sum(body, INTERIOR), _sum(body, BOUNDARY)) == (20, 0)
    assert (_sum(shadow, INTERIOR), _sum(shadow, BOUNDARY)) == (0, 52)


# ---------------------------------------------------------------------------
# MEASURED 2026-09-23: THE ALIGNMENT IS NOW ONE LAYER, NOT THREE.
#
# The four assertions below were written against hypermath's census before
# three opaques were closed there on 2026-09-21 (`path-trace` and `path-length`
# in L2_operations, `finite-apply-from-ground` in L3_ordinatics -- all three
# still uncommitted in `hypermath`). Measured now:
#
#     L0_ground      closes 3   L0_creation       refuses  6   BROKEN
#     L1_relations   closes 7   L1_entity         refuses  7   ALIGNED
#     L2_operations  closes 4   L2_will           refuses 10   BROKEN  (was 2 = 2)
#     L3_ordinatics  closes 2   L3_consciousness  refuses 28   broken by design
#
# These failures are represented as strict expected failures. They are not stale
# numbers and cannot be fixed by assigning a shared count: L0 is 3 versus 6 and
# L2 is 4 versus 10. The alignment itself broke while the vocabulary disjointness
# remained intact.
#
# WHAT SURVIVED, and it is the deeper claim: the two disjointness invariants
# still hold exactly. hypermath declares interior vocabulary and *zero* boundary
# vocabulary; hyperethics declares boundary and *zero* interior. Those are
# untouched. What decayed is the per-layer numeric correspondence, which now
# holds only at L1.
#
# THE OPEN QUESTION, which is formal work and not a test fix: was the per-layer
# alignment a structural law of the two fields, or a coincidence that held while
# hypermath's L2 was under-closed? `nd-refusal-counts-are-naming` leans on it.
# If it was a law, hypermath's three closes need re-examining; if it was
# coincidence, the claim should be narrowed to L0-L1 and this test rewritten to
# assert only what is load-bearing.
#
# NOTE ON COUPLING: this file reads two *other* repositories' sources, resolved
# as siblings of this repository's own parent directory (SIBLINGS, above). That
# is why a change in hypermath or hyperethics can turn this suite red with
# nothing in either repository aware of it. The coupling is deliberate; the
# reconciliation record for it is kept outside this repository.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("body_layer", "shadow_layer", "count"),
    [
        pytest.param(
            "L0_ground", "L0_creation", 3,
            marks=pytest.mark.xfail(
                strict=True,
                reason="2026-09-23 census: closes=3, refusals=6; alignment broke.",
            ),
        ),
        ("L1_relations", "L1_entity", 7),
        pytest.param(
            "L2_operations", "L2_will", 4,
            marks=pytest.mark.xfail(
                strict=True,
                reason="2026-09-23 census: closes=4, refusals=10; alignment broke.",
            ),
        ),
    ],
)
def test_only_the_recorded_aligned_layer_refuses_as_often_as_it_closes(body_layer, shadow_layer, count):
    assert _census(_layer("hypermath", body_layer)).get("close", 0) == count
    assert _census(_layer("hyperethics", shadow_layer)).get("non-derive", 0) == count


def test_the_fourth_layer_breaks_the_alignment():
    """L3 was always the layer that breaks alignment; the point is that it does.

    COUNT CORRECTED 2026-09-21: closes moved 1 -> 2 when
    `finite-apply-from-ground` was closed in hypermath's L3. Renumbering is
    correct *here* -- unlike the L2 case above -- because this test asserts the
    alignment *fails*, and it still fails. The exact close count is incidental
    to the claim, so it is now read rather than pinned, and the refusal count
    and the inequality carry the test.
    """
    closes = _census(_layer("hypermath", "L3_ordinatics")).get("close", 0)
    refusals = _census(_layer("hyperethics", "L3_consciousness")).get("non-derive", 0)
    assert refusals == 28
    assert closes != refusals


def test_no_hm_keyword_declares_a_model():
    """The dark matter: models are invisible to the census that measures them.

    ``nd-refusal-counts-are-naming`` turns on this. Every refutation in the
    family is carried by a finite structure, and no ``.hm`` keyword introduces
    one -- so the boundary census counts names and the things that make those
    names true are not in the vocabulary at all.
    """
    vocabulary: set[str] = set()
    for field in FIELDS:
        for stem in FIELDS[field]:
            vocabulary |= set(_census(_layer(field, stem)))
    assert vocabulary <= {
        "primitive",
        "opaque",
        "axiom",
        "derive",
        "non-derive",
        "relation",
        "close",
        "constant",
        "open",
        "graduation",
        # ADDED 2026-09-21. hyperethics coined ``notation`` for
        # ``notation Borne :: Norm -> assertion-position`` in ``L0_creation.hm``
        # -- a symbol written 74 times across L3 and declared nowhere until then.
        # It is admissible here for the reason this test exists: notation
        # introduces no model. It names assertion position, adds no type, and
        # moves no graduation count, and hyperethics' own
        # ``test_borne_is_only_ever_in_assertion_position`` holds it to that by
        # failing if any layer ever writes ``not Borne`` or quantifies over
        # borne-status. If that test ever fails, the notation has become a
        # predicate and this entry must be reconsidered along with it.
        "notation",
    }
    assert not {k for k in vocabulary if "model" in k or "structure" in k or "witness" in k}


@pytest.mark.parametrize(
    ("stem", "theorems"),
    [
        ("DarkMatterL0", ("mergedIsModel", "mergedKeepsDepthTwo", "r1", "r2", "r3")),
        ("DarkMatterL3", ("mergedIsModel", "mergedKeepsTheDerives", *[f"m{i}" for i in range(1, 13)])),
    ],
)
def test_the_merged_witnesses_are_present_and_admit_nothing(stem, theorems):
    """The evidence files are checked for shape here and for truth by Lean.

    This package has no Lean toolchain, so this cannot re-run the kernel. What
    it can do is fail if an evidence file loses a theorem or acquires a
    ``sorry`` -- which is the failure that would otherwise pass unnoticed, since
    nothing else in this repository reads these files.
    ``evidence/README.md`` gives the two commands that do re-run them.
    """
    source = Path(__file__).resolve().parents[1] / "evidence" / f"{stem}.lean"
    text = source.read_text(encoding="utf-8")
    for name in theorems:
        assert re.search(rf"^theorem {name}\b", text, re.MULTILINE), name

    # Using a term and discussing it are different, and the files discuss both
    # of these in comments. Strip the comments before looking for either.
    code = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("--")
    )
    assert not re.search(r"\bsorry\b", code)
    assert not re.search(r"^axiom\b", code, re.MULTILINE)


def test_hyperethics_l0_leaves_one_opaque_neither_closed_nor_refused():
    """The shadow's edge is ragged, and ``d-the-shadow-is-ragged`` says where.

    The first three L0 refusals land twice on ``norm-inhabits`` and once on
    ``norm-returns``. Three later refusals price the operations-and-values
    declaration. None names ``norm-other`` -- the counterpart of
    ``struct-distinct`` -- so it still gets neither treatment. If a later layer
    closes or refuses it, this test is the thing that notices.
    """
    source = _layer("hyperethics", "L0_creation")
    if not source.is_file():
        pytest.skip(f"{source} is not present, so the slot coverage cannot be measured")
    text = source.read_text(encoding="utf-8")
    refusals = [
        block.split("\n\n")[0]
        for block in text.split("\nnon-derive ")[1:]
    ]
    assert [refusal.split(":", 1)[0] for refusal in refusals] == [
        "nd-universal-immanence",
        "nd-good-from-immanence",
        "nd-transitive-exposure",
        "nd-only-the-archetype-creates",
        "nd-every-realm-creates",
        "nd-immanence-in-operations",
    ]
    assert not any("norm-other" in r for r in refusals)
