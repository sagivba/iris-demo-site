# iris-demo-site

A small **Flask-based Iris prediction demo** intended to show a clean project structure for ML-backed web apps.

> Current repository state (as of April 15, 2026): this repository is still in an early scaffold phase. Most Python source files are present but empty, so training, local app execution, and automated tests are not yet implemented.

## Project purpose

The intended system purpose is:

- receive 4 Iris flower features from a user
- run a trained prediction model
- return the predicted Iris class

The repository is designed as a simple reference template for this flow, with clear boundaries between routes, services, and model code.

## Short architecture overview

Intended layering:

- **Web/API routes** (`routes/`): HTTP handling only
- **Services** (`services/`): validation and prediction orchestration
- **Model utilities** (`model/`): training, loading, and inference helpers
- **Templates/static** (`templates/`, `static/`): UI rendering and styles
- **Entry point** (`app.py`): Flask startup wiring

This separation exists in folder layout today, but implementation is still pending.

## Folder structure overview

```text
.
├── app.py
├── model/
│   ├── predictor.py
│   └── train.py
├── routes/
│   ├── api.py
│   └── web.py
├── services/
│   ├── prediction_service.py
│   └── validation_service.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── tests/
│   ├── test_api.py
│   ├── test_app.py
│   └── test_services.py
├── requirements.txt
└── docs/
    └── dev-python.md
```

## Setup instructions

Primary development context for this repo is **WSL + Conda + VS Code**.

1. Create and activate a Conda environment (example):

   ```bash
   conda create -n iris-demo python=3.11 -y
   conda activate iris-demo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Note: `requirements.txt` is currently empty in this scaffold state.

## Local run instructions

A runnable Flask app is **not available yet** because `app.py` is currently empty.

Once app code is implemented, the expected command is:

```bash
python app.py
```

Current practical status: running that command does nothing meaningful until application code is added.

## Test run instructions

Test command for this repository:

```bash
python -m unittest discover -v
```

Current practical status: test files exist but are currently empty placeholders.

## Example input

Target prediction input format (planned behavior):

```text
sepal_length: 5.1
sepal_width: 3.5
petal_length: 1.4
petal_width: 0.2
```

## Example output

Target response format (planned behavior):

```text
Predicted class: setosa
```

Current practical status: prediction output is not available yet because model training/loading and route handling are not yet implemented.

## Current limitations

- Core Python implementation files are empty placeholders.
- No trained model artifact is present.
- No runnable web route or API behavior exists yet.
- No implemented validation flow for the 4 numeric inputs.
- No implemented end-to-end prediction flow.
- Tests are scaffolded but not yet populated with assertions.
- This project should be treated as a template scaffold, **not production-ready software**.

## Future improvements

- Implement Flask app bootstrap and home page route.
- Implement Iris model training and saved model artifact handling.
- Implement model loading and prediction service.
- Implement explicit input validation for all 4 features.
- Implement web form submission and result rendering.
- Implement JSON API endpoint for prediction.
- Add concrete `unittest` coverage for routes, services, and invalid input paths.
- Fill `requirements.txt`, developer docs, and CI workflow with working commands.

## Accuracy note

This README is intentionally aligned with the **current repository state**: architecture scaffolding is present, while executable application logic is still pending.
