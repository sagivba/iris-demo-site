"""Model loading and prediction utilities."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Sequence

MODEL_FILE = Path(__file__).resolve().parent / "iris_model.joblib"
CLASS_LABELS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}
IRIS_FIELD_ORDER = (
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
)


@lru_cache(maxsize=1)
def load_model() -> Any:
    """Load and cache the persisted Iris model artifact."""
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            f"Model artifact not found at {MODEL_FILE}. Run model/train.py first."
        )

    import joblib

    return joblib.load(MODEL_FILE)


def predict_species(model_input: list[list[float]]) -> str:
    """Predict a species label from prepared model input."""
    model = load_model()
    prediction = model.predict(model_input)[0]

    if isinstance(prediction, str):
        return prediction

    return CLASS_LABELS.get(int(prediction), str(prediction))


def _coerce_features(features: Sequence[float] | Mapping[str, float]) -> list[list[float]]:
    """Normalize feature input into the model's expected nested list shape."""
    if isinstance(features, Mapping):
        ordered = [float(features[field]) for field in IRIS_FIELD_ORDER]
        return [ordered]

    return [[float(value) for value in features]]


def predict_iris(features: Sequence[float] | Mapping[str, float]) -> str:
    """Compatibility wrapper that predicts Iris species from 4 features."""
    return predict_species(_coerce_features(features))


class IrisPredictor:
    """Small compatibility class wrapper around the predictor functions."""

    def predict(self, features: Sequence[float] | Mapping[str, float]) -> str:
        return predict_iris(features)
