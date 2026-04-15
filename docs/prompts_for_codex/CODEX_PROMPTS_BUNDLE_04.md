# CODEX Prompt Bundle 04 - Tests and Quality Gate

מטרה: להוסיף בדיקות ממוקדות עבור הדמו ולוודא שהפרויקט ניתן להרצה מקומית בצורה מסודרת.
בסיום המקבץ יש לבצע review, להריץ את כלל הבדיקות, ואז pull.

---

## TASK 1 - בדיקות

```text
You are working in the iris-demo-site repository.

Goal:
Add a focused automated test suite for the Iris demo application.

Testing requirements:
- Use Python unittest, not pytest.
- Add tests for:
  - input validation
  - prediction service
  - model prediction interface
  - main routes
- Cover both success and failure cases.
- Keep tests readable and small.

Constraints:
- Do not add large testing frameworks beyond unittest usage.
- Avoid brittle tests tied to incidental HTML formatting.
- Test behavior, not implementation noise.

At the end:
- Summarize test coverage by module and scenario.
```

---

## TASK 2 - תלויות וסביבת עבודה

```text
You are working in the iris-demo-site repository.

Goal:
Verify the repository can be run locally with a simple developer workflow.

Requirements:
- Ensure the README run instructions match the actual code.
- Confirm dependency setup aligns with the implemented app.
- If a simple local startup command is missing, add it to documentation or code as appropriate.
- Keep the workflow straightforward.

Constraints:
- Do not introduce unnecessary deployment tooling.
- Docker is optional; add it only if already present and clearly useful.
- Do not add environment complexity without need.

At the end:
- Provide the exact local commands needed to install, run, and test the app.
```

---

## TASK 3 - Definition of Done

```text
You are working in the iris-demo-site repository.

Goal:
Perform a final quality pass against the project MVP expectations.

Check and fix where needed:
- user can enter 4 features
- invalid input is blocked or handled correctly
- prediction can be triggered from the UI
- output is one of the 3 valid Iris classes
- result is displayed clearly
- basic tests exist and pass
- project runs locally
- repository state remains clean and coherent

Constraints:
- Make only targeted fixes needed to satisfy the MVP.
- Do not expand scope.
- Keep changes practical and minimal.

At the end:
- Produce a short MVP readiness summary.
```
