"""Service layer entrypoint for Iris predictions."""

from __future__ import annotations

from typing import Dict

from model.predictor import predict_species
from services.validation_service import validate_iris_inputs

SPECIES_LABELS = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica",
}

CLASS_IMAGE_PATHS = {
    "iris-setosa": "images/iris-setosa.svg",
    "iris-versicolor": "images/iris-versicolor.svg",
    "iris-virginica": "images/iris-virginica.svg",
}


def get_class_image_path(class_label: str) -> str | None:
    """Return static image path for a predicted class label."""
    normalized_label = class_label.strip().lower()

    if normalized_label in CLASS_IMAGE_PATHS:
        return CLASS_IMAGE_PATHS[normalized_label]

    if not normalized_label.startswith("iris-"):
        normalized_label = f"iris-{normalized_label}"

    return CLASS_IMAGE_PATHS.get(normalized_label)


def predict_iris(features: Dict[str, float]) -> Dict[str, object]:
    """Return a deterministic Iris response for the web result template."""
    _ = features

    predicted_class_index = 0
    predicted_class_label = SPECIES_LABELS[predicted_class_index]

    predicted_class_image_path = get_class_image_path(predicted_class_label)

    return {
        "predicted_class_index": predicted_class_index,
        "predicted_class_label": predicted_class_label,
        "predicted_class_image_path": predicted_class_image_path,
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
