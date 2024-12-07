from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase_client import (
    create_user,
    create_beef,
    change_beef_status,
    fetch_beefs,
    ban,
    check_is_banned,
    add_penalty,
    check_penalties,
    user_metadata
)

app = Flask(__name__)
CORS(app)
@app.route("/create_user", methods=["POST"])
def create_user_endpoint():
    data = request.json
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    response = create_user(email)
    return jsonify(response)

@app.route("/create_beef", methods=["POST"])
def create_beef_endpoint():
    data = request.json
    user_id = data.get("user_id")
    topic_name = data.get("topic_name")
    nsfw = data.get("nsfw", False)

    if not (user_id and topic_name):
        return jsonify({"error": "user_id, topic_name, and topic_desc are required"}), 400

    response = create_beef(user_id, topic_name, nsfw)
    return jsonify(response)

@app.route("/change_beef_status", methods=["PUT"])
def change_beef_status_endpoint():
    data = request.json
    beef_id = data.get("beef_id")
    new_status = data.get("new_status")
    if not (beef_id and new_status):
        return jsonify({"error": "beef_id and new_status are required"}), 400
    response = change_beef_status(beef_id, new_status)
    return jsonify(response)

@app.route("/fetch_beefs", methods=["GET"])
def fetch_beefs_endpoint():
    response = fetch_beefs()
    return jsonify(response)

@app.route("/ban", methods=["PUT"])
def ban_endpoint():
    data = request.json
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    response = ban(user_id)
    return jsonify(response)

@app.route("/check_is_banned", methods=["GET"])
def check_is_banned_endpoint():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    response = check_is_banned(user_id)
    return jsonify(response)

@app.route("/add_penalty", methods=["PUT"])
def add_penalty_endpoint():
    data = request.json
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    response = add_penalty(user_id)
    return jsonify(response)

@app.route("/check_penalties", methods=["GET"])
def check_penalties_endpoint():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    response = check_penalties(user_id)
    return jsonify(response)

@app.route("/user_metadata", methods=["GET"])
def user_metadata_endpoint():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    response = user_metadata(user_id)
    return jsonify(response)

if __name__ == "__main__":
    # Run on port 8080 as requested
    app.run(debug=True, host="0.0.0.0", port=8080)
