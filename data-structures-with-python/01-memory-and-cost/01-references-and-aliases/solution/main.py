from __future__ import annotations
from typing import Any

def append_shared(items: list[Any], value: Any) -> list[Any]:
    items.append(value)
    return items


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        supplies = ["tape"]
        print(append_shared(supplies, "twine"))
        print(supplies)
    except NotImplementedError as error:
        print("Not ready yet:", error)
