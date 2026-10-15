from __future__ import annotations

from collections import deque


def process_deque(commands: list[tuple[str, object]]) -> tuple[list[object], list[object]]:
    waiting = deque()
    removed = []
    for operation, value in commands:
        if operation == "left":
            waiting.appendleft(value)
        elif operation == "right":
            waiting.append(value)
        elif operation == "take_left":
            if waiting:
                removed.append(waiting.popleft())
        elif operation == "take_right":
            if waiting:
                removed.append(waiting.pop())
        else:
            raise ValueError("unknown operation")
    return removed, list(waiting)


if __name__ == "__main__":
    try:
        print(process_deque([("right", "A"), ("left", "B"), ("take_right", None)]))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
