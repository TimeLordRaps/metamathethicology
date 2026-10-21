"""Run the finite demonstration through an exact pinned Hypermath Lean checker."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from metamathethicology.certified_intellidynamics import (
    INVARIANT_ID,
    VerifiedChecker,
    demo_model,
)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--checker", type=Path, required=True)
    result.add_argument("--checker-sha256", required=True)
    result.add_argument("--model-source", type=Path, required=True)
    result.add_argument("--model-source-sha256", required=True)
    result.add_argument("--main-source", type=Path, required=True)
    result.add_argument("--main-source-sha256", required=True)
    return result


def main() -> None:
    arguments = parser().parse_args()
    checker = VerifiedChecker(
        arguments.checker,
        arguments.checker_sha256,
        arguments.model_source,
        arguments.model_source_sha256,
        arguments.main_source,
        arguments.main_source_sha256,
        (
            "finite-table-checker/v1",
            "two-context-two-peer/v1",
            "no-limit-transition/v1",
            "hyperethics-governance/v1",
            INVARIANT_ID,
        ),
    )
    print(json.dumps(demo_model(checker), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
