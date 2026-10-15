from __future__ import annotations

from collections import deque


def process_deque(commands: list[tuple[str, object]]) -> tuple[list[object], list[object]]:
    # TODO: complete the numbered steps for this function.
    waiting = deque()
    removed = []
    for operation, value in commands:
        if operation == "right":
            pass
        elif operation == "left":
            pass
        elif operation == "take_left":
            pass
        elif operation == "take_right":
            pass
        else:
            pass
    return removed, list(waiting)


if __name__ == "__main__":
    try:
        print(process_deque([("right", "A"), ("left", "B"), ("take_right", None)]))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
