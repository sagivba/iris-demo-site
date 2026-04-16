# iris-demo-site

A small **Flask-based Iris prediction demo** that shows a clean, minimal structure for an ML-backed web app.

## What is implemented

- Browser flow for Iris input and prediction result rendering.
- Service-layer validation and prediction orchestration.
- Deterministic prediction logic for local/demo use.
- `unittest` test suite for web and service behaviors.

## Project structure

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
│   ├── style.css
│   └── images/
├── tests/
│   ├── test_api.py
│   ├── test_app.py
│   └── test_services.py
├── requirements.txt
└── docs/
    └── dev-python.md
```

## Local developer workflow (WSL + Conda)

1. Create and activate a Conda environment:

   ```bash
   conda create -n iris-demo python=3.11 -y
   conda activate iris-demo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:

   ```bash
   python app.py
   ```

4. Open:

   ```text
   http://127.0.0.1:5000
   ```

## Run tests

```bash
python -m unittest discover -v
```

## Notes

- Docker support is optional and not required for local development.
- The local run command above is the intended default workflow.
