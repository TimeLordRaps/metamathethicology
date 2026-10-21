"""Partial, checked bridge from Hyperorganization CNF to Ordinatics.

Hyperorganization represents all ordinals below epsilon_0 with recursively
nested exponents.  Ordinatics represents exactly the polynomial fragment below
``omega ** omega``.  The bridge therefore accepts only Hyperorganization terms
whose exponents are finite.  It never truncates an unsupported exponent.

The selected recovery use is comparison of ``omega * phase + lower`` ranks.
No arithmetic beyond representation round-trip and order is claimed here.
"""

from __future__ import annotations

from hyperoptimization.ordinal import Ordinal as HyperorganizationOrdinal
from ordinatics.ordinals import Ordinal as OrdinaticsOrdinal


class OutsideOrdinaticsDomain(ValueError):
    """The source ordinal is at least ``omega ** omega``."""


def to_ordinatics(value: HyperorganizationOrdinal) -> OrdinaticsOrdinal:
    """Embed the exact below-``omega**omega`` part of Hyperorganization CNF."""
    if type(value) is not HyperorganizationOrdinal:
        raise TypeError("value must be a hyperoptimization Ordinal")
    terms: list[tuple[int, int]] = []
    for exponent, coefficient in value.terms:
        try:
            finite_exponent = exponent.to_int()
        except ValueError as error:
            raise OutsideOrdinaticsDomain(
                "a non-finite CNF exponent is outside Ordinatics (< omega**omega)"
            ) from error
        terms.append((finite_exponent, coefficient))
    if not terms:
        return OrdinaticsOrdinal()
    coefficients = [0] * (max(exponent for exponent, _ in terms) + 1)
    for exponent, coefficient in terms:
        coefficients[exponent] = coefficient
    return OrdinaticsOrdinal(tuple(coefficients))


def to_hyperorganization(value: OrdinaticsOrdinal) -> HyperorganizationOrdinal:
    """Embed every Ordinatics ordinal into Hyperorganization's larger carrier."""
    if type(value) is not OrdinaticsOrdinal:
        raise TypeError("value must be an ordinatics Ordinal")
    return HyperorganizationOrdinal.from_terms(
        (HyperorganizationOrdinal.of(exponent), coefficient)
        for exponent, coefficient in reversed(tuple(enumerate(value.coefficients)))
        if coefficient
    )


__all__ = ["OutsideOrdinaticsDomain", "to_hyperorganization", "to_ordinatics"]
