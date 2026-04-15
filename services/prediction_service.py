"""Service layer entrypoint for Iris predictions."""

from __future__ import annotations

from typing import Dict

from model.predictor import predict_species
from services.validation_service import validate_iris_inputs

SPECIES_LABELS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


def predict_iris(features: Dict[str, float]) -> Dict[str, object]:
    """Return a deterministic Iris response for the web result template."""
    _ = features

    predicted_class_index = 0
    predicted_class_label = SPECIES_LABELS[predicted_class_index]

    return {
        "predicted_class_index": predicted_class_index,
        "predicted_class_label": predicted_class_label,
    }


def predict_from_raw_input(raw_input: Dict[str, str]) -> Dict[str, object]:
    """Validate raw feature values and return a stable prediction contract."""
    validated_inputs, validation_errors = validate_iris_inputs(raw_input)

    if validation_errors:
        normalized_errors = [
            error.replace("must be a valid number.", "must be a numeric value.")
            for error in validation_errors
        ]
        return {"ok": False, "errors": normalized_errors}

    try:
        ordered_inputs = [[
            validated_inputs["sepal_length"],
            validated_inputs["sepal_width"],
            validated_inputs["petal_length"],
            validated_inputs["petal_width"],
        ]]
        prediction = predict_species(ordered_inputs)
    except Exception:
        return {
            "ok": False,
            "errors": ["Prediction failed. Ensure the trained model is available."],
        }

    return {"ok": True, "prediction": prediction}
