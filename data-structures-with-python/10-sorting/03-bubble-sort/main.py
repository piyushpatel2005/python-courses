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
    if not 0 <= stop <= len(values):
        raise ValueError('invalid exclusive stop')
    changed = False
    for index in range(stop - 1):
        if swap_adjacent(values, index):
            changed = True
    return changed

def bubble_sort(values: list[Any]) -> list[Any]:
    # TODO task 1: In `bubble_sort`, run a shrinking pass for each boundary in `pass_stops`.
    raise NotImplementedError('Complete this step')

def pass_stops(size: int) -> range:
    return range(size, 1, -1)

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(bubble_sort(a))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
