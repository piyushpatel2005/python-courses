from __future__ import annotations

from typing import Any, Callable, Iterable

def insert_at(values: list[Any], index: int) -> list[Any]:
    if index < 0 or index >= len(values):
        raise IndexError('invalid insertion position')
    item = values[index]
    cursor = shift_larger(values, index, item)
    values[cursor] = item
    return values

def shift_larger(values: list[Any], index: int, item: Any) -> int:
    cursor = index
    while cursor > 0 and item < values[cursor - 1]:
        values[cursor] = values[cursor - 1]
        cursor -= 1
    return cursor

if __name__ == "__main__":
    try:
        a = [2, 6, 8, 4, 1]
        print(insert_at(a, 3))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
