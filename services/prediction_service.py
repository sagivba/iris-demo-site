"""Prediction service layer for the Iris app."""

from typing import Any

from model.predictor import predict_species
from services.validation_service import validate_and_prepare_input


def predict_from_raw_input(raw_input: Any) -> dict[str, Any]:
    """Validate raw input, call model layer, and return a stable response."""
    validation_result = validate_and_prepare_input(raw_input)
    if not validation_result["ok"]:
        return {
            "ok": False,
            "errors": validation_result["errors"],
        }

    try:
        species = predict_species(validation_result["model_input"])
    except Exception:
        return {
            "ok": False,
            "errors": ["Prediction failed. Ensure the trained model is available."],
        }

    return {
        "ok": True,
        "prediction": species,
    }
