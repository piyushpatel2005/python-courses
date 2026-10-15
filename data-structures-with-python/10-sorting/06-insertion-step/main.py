from __future__ import annotations

from typing import Any, Callable, Iterable

def insert_at(values: list[Any], index: int) -> list[Any]:
    # TODO task 2: In `insert_at`, reject an invalid insertion position before mutation.
    pass
    item = values[index]
    cursor = shift_larger(values, index, item)
    # TODO task 3: In `insert_at`, fill the returned gap with the saved item and return the same list.
    raise NotImplementedError('Complete this step')

def shift_larger(values: list[Any], index: int, item: Any) -> int:
    # TODO task 1: In `shift_larger`, shift larger predecessors right and return the final gap index.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [2, 6, 8, 4, 1]
        print(insert_at(a, 3))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
