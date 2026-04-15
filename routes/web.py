"""Browser-facing routes for the Iris demo app."""

from __future__ import annotations

from flask import Blueprint, render_template, request

from services.prediction_service import predict_iris
from services.validation_service import validate_iris_inputs

web_bp = Blueprint("web", __name__)


@web_bp.get("/")
def home():
    """Render the main Iris input page."""
    return render_template("index.html", errors=[], form_values={}, prediction_label=None)


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
                errors=validation_errors,
                form_values=raw_inputs,
                prediction_label=None,
            ),
            400,
        )

    prediction = predict_iris(validated_inputs)

    return render_template(
        "index.html",
        errors=[],
        form_values=raw_inputs,
        prediction_label=prediction["predicted_class_label"],
    )
