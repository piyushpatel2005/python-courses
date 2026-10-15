from __future__ import annotations

from typing import Any, Callable, Iterable

def partition(values: list[Any], low: int, high: int) -> int:
    if low < 0 or high >= len(values) or low > high:
        raise IndexError('invalid inclusive interval')
    boundary = scan_partition(values, low, high)
    values[boundary], values[high] = (values[high], values[boundary])
    return boundary

def quicksort(values: list[Any]) -> list[Any]:
    # TODO task 2: In `quicksort`, return a fresh copy for the recursive base case.
    pass
    less, equal, greater = split_three(values)
    # TODO task 3: In `quicksort`, recursively sort the smaller and greater groups, then concatenate around the equal group.
    raise NotImplementedError('Complete this step')

def scan_partition(values: list[Any], low: int, high: int) -> int:
    pivot = values[high]
    boundary = low
    for index in range(low, high):
        if values[index] < pivot:
            values[boundary], values[index] = (values[index], values[boundary])
            boundary += 1
    return boundary

def split_three(values: list[Any]) -> tuple[list[Any], list[Any], list[Any]]:
    # TODO task 1: In `split_three`, separate a nonempty input into less, equal, and greater groups without mutation.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(quicksort(a))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
