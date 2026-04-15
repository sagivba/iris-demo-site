"""Inference utilities for Iris prediction."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = Path(__file__).with_name("iris_model.joblib")
SPECIES_BY_CLASS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}

_MODEL = None


class IrisPredictor:
    """Simple wrapper around a trained Iris classifier."""

    def __init__(self, model=None):
        self._model = model or _load_or_initialize_model()

    def predict(self, features: Sequence[float]) -> dict[str, object]:
        normalized_features = _normalize_features(features)
        predicted_class = int(self._model.predict([normalized_features])[0])
        species = SPECIES_BY_CLASS[predicted_class]
        return {
            "prediction": species,
            "class_id": predicted_class,
            "features": normalized_features,
        }


def predict_iris(features: Sequence[float]) -> dict[str, object]:
    """Predict an Iris species for a sequence of four numeric features."""
    predictor = IrisPredictor()
    return predictor.predict(features)


def _load_or_initialize_model():
    global _MODEL

    if _MODEL is not None:
        return _MODEL

    if MODEL_PATH.exists():
        _MODEL = joblib.load(MODEL_PATH)
        return _MODEL

    iris = load_iris()
    model = LogisticRegression(max_iter=300)
    model.fit(iris.data, iris.target)
    joblib.dump(model, MODEL_PATH)
    _MODEL = model
    return _MODEL


def _normalize_features(features: Sequence[float]) -> list[float]:
    if len(features) != 4:
        raise ValueError("Exactly four Iris features are required.")

    normalized: list[float] = []
    for value in features:
        normalized.append(float(value))
    return normalized
