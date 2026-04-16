# Python development workflow

This repository is intended to be developed locally with:

- WSL
- VS Code connected to WSL
- a dedicated Conda environment
- `unittest`

## 1) Environment setup

```bash
conda create -n iris-demo python=3.11 -y
conda activate iris-demo
pip install -r requirements.txt
```

## 2) Run the app

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## 3) Run tests

```bash
python -m unittest discover -v
```

## Dependencies

Dependencies are defined in `requirements.txt`:

- Flask
- scikit-learn
- joblib

Install only from `requirements.txt` unless a task explicitly requires a new dependency.
