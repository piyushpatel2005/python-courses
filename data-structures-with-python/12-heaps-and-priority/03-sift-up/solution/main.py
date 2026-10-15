from __future__ import annotations

from typing import Any, Callable, Iterable

def family_indices(index: int, size: int) -> tuple[int | None, int | None, int | None]:
    if index < 0 or index >= size:
        raise IndexError('index outside heap')
    parent = (index - 1) // 2 if index > 0 else None
    left = 2 * index + 1
    right = 2 * index + 2
    return (parent, left if left < size else None, right if right < size else None)

def is_min_heap(values: list[Any]) -> bool:
    for index in range(1, len(values)):
        parent = (index - 1) // 2
        if values[index] < values[parent]:
            return False
    return True

class MinHeap:

    def __init__(self, values: Iterable[Any]=()) -> None:
        self.data: list[Any] = list(values)

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = rise_once(self.data, index)
            if parent == index:
                break
            index = parent

def rise_once(values: list[Any], index: int) -> int:
    if index == 0:
        return index
    parent = (index - 1) // 2
    if values[index] < values[parent]:
        values[index], values[parent] = (values[parent], values[index])
        return parent
    return index

if __name__ == "__main__":
    try:
        heap = MinHeap([3, 7, 5, 9, 1])
        heap._sift_up(4)
        print(heap.data)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
