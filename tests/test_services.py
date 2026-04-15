import unittest
from unittest.mock import patch

from services.prediction_service import get_class_image_path, predict_from_raw_input, predict_iris


class PredictionServiceTests(unittest.TestCase):
    def test_get_class_image_path_supports_all_expected_class_labels(self):
        self.assertEqual(get_class_image_path("Iris-setosa"), "images/iris-setosa.svg")
        self.assertEqual(get_class_image_path("Iris-versicolor"), "images/iris-versicolor.svg")
        self.assertEqual(get_class_image_path("Iris-virginica"), "images/iris-virginica.svg")
        self.assertEqual(get_class_image_path("setosa"), "images/iris-setosa.svg")

    def test_get_class_image_path_returns_none_for_unknown_class(self):
        self.assertIsNone(get_class_image_path("Iris-unknown"))

    def test_predict_iris_includes_image_path_in_result_payload(self):
        features = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        }

        with patch("services.prediction_service.predict_species", return_value="versicolor"):
            result = predict_iris(features)

        self.assertEqual(
            result,
            {
                "predicted_class_index": 1,
                "predicted_class_label": "Iris-versicolor",
                "predicted_class_image_path": "images/iris-versicolor.svg",
            },
        )

    def test_predict_iris_returns_none_image_when_class_is_unknown(self):
        features = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        }

        with patch("services.prediction_service.predict_species", return_value="mystery-class"):
            result = predict_iris(features)

        self.assertEqual(result["predicted_class_label"], "mystery-class")
        self.assertIsNone(result["predicted_class_image_path"])

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
