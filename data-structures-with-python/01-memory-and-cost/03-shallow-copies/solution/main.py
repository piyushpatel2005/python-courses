from __future__ import annotations
from typing import Any

def copy_outer(items: list[Any]) -> list[Any]:
    return list(items)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        card = ["queued"]
        original = [card]
        copy = copy_outer(original)
        print(copy is original, copy[0] is card)
    except NotImplementedError as error:
        print("Not ready yet:", error)
