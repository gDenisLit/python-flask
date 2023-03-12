import json
import time
import aiofiles
import random


async def load_bugs():
    async with aiofiles.open("./data/bug.json", "r") as f:
        data = await f.read()
        return json.loads(data)


async def query():
    return await load_bugs()


async def get_by_id(bug_id):
    bugs = await load_bugs()
    for bug in bugs:
        if bug["_id"] == bug_id:
            return bug
    raise ValueError(f"Bug with id {bug_id} not found")


async def remove_bug(bug_id):
    bugs = await load_bugs()
    for bug in bugs:
        if bug["_id"] == bug_id:
            bugs.remove(bug)
            await save_bugs(bugs)
            return bugs
    raise ValueError(f"Bug with id {bug_id} not found")


async def update_bug(new_bug):
    bugs = await query()
    idx = -1
    for i, bug in enumerate(bugs):
        if bug["_id"] == new_bug["_id"]:
            idx = i
            break

    print('found idx', idx)
    if idx >= 0:
        bugs[idx] = new_bug

    await save_bugs(bugs)
    return bugs


async def add_bug(new_bug):
    print('new ', new_bug)
    bug = create_bug(new_bug["title"], new_bug["severity"])
    bugs = await query()
    bugs.append(bug)
    await save_bugs(bugs)
    return bugs


async def save_bugs(bugs):
    async with aiofiles.open("./data/bug.json", "w") as f:
        await f.write(json.dumps(bugs))


def create_bug(title, severity):
    return {
        "_id": make_id(),
        "title": title,
        "severity": severity,
        "createdAt": time.time(),
    }


def make_id():
    alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
    str = ""
    for i in range(26):
        rand_idx = random.randint(0, len(alphabet) - 1)
        str += alphabet[rand_idx]

    return str


Bug_Service = {
    "query": query,
    "get_by_id": get_by_id,
    "update_bug": update_bug,
    "add_bug": add_bug,
    "remove_bug": remove_bug,
}
