from flask import jsonify, Blueprint, request
from api.bug.controller import Bug_Controller

bug_bp = Blueprint("bug", __name__)


@bug_bp.route("/", methods=["GET"])
async def get_bugs():
    try:
        bugs = await Bug_Controller["query"]()
        return jsonify(bugs)
    except:
        return jsonify({"message": f"Internal error"}), 500


@bug_bp.route("/<bug_id>", methods=["GET"])
async def get_bug_by_id(bug_id):
    try:
        bug = await Bug_Controller["get_bug_by_id"](bug_id)
        return jsonify(bug)
    except:
        return jsonify({"message": f"Internal error"}), 500


@bug_bp.route("/<bug_id>", methods=["DELETE"])
async def remove_bug(bug_id):
    try:
        bugs = await Bug_Controller["remove_bug"](bug_id)
        return jsonify(bugs)
    except:
        return jsonify({"message": f"Internal error"}), 500


@bug_bp.route("/", methods=["POST"])
async def add_bug():
    try:
        bug_data = request.get_json()
        bugs = await Bug_Controller["add_bug"](bug_data)
        return jsonify(bugs), 201
    except:
        return jsonify({"message": f"Internal error"}), 500


@bug_bp.route("/", methods=["PUT"])
async def update_bug():
    try:
        bug_data = request.get_json()
        bugs = await Bug_Controller["update_bug"](bug_data)
        return jsonify(bugs), 201
    except:
        return jsonify({"message": f"Internal error"}), 500
