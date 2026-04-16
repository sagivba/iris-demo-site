import unittest

from services.validation_service import validate_iris_inputs


class ValidationServiceTests(unittest.TestCase):
    def test_validate_iris_inputs_returns_float_values_for_valid_input(self):
        values, errors = validate_iris_inputs(
            {
                "sepal_length": " 5.1 ",
                "sepal_width": "3.5",
                "petal_length": "1.4",
                "petal_width": "0.2",
            }
        )

        self.assertEqual(errors, [])
        self.assertEqual(
            values,
            {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            },
        )

    def test_validate_iris_inputs_returns_required_errors_when_fields_missing(self):
        values, errors = validate_iris_inputs({})

        self.assertEqual(values, {})
        self.assertEqual(
            errors,
            [
                "sepal_length is required.",
                "sepal_width is required.",
                "petal_length is required.",
                "petal_width is required.",
            ],
        )

    def test_validate_iris_inputs_returns_number_error_for_non_numeric_value(self):
        values, errors = validate_iris_inputs(
            {
                "sepal_length": "5.1",
                "sepal_width": "abc",
                "petal_length": "1.4",
                "petal_width": "0.2",
            }
        )

        self.assertEqual(values, {"sepal_length": 5.1, "petal_length": 1.4, "petal_width": 0.2})
        self.assertEqual(errors, ["sepal_width must be a valid number."])


if __name__ == "__main__":
    unittest.main()
