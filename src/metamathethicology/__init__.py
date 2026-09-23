"""Metamathethicology: ordinatics-first, explicitly relative operation spaces.

The combination fields built on that substrate are submodules, imported directly:
`metamathethicology.will_electrophysics` transports electrical law, cited from
`hyperphysics`, onto the will tensor, cited from `hyperethics`, and
`metamathethicology.oreality` reads four declared realms through the structure
`hyperprobability` states. Neither is re-exported here, because a combination
field should be reached by name.
"""

from __future__ import annotations

from .representation import (
    decode_derivation,
    decode_space,
    derivation_digest,
    encode_derivation,
    encode_space,
    judgment_digest,
    space_digest,
)
from .spaces import (
    Assumption,
    BudgetExceeded,
    Derivation,
    Domain,
    InvalidDerivation,
    Judgment,
    OperationSpace,
    Rule,
    Step,
    close,
    reflect,
    replay,
)

__version__ = "0.1.0.dev0"
__all__ = [
    "Assumption", "BudgetExceeded", "Derivation", "Domain", "InvalidDerivation",
    "Judgment", "OperationSpace", "Rule", "Step", "close", "reflect", "replay",
    "decode_derivation", "decode_space", "derivation_digest", "encode_derivation",
    "encode_space", "judgment_digest", "space_digest",
]
