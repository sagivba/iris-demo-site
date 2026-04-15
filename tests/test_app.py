"""Tests for browser-facing Flask routes."""

import unittest

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

    def test_predict_form_submission_success(self) -> None:
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
        self.assertIn(b"setosa", response.data)

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
        self.assertIn(b"sepal_length is required", response.data)
        self.assertIn(b"sepal_width must be a valid number", response.data)


if __name__ == "__main__":
    unittest.main()
