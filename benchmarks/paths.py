"""Paths for a local ik_llama.cpp build.

Override with IK_LLAMA_HOME (the repo root that contains build/), or with
IK_LLAMA_BIN and IK_LLAMA_MODELS when the binaries and GGUFs live apart.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ik_home() -> Path:
    return Path(os.environ.get("IK_LLAMA_HOME", Path.home() / "ik_llama.cpp")).expanduser()


def models_dir() -> Path:
    return Path(os.environ.get("IK_LLAMA_MODELS", ik_home() / "build" / "models"))


def bin_dir() -> Path:
    return Path(os.environ.get("IK_LLAMA_BIN", ik_home() / "build" / "bin"))


def expand(text: str, **extra: object) -> str:
    values = {
        "models": str(models_dir()),
        "bin": str(bin_dir()),
    }
    values.update({key: str(value) for key, value in extra.items()})
    out = text
    for key, value in values.items():
        out = out.replace("{" + key + "}", value)
    return out
