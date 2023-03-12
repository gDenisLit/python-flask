from api.bug.service import Bug_Service


async def _query():
    try:
        bugs = await Bug_Service["query"]()
        return bugs
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


async def _get_bug_by_id(bug_id):
    try:
        bug = await Bug_Service["get_by_id"](bug_id)
        return bug
    except Exception as e:
        print({"message": f"Error getting bug by id: {e}"})


async def _remove_bug(bug_id):
    try:
        bugs = await Bug_Service["remove_bug"](bug_id)
        return bugs
    except Exception as e:
        print({"message": f"Error removing bug: {e}"})


async def _add_bug(bug_data):
    try:
        bugs = await Bug_Service["add_bug"](bug_data)
        return bugs
    except Exception as e:
        print({"message": f"Error adding bug: {e}"})


async def _update_bug(bug_data):
    try:
        bugs = await Bug_Service["update_bug"](bug_data)
        return bugs, 201
    except Exception as e:
        print({"message": f"Error updating bug: {e}"})


Bug_Controller = {
    "query": _query,
    "get_bug_by_id": _get_bug_by_id,
    "remove_bug": _remove_bug,
    "add_bug": _add_bug,
    "update_bug": _update_bug,
}
