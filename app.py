"""Application entrypoint for the Iris demo site."""

from flask import Flask

from routes.web import web_bp


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(web_bp)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
