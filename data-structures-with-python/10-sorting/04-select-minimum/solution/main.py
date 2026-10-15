from __future__ import annotations

from typing import Any, Callable, Iterable

def minimum_index(values: list[Any], start: int) -> int:
    if start < 0 or start >= len(values):
        raise IndexError('empty or invalid suffix')
    best = start
    for index in range(start + 1, len(values)):
        if values[index] < values[best]:
            best = index
    return best

if __name__ == "__main__":
    try:
        print(minimum_index([6, 8, 2, 2], 1))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
