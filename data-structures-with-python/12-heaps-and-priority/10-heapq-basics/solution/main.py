from __future__ import annotations

from typing import Any, Callable, Iterable

import heapq

def heapq_order(values: Iterable[Any]) -> list[Any]:
    heap = make_heap(values)
    result: list[Any] = []
    while heap:
        result.append(heapq.heappop(heap))
    return result

def make_heap(values: Iterable[Any]) -> list[Any]:
    heap = list(values)
    heapq.heapify(heap)
    return heap

if __name__ == "__main__":
    try:
        print(heapq_order([7, 2, 5, 1]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
