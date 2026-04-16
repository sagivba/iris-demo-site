# iris-demo-site

A small Flask-based Iris prediction demo intended as a clean reference structure for ML-backed web apps.

## Purpose

This project demonstrates a simple end-to-end flow for:
- collecting Iris flower measurements in a web form,
- validating those inputs,
- returning a predicted Iris class,
- rendering the result in the same page.

It prioritizes clear layering (`routes` → `services` → `model`) and `unittest` coverage.

## Current Architecture Overview

- `app.py` creates the Flask app and registers the web blueprint.
- `routes/web.py` handles browser requests (`/` and `/predict`) and template rendering.
- `services/validation_service.py` validates required numeric input fields.
- `services/prediction_service.py` orchestrates prediction responses for web/API-style contracts.
- `model/predictor.py` provides model-loading and prediction utilities.
- `templates/` and `static/` provide the UI.

Notes about current implementation state:
- `routes/api.py` exists but currently has no route implementation.
- `model/train.py` exists but is currently empty.
- `Dockerfile` exists but is currently empty.

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── TODO.md
├── docs/
│   └── dev-python.md
├── model/
│   ├── __init__.py
│   ├── predictor.py
│   └── train.py
├── routes/
│   ├── __init__.py
│   ├── api.py
│   └── web.py
├── services/
│   ├── __init__.py
│   ├── prediction_service.py
│   └── validation_service.py
├── static/
│   ├── style.css
│   └── images/
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
└── tests/
    ├── __init__.py
    ├── test_api.py
    ├── test_app.py
    ├── test_model_predictor.py
    ├── test_services.py
    └── test_validation_service.py
```

## Setup (WSL + Conda)

```bash
conda create -n iris-demo python=3.11 -y
conda activate iris-demo
pip install -r requirements.txt
```

## Environment Variables

No environment variables are required by the current codebase for local run.

## Run Locally

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Run Tests

```bash
python -m unittest discover -v
```

## Main Routes / Flows

### Web Flow
- `GET /` renders the Iris input form.
- `POST /predict` validates input and renders either:
  - validation errors (HTTP 400),
  - prediction output in-page (HTTP 200),
  - generic failure message on prediction exceptions (HTTP 500).

### API Flow
- No API route is currently implemented in `routes/api.py`.

## Technologies Used

From `requirements.txt`:
- Flask
- scikit-learn
- joblib
- gunicorn

## Current Project Status

The browser-based prediction flow is implemented and covered by unit tests. API routing and model training script implementation are not yet completed.

## Known Gaps / Near-Term Next Steps

- Implement and register API prediction route(s).
- Add API-focused tests once routes exist.
- Implement `model/train.py` training workflow or remove placeholder until needed.
- Either wire or remove `templates/result.html` to avoid unused template drift.
