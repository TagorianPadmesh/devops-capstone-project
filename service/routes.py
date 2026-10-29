"""REST endpoints for customer accounts."""
from flask import Blueprint, jsonify, request
from service.models import store

accounts_blueprint = Blueprint("accounts", __name__)


def _validate_payload(payload, partial=False):
    if not isinstance(payload, dict):
        return "JSON object required"
    if not partial:
        missing = [
            field for field in ("name", "email", "address")
            if not str(payload.get(field, "")).strip()
        ]
        if missing:
            return "Missing required fields: " + ", ".join(missing)
    if "email" in payload and "@" not in str(payload["email"]):
        return "A valid email address is required"
    return None


@accounts_blueprint.post("/accounts")
def create_account():
    payload = request.get_json(silent=True)
    error = _validate_payload(payload)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(store.create(payload).serialize()), 201


@accounts_blueprint.get("/accounts")
def list_accounts():
    return jsonify([account.serialize() for account in store.all()]), 200


@accounts_blueprint.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = store.find(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account.serialize()), 200


@accounts_blueprint.put("/accounts/<int:account_id>")
def update_account(account_id):
    payload = request.get_json(silent=True)
    error = _validate_payload(payload, partial=True)
    if error:
        return jsonify({"error": error}), 400
    account = store.update(account_id, payload)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account.serialize()), 200


@accounts_blueprint.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    if store.delete(account_id) is None:
        return jsonify({"error": "Account not found"}), 404
    return "", 204
