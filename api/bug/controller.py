from api.bug.service import Bug_Service


async def query():
    try:
        bugs = await Bug_Service["query"]()
        return bugs
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


async def get_bug_by_id(bug_id):
    try:
        bug = await Bug_Service["get_by_id"](bug_id)
        return bug
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


async def remove_bug(bug_id):
    try:
        bugs = await Bug_Service["remove_bug"](bug_id)
        return bugs
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


async def add_bug(bug_data):
    try:
        bugs = await Bug_Service["add_bug"](bug_data)
        return bugs
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


async def update_bug(bug_data):
    try:
        bugs = await Bug_Service["update_bug"](bug_data)
        return bugs, 201
    except Exception as e:
        print({"message": f"Error creating bug: {e}"})


Bug_Controller = {
    "query": query,
    "get_bug_by_id": get_bug_by_id,
    "remove_bug": remove_bug,
    "add_bug": add_bug,
    "update_bug": update_bug,
}
