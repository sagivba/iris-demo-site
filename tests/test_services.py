import unittest
from unittest.mock import patch

from services.prediction_service import predict_from_raw_input


class PredictionServiceTests(unittest.TestCase):
    def test_predict_from_raw_input_returns_prediction_on_success(self):
        raw_input = {
            "sepal_length": "5.1",
            "sepal_width": "3.5",
            "petal_length": "1.4",
            "petal_width": "0.2",
        }

        with patch("services.prediction_service.predict_species", return_value="setosa") as mock_predict:
            result = predict_from_raw_input(raw_input)

        self.assertEqual(result, {"ok": True, "prediction": "setosa"})
        mock_predict.assert_called_once_with([[5.1, 3.5, 1.4, 0.2]])

    def test_predict_from_raw_input_returns_validation_errors(self):
        raw_input = {
            "sepal_length": "5.1",
            "sepal_width": "not-a-number",
            "petal_length": "1.4",
        }

        result = predict_from_raw_input(raw_input)

        self.assertFalse(result["ok"])
        self.assertIn("errors", result)
        self.assertIn("sepal_width must be a numeric value.", result["errors"])
        self.assertIn("petal_width is required.", result["errors"])

    def test_predict_from_raw_input_returns_stable_model_error(self):
        raw_input = {
            "sepal_length": "6.0",
            "sepal_width": "3.0",
            "petal_length": "4.8",
            "petal_width": "1.8",
        }

        with patch("services.prediction_service.predict_species", side_effect=RuntimeError("boom")):
            result = predict_from_raw_input(raw_input)

        self.assertEqual(
            result,
            {
                "ok": False,
                "errors": ["Prediction failed. Ensure the trained model is available."],
            },
        )


if __name__ == "__main__":
    unittest.main()
