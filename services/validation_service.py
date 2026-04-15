"""Validation utilities for Iris prediction inputs."""

from __future__ import annotations

from typing import Dict, List, Tuple

IRIS_FIELDS: Tuple[str, ...] = (
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
)


def validate_iris_inputs(raw_inputs: Dict[str, str]) -> Tuple[Dict[str, float], List[str]]:
    """Validate and normalize raw Iris inputs.

    Returns:
        tuple[dict[str, float], list[str]]: Parsed values and validation errors.
    """
    values: Dict[str, float] = {}
    errors: List[str] = []

    for field in IRIS_FIELDS:
        raw_value = str(raw_inputs.get(field, "")).strip()

        if not raw_value:
            errors.append(f"{field} is required.")
            continue

        try:
            values[field] = float(raw_value)
        except ValueError:
            errors.append(f"{field} must be a valid number.")

    return values, errors
