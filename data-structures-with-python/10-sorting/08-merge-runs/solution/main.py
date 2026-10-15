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
        print(merge_runs([1, 5, 8], [2, 5, 7]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
