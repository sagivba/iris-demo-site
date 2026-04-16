import unittest
from unittest.mock import MagicMock, patch

from model.predictor import IrisPredictor, _coerce_features, predict_iris, predict_species


class ModelPredictorTests(unittest.TestCase):
    def test_coerce_features_orders_mapping_by_expected_fields(self):
        model_input = _coerce_features(
            {
                "petal_width": 0.2,
                "sepal_width": 3.5,
                "sepal_length": 5.1,
                "petal_length": 1.4,
            }
        )

        self.assertEqual(model_input, [[5.1, 3.5, 1.4, 0.2]])

    def test_coerce_features_supports_sequence_input(self):
        model_input = _coerce_features([5.1, 3.5, 1.4, 0.2])
        self.assertEqual(model_input, [[5.1, 3.5, 1.4, 0.2]])

    def test_predict_species_maps_numeric_prediction_to_label(self):
        mock_model = MagicMock()
        mock_model.predict.return_value = [1]

        with patch("model.predictor.load_model", return_value=mock_model):
            result = predict_species([[6.2, 2.8, 4.8, 1.8]])

        self.assertEqual(result, "versicolor")

    def test_predict_species_returns_string_prediction_as_is(self):
        mock_model = MagicMock()
        mock_model.predict.return_value = ["virginica"]

        with patch("model.predictor.load_model", return_value=mock_model):
            result = predict_species([[6.4, 2.9, 5.6, 2.1]])

        self.assertEqual(result, "virginica")

    def test_predict_iris_delegates_to_predict_species(self):
        with patch("model.predictor.predict_species", return_value="setosa") as mock_predict:
            result = predict_iris(
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2,
                }
            )

        self.assertEqual(result, "setosa")
        mock_predict.assert_called_once_with([[5.1, 3.5, 1.4, 0.2]])

    def test_iris_predictor_class_exposes_predict_method(self):
        predictor = IrisPredictor()

        with patch("model.predictor.predict_iris", return_value="setosa") as mock_predict:
            result = predictor.predict([5.1, 3.5, 1.4, 0.2])

        self.assertEqual(result, "setosa")
        mock_predict.assert_called_once_with([5.1, 3.5, 1.4, 0.2])


if __name__ == "__main__":
    unittest.main()
