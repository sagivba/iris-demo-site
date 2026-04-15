"""Validation helpers for Iris feature inputs."""

from __future__ import annotations

import math
from typing import Any, Dict, List

IRIS_FEATURE_FIELDS = (
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
)


ValidationError = Dict[str, str]
ValidationResult = Dict[str, Any]


def validate_iris_features(payload: Dict[str, Any] | None) -> ValidationResult:
    """Validate and normalize Iris feature inputs.

    Args:
        payload: Mapping containing Iris feature keys.

    Returns:
        A dict with shape:
            {
                "is_valid": bool,
                "data": dict[str, float],
                "errors": list[{"field": str, "code": str, "message": str}],
            }
    """
    if payload is None:
        payload = {}

    errors: List[ValidationError] = []
    normalized: Dict[str, float] = {}

    for field in IRIS_FEATURE_FIELDS:
        if field not in payload:
            errors.append(
                {
                    "field": field,
                    "code": "required",
                    "message": f"{field} is required.",
                }
            )
            continue

        raw_value = payload.get(field)

        if raw_value is None:
            errors.append(
                {
                    "field": field,
                    "code": "required",
                    "message": f"{field} is required.",
                }
            )
            continue

        if isinstance(raw_value, str) and not raw_value.strip():
            errors.append(
                {
                    "field": field,
                    "code": "required",
                    "message": f"{field} cannot be empty.",
                }
            )
            continue

        try:
            numeric_value = float(raw_value)
        except (TypeError, ValueError):
            errors.append(
                {
                    "field": field,
                    "code": "not_numeric",
                    "message": f"{field} must be numeric.",
                }
            )
            continue

        if not math.isfinite(numeric_value):
            errors.append(
                {
                    "field": field,
                    "code": "not_numeric",
                    "message": f"{field} must be a finite numeric value.",
                }
            )
            continue

        normalized[field] = numeric_value

    return {
        "is_valid": not errors,
        "data": normalized if not errors else {},
        "errors": errors,
    }
