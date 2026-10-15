from __future__ import annotations

from typing import Any, Callable, Iterable

def partition(values: list[Any], low: int, high: int) -> int:
    # TODO task 2: In `partition`, reject an invalid inclusive interval before mutation.
    pass
    boundary = scan_partition(values, low, high)
    # TODO task 3: In `partition`, exchange the pivot into the returned boundary and return that index.
    raise NotImplementedError('Complete this step')

def scan_partition(values: list[Any], low: int, high: int) -> int:
    # TODO task 1: In `scan_partition`, scan non-pivot items into the smaller region and return its boundary.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [9, 6, 2, 8, 4, 0]
        p = partition(a, 1, 4)
        print(p, a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
