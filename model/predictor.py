"""Model loading and prediction utilities."""

from functools import lru_cache
from pathlib import Path
from typing import Any

MODEL_FILE = Path(__file__).resolve().parent / "iris_model.joblib"
CLASS_LABELS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


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
