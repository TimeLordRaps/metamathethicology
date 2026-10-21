"""Run the bounded operation-space demonstration."""

from __future__ import annotations

import json

from .examples import demo

print(json.dumps(demo(), indent=2, ensure_ascii=True))
