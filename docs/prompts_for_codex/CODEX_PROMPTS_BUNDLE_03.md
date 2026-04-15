# CODEX Prompt Bundle 03 - UI and User Experience

מטרה: לבנות את שכבת הממשק עבור דמו Iris ולחבר אותה לליבת החיזוי שכבר מומשה.
בסיום המקבץ יש לבצע review, בדיקה ידנית, ואז pull.

---

## TASK 1 - ממשק משתמש

```text
You are working in the iris-demo-site repository.

Goal:
Implement the main user interface for the Iris demo web app.

UI requirements:
- A clear page title
- A short explanation of the demo
- A form with 4 numeric inputs:
  - sepal_length
  - sepal_width
  - petal_length
  - petal_width
- A predict button
- A visible area for result display
- A visible area for validation or system errors

Constraints:
- Keep the page simple and clean.
- Do not introduce heavy frontend frameworks.
- Use the existing templates/static structure.
- Do not add features not described in the spec.

At the end:
- Summarize which templates and static assets were changed.
```

---

## TASK 2 - תצוגת תוצאה

```text
You are working in the iris-demo-site repository.

Goal:
Improve result presentation after prediction.

Requirements:
- Show the predicted class clearly.
- Distinguish visually between success and error states.
- Preserve or re-display submitted values if appropriate.
- Keep the result area understandable for a demo audience.

Optional:
- Add a reset action if it can be done simply.

Constraints:
- Do not add charts yet.
- Do not add probabilities unless already returned by the backend.
- Keep the HTML structure maintainable.

At the end:
- Summarize the result-state UX behavior.
```

---

## TASK 3 - טיפול בשגיאות

```text
You are working in the iris-demo-site repository.

Goal:
Improve end-user error handling in the UI flow.

Requirements:
- Show user-friendly messages for invalid input.
- Handle internal prediction failures gracefully.
- Avoid raw stack traces or technical leaks in the UI.
- Ensure the page remains usable after an error.

Constraints:
- Keep developer diagnostics in code/logs, not in the rendered UI.
- Do not overcomplicate logging.
- Keep messages specific enough for correction.

At the end:
- List the main user-facing error scenarios handled.
```
