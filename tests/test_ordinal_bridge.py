from __future__ import annotations

from itertools import product

import pytest
from hyperoptimization.ordinal import Ordinal as HyperorganizationOrdinal
from ordinatics.ordinals import Ordinal as OrdinaticsOrdinal

from metamathethicology.certified_intellidynamics import RecoveryRank
from metamathethicology.ordinal_bridge import (
    OutsideOrdinaticsDomain,
    to_hyperorganization,
    to_ordinatics,
)

GRID = tuple(OrdinaticsOrdinal(coefficients) for coefficients in product(range(3), repeat=4))


def test_every_bounded_grid_value_round_trips_exactly():
    for value in GRID:
        assert to_ordinatics(to_hyperorganization(value)) == value


def test_embedding_is_injective_on_the_checked_grid():
    images = {to_hyperorganization(value) for value in GRID}
    assert len(images) == len(set(GRID))


def test_order_is_preserved_and_reflected_on_the_checked_grid():
    for left, right in product(GRID, repeat=2):
        assert (to_hyperorganization(left) < to_hyperorganization(right)) == (left < right)


def test_recovery_omega_times_phase_plus_lower_is_the_same_ordinal():
    for phase, lower in product(range(5), repeat=2):
        native = HyperorganizationOrdinal.from_terms(
            tuple(
                term
                for term in (
                    (HyperorganizationOrdinal.of(1), phase),
                    (HyperorganizationOrdinal.of(0), lower),
                )
                if term[1]
            )
        )
        assert to_ordinatics(native) == RecoveryRank(phase, lower).ordinal


def test_nonfinite_exponent_is_rejected_without_truncation():
    omega = HyperorganizationOrdinal.omega()
    omega_to_omega = HyperorganizationOrdinal.omega_power(omega)
    with pytest.raises(OutsideOrdinaticsDomain, match="outside Ordinatics"):
        to_ordinatics(omega_to_omega)


def test_bridge_refuses_values_from_the_wrong_carrier():
    with pytest.raises(TypeError, match="hyperoptimization"):
        to_ordinatics(OrdinaticsOrdinal((1, 2)))
    with pytest.raises(TypeError, match="ordinatics"):
        to_hyperorganization(HyperorganizationOrdinal.of(3))
