"""Application factory for the Customer Accounts service."""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
from service.routes import accounts_blueprint


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY="development-only-change-me", JSON_SORT_KEYS=False)
    if test_config:
        app.config.update(test_config)

    Talisman(
        app,
        force_https=app.config.get("TALISMAN_FORCE_HTTPS", False),
        content_security_policy={
            "default-src": ["'self'"],
            "img-src": ["'self'", "data:"],
            "style-src": ["'self'", "'unsafe-inline'"],
            "script-src": ["'self'"],
        },
    )
    CORS(
        app,
        resources={r"/accounts*": {"origins": app.config.get("CORS_ORIGINS", "*")}},
        supports_credentials=False,
    )
    app.register_blueprint(accounts_blueprint)

    @app.get("/")
    def index():
        return jsonify({"service": "Customer Accounts", "status": "running"}), 200

    return app


app = create_app()
