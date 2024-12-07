from flask import Flask, request, jsonify
from supabase_client import (
    create_user,
    create_post,
    change_status,
    create_beef,
    fetch_posts,
    fetch_beefs,
    ban,
    check_is_banned,
    add_penalty,
    check_penalties,
    user_metadata
)

app = Flask(__name__)

@app.route("/create_user", methods=["POST"])
def create_user_endpoint():
    data = request.json
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    response = create_user(email)
    return jsonify(response)

@app.route("/create_post", methods=["POST"])
def create_post_endpoint():
    data = request.json
    user_id = data.get("user_id")
    topic_name = data.get("topic_name")
    topic_desc = data.get("topic_desc")
    if not (user_id and topic_name and topic_desc):
        return jsonify({"error": "user_id, topic_name, and topic_desc are required"}), 400
    response = create_post(user_id, topic_name, topic_desc)
    return jsonify(response)

@app.route("/change_status", methods=["PUT"])
def change_status_endpoint():
    data = request.json
    post_id = data.get("post_id")
    new_status = data.get("new_status")
    if not (post_id and new_status):
        return jsonify({"error": "post_id and new_status are required"}), 400
    response = change_status(post_id, new_status)
    return jsonify(response)

@app.route("/create_beef", methods=["POST"])
def create_beef_endpoint():
    data = request.json
    topic_id = data.get("topic_id")
    user_id_1 = data.get("user_id_1")
    user_id_2 = data.get("user_id_2")
    if not (topic_id and user_id_1 and user_id_2):
        return jsonify({"error": "topic_id, user_id_1, and user_id_2 are required"}), 400
    response = create_beef(topic_id, user_id_1, user_id_2)
    return jsonify(response)

@app.route("/fetch_posts", methods=["GET"])
def fetch_posts_endpoint():
    response = fetch_posts()
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
    app.run(debug=True, host="0.0.0.0", port=8080)

