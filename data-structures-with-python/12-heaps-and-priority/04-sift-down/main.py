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

    def _sift_down(self, index: int) -> None:
        # TODO task 2: In `MinHeap._sift_down`, move down through smaller children until the subtree obeys heap order.
        raise NotImplementedError('Complete this step')

def rise_once(values: list[Any], index: int) -> int:
    if index == 0:
        return index
    parent = (index - 1) // 2
    if values[index] < values[parent]:
        values[index], values[parent] = (values[parent], values[index])
        return parent
    return index

def smaller_child(values: list[Any], index: int) -> int | None:
    # TODO task 1: In `smaller_child`, choose the smaller existing child, favoring the left on a tie.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        heap = MinHeap([10, 3, 5, 7, 8, 6])
        heap._sift_down(0)
        print(heap.data)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
