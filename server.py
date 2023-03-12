from flask import Flask, jsonify, request, render_template
from api.bug.controller import get_bugs, get_bug_by_id, remove_bug, add_bug, update_bug

app = Flask(__name__)
app.static_folder = "public"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/bug", methods=["GET"])
async def get_bugs():
    try:
        bugs = await get_bugs()
        return jsonify(bugs)
    except:
        return jsonify({"message": f"Internal error"}), 500


@app.route("/api/bug/<bug_id>", methods=["GET"])
async def get_bug_by_id(bug_id):
    try:
        bug = await get_bug_by_id(bug_id)
        return jsonify(bug)
    except:
        return jsonify({"message": f"Internal error"}), 500


@app.route("/api/bug/<bug_id>", methods=["DELETE"])
async def remove_bug(bug_id):
    try:
        bugs = await remove_bug(bug_id)
        return jsonify(bugs)
    except:
        return jsonify({"message": f"Internal error"}), 500


@app.route("/api/bug", methods=["POST"])
async def add_bug():
    try:
        bug_data = request.get_json()
        bugs = await add_bug(bug_data)
        return jsonify(bugs), 201
    except:
        return jsonify({"message": f"Internal error"}), 500


@app.route("/api/bug", methods=["PUT"])
async def update_bug():
    try:
        bug_data = request.get_json()
        bugs = await update_bug(bug_data)
        return jsonify(bugs), 201
    except:
        return jsonify({"message": f"Internal error"}), 500


app.run(port=3030, debug=True)
