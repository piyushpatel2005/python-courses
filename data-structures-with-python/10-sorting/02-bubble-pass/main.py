from __future__ import annotations

from typing import Any, Callable, Iterable

def swap_adjacent(values: list[Any], index: int) -> bool:
    if index < 0 or index + 1 >= len(values):
        raise IndexError('adjacent pair outside list')
    if values[index + 1] < values[index]:
        values[index], values[index + 1] = (values[index + 1], values[index])
        return True
    return False

def bubble_pass(values: list[Any], stop: int) -> bool:
    # TODO task 1: In `bubble_pass`, reject an exclusive stop outside the list boundaries.
    pass
    # TODO task 2: In `bubble_pass`, scan every active pair and return whether any exchange occurred.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(bubble_pass(a, len(a)), a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
