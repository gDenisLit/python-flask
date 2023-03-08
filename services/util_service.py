import random


def make_id():
    alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
    str = ""
    for i in range(26):
        rand_idx = random.randint(0, len(alphabet) - 1)
        str += alphabet[rand_idx]

    return str
