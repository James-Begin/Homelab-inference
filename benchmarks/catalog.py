#!/usr/bin/env python3
"""
Experiment Catalog Validation and Loading Module
Implements catalog schema validation per improvement-plan.md Section 5 (Phase 1.1).
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_REQUEST_BLOCK = {
    "endpoint": "chat",
    "max_tokens": 4096,
    "temperature": 0.0,
    "top_p": 1.0,
    "seed": 0,
    "system_prompt": "You are an expert scientific researcher. Provide concise, rigorous reasoning within 600 words, then state your final answer choice clearly.",
    "user_suffix": "standard_v2"
}

VALID_PROTOCOLS = {
    "A-tput-v1",
    "B-equiv-v1",
    "Q-kld-v1",
    "C-code-v1",
    "C-gpqa-v2",
    "legacy-v1"
}


class CatalogValidationError(Exception):
    """Raised when an experiment catalog fails schema or uniqueness validation."""
    pass


def normalize_catalog_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures legacy fields are normalized into the modern schema."""
    norm = dict(entry)

    # Normalize request block
    if "request" not in norm or not isinstance(norm["request"], dict):
        req = dict(DEFAULT_REQUEST_BLOCK)
        if "prompt" in norm:
            req["prompt_type"] = norm["prompt"]
        norm["request"] = req

    # Normalize protocol
    if "protocol" not in norm:
        norm["protocol"] = "legacy-v1"

    # Normalize lossy flag
    if "lossy" not in norm:
        # Heuristic: MTP, suffix, repack, numactl are lossless; KV quant, SER, expert clamping are lossy
        change = norm.get("change", "").lower()
        server_flags = norm.get("server_flags", "").lower()
        if any(k in change or k in server_flags for k in ["-ctk", "-ctv", "-ser", "pruning", "clamp"]):
            norm["lossy"] = True
        else:
            norm["lossy"] = False

    return norm


def load_catalog(catalog_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Loads and validates the experiments catalog.
    Validates:
      - Unique 'number'
      - Unique 'id'
      - Required fields
    Fixes known defect H10 (duplicate number 90) during normalization.
    """
    if catalog_path is None:
        catalog_path = Path(__file__).resolve().parent / "experiments.json"
    else:
        catalog_path = Path(catalog_path)

    if not catalog_path.exists():
        raise FileNotFoundError(f"Catalog file not found: {catalog_path}")

    with open(catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise CatalogValidationError("Catalog root must be a JSON array of experiment objects.")

    seen_numbers = {}
    seen_ids = set()
    normalized_list = []

    for idx, entry in enumerate(data):
        if not isinstance(entry, dict):
            raise CatalogValidationError(f"Item at index {idx} is not an object: {entry}")

        exp_id = entry.get("id")
        if not exp_id:
            raise CatalogValidationError(f"Item at index {idx} missing required field 'id'.")

        if exp_id in seen_ids:
            raise CatalogValidationError(f"Duplicate experiment id found: '{exp_id}' at index {idx}.")
        seen_ids.add(exp_id)

        # Handle H10 fix: if duplicate number 90 occurs, check if it's the exp89 slot similarity run
        num = entry.get("number")
        if num is None:
            raise CatalogValidationError(f"Experiment '{exp_id}' missing required field 'number'.")

        if num == 90 and "exp89" in exp_id:
            num = 89
            entry["number"] = 89

        if num in seen_numbers:
            prev_id = seen_numbers[num]
            raise CatalogValidationError(
                f"Duplicate experiment number '{num}' found for '{exp_id}' (previously assigned to '{prev_id}')."
            )
        seen_numbers[num] = exp_id

        norm_entry = normalize_catalog_entry(entry)
        normalized_list.append(norm_entry)

    return normalized_list


def get_experiment(catalog: List[Dict[str, Any]], key: str) -> Dict[str, Any]:
    """Finds an experiment by number or ID string."""
    hits = [
        exp for exp in catalog
        if str(exp.get("number")) == str(key) or exp.get("id") == str(key)
    ]
    if len(hits) == 1:
        return hits[0]
    prefix = [exp for exp in catalog if str(exp.get("id", "")).startswith(str(key))]
    if len(prefix) == 1:
        return prefix[0]
    known = ", ".join(str(exp.get("number")) for exp in catalog)
    raise KeyError(f"No single experiment matches {key!r}. Numbers in catalog: {known}")


if __name__ == "__main__":
    cat = load_catalog()
    print(f"Catalog successfully loaded and validated: {len(cat)} experiments.")
