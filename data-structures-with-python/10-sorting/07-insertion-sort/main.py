from __future__ import annotations

from typing import Any, Callable, Iterable

def insert_at(values: list[Any], index: int) -> list[Any]:
    if index < 0 or index >= len(values):
        raise IndexError('invalid insertion position')
    item = values[index]
    cursor = shift_larger(values, index, item)
    values[cursor] = item
    return values

def insertion_sort(values: list[Any]) -> list[Any]:
    # TODO task 1: In `insertion_sort`, extend the sorted prefix by calling `insert_at` at each next index.
    raise NotImplementedError('Complete this step')

def shift_larger(values: list[Any], index: int, item: Any) -> int:
    cursor = index
    while cursor > 0 and item < values[cursor - 1]:
        values[cursor] = values[cursor - 1]
        cursor -= 1
    return cursor

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(insertion_sort(a))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
