from __future__ import annotations

from typing import Any, Callable, Iterable

import heapq

def heapq_order(values: Iterable[Any]) -> list[Any]:
    heap = make_heap(values)
    # TODO task 2: In `heapq_order`, drain the copied heap with `heapq.heappop` into a new ordered result.
    raise NotImplementedError('Complete this step')

def make_heap(values: Iterable[Any]) -> list[Any]:
    # TODO task 1: In `make_heap`, copy the input, heapify the copy, and return the owned heap list.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(heapq_order([7, 2, 5, 1]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
