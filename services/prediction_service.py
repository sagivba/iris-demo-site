"""Service layer entrypoint for Iris predictions."""

from __future__ import annotations

from typing import Dict

SPECIES_LABELS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


def predict_iris(features: Dict[str, float]) -> Dict[str, object]:
    """Return a placeholder prediction for validated Iris features.

    Note:
        This service intentionally shields routes from model details.
        It currently returns a deterministic placeholder prediction.
    """
    _ = features

    predicted_class_index = 0
    predicted_class_label = SPECIES_LABELS[predicted_class_index]

    return {
        "predicted_class_index": predicted_class_index,
        "predicted_class_label": predicted_class_label,
    }
