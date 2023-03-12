from flask import Flask, jsonify, request, send_file, render_template
import os
from services.bug_service import Bug_Service

app = Flask(__name__)
app.static_folder = "public"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/bug", methods=["GET"])
async def get_bugs():
    bugs = await Bug_Service["query"]()
    return jsonify(bugs)


@app.route("/api/bug/<bug_id>", methods=["GET"])
async def get_bug_by_id(bug_id):
    bug = await Bug_Service["get_by_id"](bug_id)
    return jsonify(bug)


@app.route("/api/bug/<bug_id>", methods=["DELETE"])
async def remove_bug(bug_id):
    bugs = await Bug_Service["remove_bug"](bug_id)
    return jsonify(bugs)


@app.route("/api/bug", methods=["POST"])
async def add_bug():
    try:
        bug_data = request.get_json()
        bugs = await Bug_Service.add_bug(bug_data)
        return jsonify(bugs), 201
    except Exception as e:
        return jsonify({"message": f"Error creating bug: {e}"}), 500


@app.route("/api/bug", methods=["PUT"])
async def update_bug():
    try:
        bug_data = request.get_json()
        print("bug data", bug_data)
        bugs = await Bug_Service.update_bug(bug_data)
        print(bugs)
        return jsonify(bugs), 201
    except Exception as e:
        return jsonify({"message": f"Error updating bug: {e}"}), 500


app.run(port=3030, debug=True)
