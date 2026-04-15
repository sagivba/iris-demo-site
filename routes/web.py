"""Browser-facing routes for the Iris demo app."""

from __future__ import annotations

import logging

from flask import Blueprint, render_template, request

from services.prediction_service import predict_iris
from services.validation_service import validate_iris_inputs

web_bp = Blueprint("web", __name__)

FIELD_LABELS = {
    "sepal_length": "Sepal length",
    "sepal_width": "Sepal width",
    "petal_length": "Petal length",
    "petal_width": "Petal width",
}


def _format_validation_errors(validation_errors: list[str]) -> list[str]:
    """Convert internal validation messages into user-friendly form text."""
    formatted_errors: list[str] = []

    for error in validation_errors:
        formatted_error = error

        for field_name, label in FIELD_LABELS.items():
            if formatted_error.startswith(field_name):
                formatted_error = formatted_error.replace(field_name, label, 1)
                break

        if formatted_error.endswith("must be a valid number."):
            formatted_error = formatted_error.replace(
                "must be a valid number.",
                "must be a number (for example: 5.1).",
            )

        formatted_errors.append(formatted_error)

    return formatted_errors


@web_bp.get("/")
def home():
    """Render the main Iris input page."""
    return render_template(
        "index.html",
        errors=[],
        form_values={},
        prediction_label=None,
        prediction_image_path=None,
        prediction_image_alt=None,
    )


@web_bp.post("/predict")
def predict():
    """Handle Iris form submission and return either errors or prediction."""
    raw_inputs = {
        "sepal_length": request.form.get("sepal_length", ""),
        "sepal_width": request.form.get("sepal_width", ""),
        "petal_length": request.form.get("petal_length", ""),
        "petal_width": request.form.get("petal_width", ""),
    }

    validated_inputs, validation_errors = validate_iris_inputs(raw_inputs)

    if validation_errors:
        return (
            render_template(
                "index.html",
                errors=_format_validation_errors(validation_errors),
                form_values=raw_inputs,
                prediction_label=None,
            ),
            400,
        )

    try:
        prediction = predict_iris(validated_inputs)
    except Exception:
        logging.exception("Prediction failed in web flow.")
        return (
            render_template(
                "index.html",
                errors=[
                    "We could not generate a prediction right now. "
                    "Please try again in a moment."
                ],
                form_values=raw_inputs,
            ),
            500,
        )

    return render_template(
        "index.html",
        errors=[],
        form_values=raw_inputs,
        prediction_label=prediction["predicted_class_label"],
        prediction_image_path=prediction["predicted_class_image_path"],
        prediction_image_alt=prediction["predicted_class_label"],
    )
