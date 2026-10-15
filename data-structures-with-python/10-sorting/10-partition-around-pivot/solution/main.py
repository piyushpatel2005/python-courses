from __future__ import annotations

from typing import Any, Callable, Iterable

def partition(values: list[Any], low: int, high: int) -> int:
    if low < 0 or high >= len(values) or low > high:
        raise IndexError('invalid inclusive interval')
    boundary = scan_partition(values, low, high)
    values[boundary], values[high] = (values[high], values[boundary])
    return boundary

def scan_partition(values: list[Any], low: int, high: int) -> int:
    pivot = values[high]
    boundary = low
    for index in range(low, high):
        if values[index] < pivot:
            values[boundary], values[index] = (values[index], values[boundary])
            boundary += 1
    return boundary

if __name__ == "__main__":
    try:
        a = [9, 6, 2, 8, 4, 0]
        p = partition(a, 1, 4)
        print(p, a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
