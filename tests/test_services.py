import unittest

from services.validation_service import validate_iris_features


class ValidationServiceTestCase(unittest.TestCase):
    def test_validate_iris_features_accepts_valid_numeric_input(self):
        payload = {
            "sepal_length": "5.1",
            "sepal_width": 3,
            "petal_length": "1.4",
            "petal_width": 0.2,
        }

        result = validate_iris_features(payload)

        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(
            result["data"],
            {
                "sepal_length": 5.1,
                "sepal_width": 3.0,
                "petal_length": 1.4,
                "petal_width": 0.2,
            },
        )

    def test_validate_iris_features_rejects_missing_fields(self):
        result = validate_iris_features({"sepal_length": 5.1})

        self.assertFalse(result["is_valid"])
        self.assertEqual(result["data"], {})
        self.assertEqual(len(result["errors"]), 3)
        self.assertEqual(result["errors"][0]["code"], "required")

    def test_validate_iris_features_rejects_empty_or_none_values(self):
        payload = {
            "sepal_length": "",
            "sepal_width": "   ",
            "petal_length": None,
            "petal_width": 0.2,
        }

        result = validate_iris_features(payload)

        self.assertFalse(result["is_valid"])
        self.assertEqual(result["data"], {})
        error_fields = {error["field"] for error in result["errors"]}
        self.assertSetEqual(
            error_fields,
            {"sepal_length", "sepal_width", "petal_length"},
        )

    def test_validate_iris_features_rejects_non_numeric_values(self):
        payload = {
            "sepal_length": "abc",
            "sepal_width": object(),
            "petal_length": "NaN",
            "petal_width": "1.0",
        }

        result = validate_iris_features(payload)

        self.assertFalse(result["is_valid"])
        self.assertEqual(result["data"], {})
        self.assertEqual(len(result["errors"]), 3)
        for error in result["errors"]:
            self.assertEqual(error["code"], "not_numeric")


if __name__ == "__main__":
    unittest.main()
