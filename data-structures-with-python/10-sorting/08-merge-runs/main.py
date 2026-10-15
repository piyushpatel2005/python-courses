from __future__ import annotations

from typing import Any, Callable, Iterable

def merge_runs(left: list[Any], right: list[Any]) -> list[Any]:
    result, i, j = merge_fronts(left, right)
    # TODO task 2: In `merge_runs`, append both unconsumed suffixes and return the completed merge.
    raise NotImplementedError('Complete this step')

def merge_fronts(left: list[Any], right: list[Any]) -> tuple[list[Any], int, int]:
    # TODO task 1: In `merge_fronts`, merge current fronts until one run ends; return the prefix and both cursors.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(merge_runs([1, 5, 8], [2, 5, 7]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
