from __future__ import annotations

from typing import Any, Callable, Iterable

def swap_adjacent(values: list[Any], index: int) -> bool:
    # TODO task 1: In `swap_adjacent`, reject an index that does not identify a complete adjacent pair.
    pass
    # TODO task 2: In `swap_adjacent`, exchange a descending pair and return whether it changed.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [7, 2, 5]
        print(swap_adjacent(a, 0), a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
