import json
import time
import aiofiles
import random


async def _load_bugs():
    try:
        async with aiofiles.open("./data/bug.json", "r") as f:
            data = await f.read()
            return json.loads(data)
    except Exception as e:
        raise ValueError(f"Error reading bug.json")


async def _query():
    return await _load_bugs()


async def _get_by_id(bug_id):
    bugs = await _load_bugs()
    for bug in bugs:
        if bug["_id"] == bug_id:
            return bug
    raise ValueError(f"Bug with id {bug_id} not found")


async def _remove_bug(bug_id):
    bugs = await _load_bugs()
    for bug in bugs:
        if bug["_id"] == bug_id:
            bugs.remove(bug)
            await _save_bugs(bugs)
            return bugs
    raise ValueError(f"Error removing bug. Bug with {bug_id} not found")


async def _update_bug(new_bug):
    bugs = await _query()
    idx = -1
    for i, bug in enumerate(bugs):
        if bug["_id"] == new_bug["_id"]:
            idx = i
            break

    if idx < 0:
        raise ValueError(f"Error updating bug. Failed to find the original bug.")
    else:
        bugs[idx] = new_bug
        await _save_bugs(bugs)
        return bugs


async def _add_bug(new_bug):
    bug = _create_bug(new_bug["title"], new_bug["severity"])
    bugs = await _query()
    bugs.append(bug)
    await _save_bugs(bugs)
    return bugs


async def _save_bugs(bugs):
    try:
        async with aiofiles.open("./data/bug.json", "w") as f:
            await f.write(json.dumps(bugs))
    except Exception as e:
        raise ValueError(f"Error saving bugs to file")


def _create_bug(title, severity):
    return {
        "_id": _make_id(),
        "title": title,
        "severity": severity,
        "createdAt": time.time(),
    }


def _make_id():
    alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
    str = ""
    for i in range(26):
        rand_idx = random.randint(0, len(alphabet) - 1)
        str += alphabet[rand_idx]

    return str


Bug_Service = {
    "query": _query,
    "get_by_id": _get_by_id,
    "update_bug": _update_bug,
    "add_bug": _add_bug,
    "remove_bug": _remove_bug,
}
