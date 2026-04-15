"""Flask app entry point for Iris demo site."""

from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "Iris Demo Site"


if __name__ == "__main__":
    app.run(debug=True)
