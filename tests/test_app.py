"""Tests for browser-facing Flask routes."""

import unittest
from unittest.mock import patch

from app import create_app


class WebRoutesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home_page_loads(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Iris Predictor", response.data)
        self.assertIn(b'name="smiles"', response.data)
        self.assertIn(b"Submit", response.data)
        self.assertIn(b"Reset", response.data)
        self.assertIn(b"Errors", response.data)
        self.assertIn(b"Prediction Result", response.data)

    def test_predict_form_submission_success(self) -> None:
        with patch(
            "routes.web.predict_iris",
            return_value={
                "predicted_class_index": 0,
                "predicted_class_label": "Iris-setosa",
                "predicted_class_image_path": "images/iris-setosa.svg",
            },
        ):
            response = self.client.post(
                "/predict",
                data={
                    "sepal_length": "5.1",
                    "sepal_width": "3.5",
                    "petal_length": "1.4",
                    "petal_width": "0.2",
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Prediction Result", response.data)
        self.assertIn(b"Iris-setosa", response.data)
        self.assertIn(b"Example image of predicted class.", response.data)
        self.assertIn(b"static/images/iris-setosa.svg", response.data)

    def test_predict_form_submission_success_without_model_artifact(self) -> None:
        response = self.client.post(
            "/predict",
            data={
                "sepal_length": "5.1",
                "sepal_width": "3.5",
                "petal_length": "1.4",
                "petal_width": "0.2",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Iris-setosa", response.data)
        self.assertIn(b"static/images/iris-setosa.svg", response.data)

    def test_predict_form_submission_renders_image_fallback_message(self) -> None:
        with patch(
            "routes.web.predict_iris",
            return_value={
                "predicted_class_index": None,
                "predicted_class_label": "Iris-unknown",
                "predicted_class_image_path": None,
            },
        ):
            response = self.client.post(
                "/predict",
                data={
                    "sepal_length": "5.1",
                    "sepal_width": "3.5",
                    "petal_length": "1.4",
                    "petal_width": "0.2",
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Iris-unknown", response.data)
        self.assertIn(b"No example image available for this predicted class.", response.data)

    def test_predict_form_submission_validation_error(self) -> None:
        response = self.client.post(
            "/predict",
            data={
                "sepal_length": "",
                "sepal_width": "abc",
                "petal_length": "1.4",
                "petal_width": "0.2",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Sepal length is required.", response.data)
        self.assertIn(b"Sepal width must be a number (for example: 5.1).", response.data)
        self.assertIn(b"Iris Predictor", response.data)

    def test_predict_form_submission_internal_prediction_error(self) -> None:
        with patch("routes.web.predict_iris", side_effect=RuntimeError("model failed")):
            response = self.client.post(
                "/predict",
                data={
                    "sepal_length": "5.1",
                    "sepal_width": "3.5",
                    "petal_length": "1.4",
                    "petal_width": "0.2",
                },
            )

        self.assertEqual(response.status_code, 500)
        self.assertIn(
            b"We could not generate a prediction right now. Please try again in a moment.",
            response.data,
        )
        self.assertIn(b"Iris Predictor", response.data)
        self.assertNotIn(b"RuntimeError", response.data)


if __name__ == "__main__":
    unittest.main()
