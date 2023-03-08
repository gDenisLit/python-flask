from util_service import make_id
import json
import time

with open("./data/bug.json", "r") as f:
    bugs = json.load(f)


def query():
    return bugs


def get_by_id(bug_id):
    for bug in bugs:
        if bug["_id"] == bug_id:
            return bug
    return None


def update_bug(new_bug):
    idx = -1
    for i, bug in enumerate(bugs):
        if bug["_id"] == new_bug["_id"]:
            idx = i
            break

    if idx >= 0:
        bugs[idx] = new_bug

    save_bugs()
    return bugs


def add_bug(title, severity):
    bug = create_bug(title, severity)
    bugs.append(bug)
    save_bugs()
    return bugs


def remove_bug(bug_id):
    bug = get_by_id(bug_id)
    bugs.remove(bug)
    save_bugs()
    return bugs


def save_bugs():
    with open("./data/bug.json", "w") as outfile:
        json.dump(bugs, outfile, indent=4)


def create_bug(title, severity):
    return {
        "_id": make_id(),
        "title": title,
        "severity": severity,
        "createdAt": time.time(),
    }


Bug_Service = {
    "query": query,
    "get_by_id": get_by_id,
    "update_bug": update_bug,
    "add_bug": add_bug,
    "remove_bug": remove_bug,
}
