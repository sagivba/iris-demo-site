# CODEX Prompt Bundle 02 - Backend Prediction Core

מטרה: לממש את ליבת המערכת - טעינת מודל, ולידציה, שירות חיזוי וניתוב בקשה.
בסיום המקבץ יש לבצע review, להריץ בדיקות רלוונטיות, ואז pull.

---

## TASK 1 - שכבת המודל

```text
You are working in the iris-demo-site repository.

Goal:
Implement the model layer for Iris prediction.

Functional intent:
- The system receives 4 numeric Iris features.
- The model layer loads or initializes a trained Iris classifier.
- The model layer exposes a stable prediction interface.

Requirements:
- Create or update files under model/.
- Expose a clear function or class for prediction.
- Return a normalized prediction result.
- Map model output to one of:
  - setosa
  - versicolor
  - virginica

Constraints:
- Keep the implementation simple.
- Prefer a preloaded or cached model pattern if appropriate.
- Do not implement model training through the UI.
- Do not introduce database usage.
- Do not over-engineer abstraction layers.

At the end:
- Describe the public interface of the model layer.
```

---

## TASK 2 - קלט וולידציה

```text
You are working in the iris-demo-site repository.

Goal:
Implement input validation for the four Iris features.

Input fields:
- sepal_length
- sepal_width
- petal_length
- petal_width

Requirements:
- All four fields are required.
- All values must be numeric.
- Reject empty, missing, or non-numeric values.
- Produce clear validation errors.

Constraints:
- Keep validation logic centralized and testable.
- Do not couple validation directly to HTML rendering.
- Optional range checks may be added only if implemented conservatively.

Expected outcome:
- A reusable validation function or module under services/ or a clearly appropriate location.
- Structured errors that routes can consume.

At the end:
- Summarize validation rules implemented.
```

---

## TASK 3 - שכבת השירות

```text
You are working in the iris-demo-site repository.

Goal:
Implement the prediction service layer.

Responsibilities:
- accept raw input
- validate input
- normalize or cast values
- prepare model input
- call the model layer
- return a stable response object

Constraints:
- Keep business logic out of routes.
- Do not render HTML inside the service layer.
- Keep the output format consistent for success and failure paths.

Suggested success shape:
{
  "ok": true,
  "prediction": "setosa"
}

Suggested error shape:
{
  "ok": false,
  "errors": [...]
}

At the end:
- Explain what the service expects as input and what it returns.
```

---

## TASK 4 - שכבת הניתוב

```text
You are working in the iris-demo-site repository.

Goal:
Implement the HTTP routes required for the Iris demo app.

Minimum routes:
- route for the main page
- route for prediction form submission

Requirements:
- The prediction route must call the service layer, not the model directly.
- Handle success and validation errors cleanly.
- Keep route handlers thin.
- Make the implementation consistent with the existing app entrypoint.

Constraints:
- Do not add authentication.
- Do not add unrelated API endpoints.
- Do not add persistence.
- Keep the routing readable and minimal.

At the end:
- Summarize the routes and their responsibilities.
```
