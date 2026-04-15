"""Validation helpers for Iris prediction input."""

from typing import Any

FEATURE_NAMES = (
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
)


def validate_and_prepare_input(raw_input: Any) -> dict[str, Any]:
    """Validate raw payload and prepare model-ready input.

    Returns a stable dictionary shape with ``ok`` and ``errors`` keys.
    On success, includes ``normalized`` and ``model_input``.
    """
    if not isinstance(raw_input, dict):
        return {
            "ok": False,
            "errors": ["Input must be an object with Iris feature fields."],
        }

    errors: list[str] = []
    normalized: dict[str, float] = {}

    for field in FEATURE_NAMES:
        raw_value = raw_input.get(field)

        if raw_value is None:
            errors.append(f"{field} is required.")
            continue

        if isinstance(raw_value, str):
            raw_value = raw_value.strip()
            if raw_value == "":
                errors.append(f"{field} is required.")
                continue

        try:
            normalized[field] = float(raw_value)
        except (TypeError, ValueError):
            errors.append(f"{field} must be a numeric value.")

    if errors:
        return {
            "ok": False,
            "errors": errors,
        }

    model_input = [[normalized[field] for field in FEATURE_NAMES]]

    return {
        "ok": True,
        "errors": [],
        "normalized": normalized,
        "model_input": model_input,
    }
