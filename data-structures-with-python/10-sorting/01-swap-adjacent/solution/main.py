from __future__ import annotations

from typing import Any, Callable, Iterable

def swap_adjacent(values: list[Any], index: int) -> bool:
    if index < 0 or index + 1 >= len(values):
        raise IndexError('adjacent pair outside list')
    if values[index + 1] < values[index]:
        values[index], values[index + 1] = (values[index + 1], values[index])
        return True
    return False

if __name__ == "__main__":
    try:
        a = [7, 2, 5]
        print(swap_adjacent(a, 0), a)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
