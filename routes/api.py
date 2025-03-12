from flask import Blueprint, request, jsonify
from services.db_service import get_comments_info, get_general_info

api_app = Blueprint("api", __name__)


@api_app.route("/api/comments/", methods=["GET"])
def get_comments():
    user_login = request.args.get("user_login")
    if not user_login:
        return jsonify({"error": "user_login is required"}), 400

    data = list(get_comments_info(user_login))

    return jsonify(data)


@api_app.route("/api/general/", methods=["GET"])
def get_user_activity_summary():
    user_login = request.args.get("user_login")
    if not user_login:
        return jsonify({"error": "user_login is required"}), 400

    data = list(get_general_info(user_login))
    print(data)
    return jsonify(data)
