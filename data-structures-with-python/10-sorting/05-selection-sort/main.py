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

def selection_sort(values: list[Any]) -> list[Any]:
    # TODO task 1: In `selection_sort`, place each remaining suffix minimum into the next destination.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [6, 1, 5, 2]
        print(selection_sort(a))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
