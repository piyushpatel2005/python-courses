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
        while True:
            child = smaller_child(self.data, index)
            if child is None or not self.data[child] < self.data[index]:
                return
            self.data[index], self.data[child] = (self.data[child], self.data[index])
            index = child

    def push(self, value: Any) -> None:
        # TODO task 1: In `MinHeap.push`, append the new leaf and pass its index to the completed sift-up helper.
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
    left = 2 * index + 1
    if left >= len(values):
        return None
    right = left + 1
    if right < len(values) and values[right] < values[left]:
        return right
    return left

if __name__ == "__main__":
    try:
        heap = MinHeap()
        for value in [7, 2, 5, 1]:
            heap.push(value)
        print(heap.data)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
