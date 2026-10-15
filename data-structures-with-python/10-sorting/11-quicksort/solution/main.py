from __future__ import annotations

from typing import Any, Callable, Iterable

def partition(values: list[Any], low: int, high: int) -> int:
    if low < 0 or high >= len(values) or low > high:
        raise IndexError('invalid inclusive interval')
    boundary = scan_partition(values, low, high)
    values[boundary], values[high] = (values[high], values[boundary])
    return boundary

def quicksort(values: list[Any]) -> list[Any]:
    if len(values) < 2:
        return list(values)
    less, equal, greater = split_three(values)
    return quicksort(less) + equal + quicksort(greater)

def scan_partition(values: list[Any], low: int, high: int) -> int:
    pivot = values[high]
    boundary = low
    for index in range(low, high):
        if values[index] < pivot:
            values[boundary], values[index] = (values[index], values[boundary])
            boundary += 1
    return boundary

def split_three(values: list[Any]) -> tuple[list[Any], list[Any], list[Any]]:
    pivot = values[len(values) // 2]
    less: list[Any] = []
    equal: list[Any] = []
    greater: list[Any] = []
    for value in values:
        if value < pivot:
            less.append(value)
        elif pivot < value:
            greater.append(value)
        else:
            equal.append(value)
    return (less, equal, greater)

if __name__ == "__main__":
    try:
        a = [7, 2, 5, 1]
        print(quicksort(a))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
