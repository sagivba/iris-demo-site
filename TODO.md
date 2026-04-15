# TODO

## Goal

Build a small but complete Flask-based reference implementation for an ML web app using the Iris dataset.

This TODO is intentionally split into small, reviewable tasks for AI-assisted execution.
Run one task at a time.
If a task depends on a previous task, wait for the previous task to finish and be reviewed before continuing.

## Global rules for every task

- Use Flask.
- Develop for WSL + Conda + VS Code.
- Use `unittest` only. Do not introduce `pytest`.
- Keep diffs small and focused.
- Do not perform broad refactors unless explicitly requested.
- Do not add a database.
- Do not add a JavaScript framework.
- Do not retrain the model during requests.
- Keep route handlers thin.
- Keep ML logic out of route handlers.
- Keep dependencies minimal.
- Update docs when behavior, commands, or structure change.
- Keep CI green.

## Dependency order

Run tasks in this order unless explicitly stated otherwise.

- Task 01 -> Task 02 -> Task 03 -> Task 04 -> Task 05 -> Task 06 -> Task 07 -> Task 08 -> Task 09 -> Task 10 -> Task 11 -> Task 12 -> Task 13 -> Task 14

Do not skip required predecessors.

---

## Task 01 - Fill bootstrap files with minimal initial content

### Depends on
- Existing repo skeleton already created

### Objective
Add minimal initial content so the repo is no longer empty and can be opened cleanly in VS Code and GitHub.

### Scope
Update only:
- `README.md`
- `requirements.txt`
- `.gitignore`
- `.env`
- `app.py`
- `routes/__init__.py`
- `routes/web.py`
- `routes/api.py`
- `services/__init__.py`
- `services/prediction_service.py`
- `services/validation_service.py`
- `model/__init__.py`
- `model/train.py`
- `model/predictor.py`
- `templates/base.html`
- `templates/index.html`
- `templates/result.html`
- `static/style.css`
- `tests/__init__.py`
- `tests/test_app.py`
- `tests/test_api.py`
- `tests/test_services.py`
- `docs/dev-python.md`
- `.vscode/settings.json`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.github/workflows/ci.yml`

### Deliverable
- Minimal placeholders only
- No real ML logic yet
- No broken imports
- App should at least import cleanly

### Stop after completion
Wait before moving to Task 02.

---

## Task 02 - Make Flask app runnable with a minimal home page

### Depends on
- Task 01

### Objective
Create a minimal runnable Flask application.

### Scope
Implement:
- `app.py`
- `routes/web.py`
- `templates/base.html`
- `templates/index.html`
- `static/style.css`

### Requirements
- `/` must return HTTP 200
- Page should render a simple Iris input form shell
- Form fields may exist as placeholders, but no prediction flow yet
- Keep app structure simple and explicit

### Deliverable
- `python app.py` starts Flask locally
- Home page renders successfully

### Stop after completion
Wait before moving to Task 03.

---

## Task 03 - Add VS Code and local Python workflow configuration

### Depends on
- Task 01

### Objective
Make the repo comfortable to use from VS Code in WSL with Conda and unittest discovery.

### Scope
Implement or refine:
- `.vscode/settings.json`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.env`
- `docs/dev-python.md`

### Requirements
- unittest discovery works from VS Code
- CLI test command is documented
- Flask launch config exists
- tasks for run, test, and train are defined if practical
- `PYTHONPATH` handling is documented clearly

### Deliverable
- Clean local developer workflow documentation and config

### Stop after completion
Wait before moving to Task 04.

---

## Task 04 - Implement Iris training pipeline and persist model

### Depends on
- Task 02
- Task 03

### Objective
Train a simple Iris model from scikit-learn and save it to disk.

### Scope
Implement:
- `model/train.py`
- `model/predictor.py`
- `requirements.txt`
- `README.md`
- `docs/dev-python.md`

### Requirements
- Use Iris dataset from scikit-learn
- Train a simple model
- Save the trained artifact to a file
- Do not train during request handling
- Keep implementation simple and explicit
- Document the train command

### Deliverable
- A reproducible training command
- A persisted model artifact path defined by the project

### Stop after completion
Wait before moving to Task 05.

---

## Task 05 - Add model loading utility and prediction service

### Depends on
- Task 04

### Objective
Load the persisted model and expose prediction logic through the service layer.

### Scope
Implement:
- `model/predictor.py`
- `services/prediction_service.py`

### Requirements
- Load model from disk
- Expose a function that accepts the 4 Iris numeric inputs
- Return both predicted class index and label
- Keep service independent from Flask request objects
- Keep route handlers free of ML logic

### Deliverable
- Prediction service callable from future web and API routes

### Stop after completion
Wait before moving to Task 06.

---

## Task 06 - Add input validation service

### Depends on
- Task 05

### Objective
Create explicit validation for the 4 numeric input fields.

### Scope
Implement:
- `services/validation_service.py`

### Requirements
- Validate required fields
- Validate numeric conversion
- Return clear structured errors
- Keep validation reusable for both form and API usage
- Do not hide behavior in decorators or magic abstractions

### Deliverable
- Reusable validation flow for UI and API

### Stop after completion
Wait before moving to Task 07.

---

## Task 07 - Implement HTML form submission and result page

### Depends on
- Task 05
- Task 06

### Objective
Complete the browser flow from form input to prediction result page.

### Scope
Implement:
- `routes/web.py`
- `templates/index.html`
- `templates/result.html`
- `templates/base.html`
- `static/style.css`

### Requirements
- Home page form contains:
  - `sepal_length`
  - `sepal_width`
  - `petal_length`
  - `petal_width`
- Form submission triggers validation
- Valid submission returns a result page
- Result page shows:
  - all input values
  - predicted label
- Invalid submission shows a clear user-facing error path

### Deliverable
- End-to-end prediction flow through HTML

### Stop after completion
Wait before moving to Task 08.

---

## Task 08 - Implement JSON API endpoint

### Depends on
- Task 05
- Task 06

### Objective
Add internal prediction API endpoint.

### Scope
Implement:
- `routes/api.py`
- `app.py` if route registration needs it

### Requirements
- Add `POST /api/predict`
- Accept JSON body with the 4 fields
- On success, return JSON with:
  - `predicted_class_index`
  - `predicted_class_label`
- On invalid input, return clear JSON error response
- Keep route handler thin

### Deliverable
- Working JSON prediction endpoint

### Stop after completion
Wait before moving to Task 09.

---

## Task 09 - Add app tests for web and API flows

### Depends on
- Task 07
- Task 08

### Objective
Add `unittest` coverage for the Flask app behavior.

### Scope
Implement:
- `tests/test_app.py`
- `tests/test_api.py`

### Requirements
Add tests for:
- home page loads
- valid form submission
- invalid form submission
- valid API request
- invalid API request

### Deliverable
- Tests pass with:
  - `python -m unittest discover -v`

### Stop after completion
Wait before moving to Task 10.

---

## Task 10 - Add prediction service unit tests

### Depends on
- Task 05
- Task 06

### Objective
Add focused service-level unit tests.

### Scope
Implement:
- `tests/test_services.py`

### Requirements
- Test prediction service success path
- Test validation behavior
- Keep tests deterministic
- Do not require network access
- Avoid heavy integration setup

### Deliverable
- Service-layer test coverage using `unittest`

### Stop after completion
Wait before moving to Task 11.

---

## Task 11 - Improve README for full project usage

### Depends on
- Task 04
- Task 07
- Task 08
- Task 09
- Task 10

### Objective
Turn `README.md` into a complete project guide.

### Scope
Update:
- `README.md`

### Requirements
Document:
- project purpose
- repository structure
- Conda environment setup
- dependency installation
- training command
- app run command
- test command
- API usage example
- optional Docker usage
- architecture summary

### Deliverable
- A strong top-level README for humans and AI agents

### Stop after completion
Wait before moving to Task 12.

---

## Task 12 - Improve developer documentation

### Depends on
- Task 03
- Task 09
- Task 10
- Task 11

### Objective
Complete local workflow documentation.

### Scope
Update:
- `docs/dev-python.md`

### Requirements
Document:
- WSL workflow
- VS Code usage
- unittest discovery
- available tasks
- Flask run/debug flow
- common troubleshooting
- how to re-train model
- how to run tests from CLI and VS Code

### Deliverable
- Developer workflow doc aligned with actual repo behavior

### Stop after completion
Wait before moving to Task 13.

---

## Task 13 - Finalize CI workflow

### Depends on
- Task 09
- Task 10

### Objective
Add or refine GitHub Actions CI.

### Scope
Update:
- `.github/workflows/ci.yml`

### Requirements
- Run on `push`
- Run on `pull_request`
- Install dependencies
- Run `python -m unittest discover -v`
- Keep workflow simple

### Deliverable
- Working basic CI pipeline

### Stop after completion
Wait before moving to Task 14.

---

## Task 14 - Add optional Docker support

### Depends on
- Task 11
- Task 12
- Task 13

### Objective
Add a simple Docker run path without changing the primary local workflow.

### Scope
Implement or update:
- `Dockerfile`
- `README.md`

### Requirements
- Docker support is optional only
- Main workflow remains WSL + Conda + VS Code
- Keep Dockerfile simple
- Do not redesign project layout around Docker

### Deliverable
- Optional containerized run mode documented clearly

### Stop after completion
This is the last planned task.

---

## Execution notes for Codex

- Run one task at a time.
- After each task, stop and wait.
- If a task requires a previous task, do not continue until that task is completed.
- Do not combine multiple tasks into one large change.
- Do not add features that belong to later tasks.
- Keep documentation aligned with every meaningful change.
- Keep imports, naming, and structure explicit and easy to follow.

## Recommended first task to run

Start with:
- Task 01 - Fill bootstrap files with minimal initial content
