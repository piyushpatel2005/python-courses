from __future__ import annotations

from typing import Any, Callable, Iterable

def merge_runs(left: list[Any], right: list[Any]) -> list[Any]:
    result, i, j = merge_fronts(left, right)
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(values: list[Any]) -> list[Any]:
    # TODO task 1: In `merge_sort`, return a fresh copy for inputs with fewer than two items.
    pass
    # TODO task 2: In `merge_sort`, recursively sort both halves and combine them with `merge_runs`.
    raise NotImplementedError('Complete this step')

def merge_fronts(left: list[Any], right: list[Any]) -> tuple[list[Any], int, int]:
    result: list[Any] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    return (result, i, j)

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(merge_sort(a), a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
