from __future__ import annotations

from typing import Any, Callable, Iterable

import heapq

def top_k(values: Iterable[int], k: int) -> list[int]:
    if k < 0:
        raise ValueError('k must be nonnegative')
    if k == 0:
        return []
    heap: list[int] = []
    for value in values:
        retain_candidate(heap, value, k)
    result: list[int] = []
    while heap:
        result.append(heapq.heappop(heap))
    result.reverse()
    return result

def retain_candidate(heap: list[int], value: int, k: int) -> None:
    if len(heap) < k:
        heapq.heappush(heap, value)
        return
    if value > heap[0]:
        heapq.heapreplace(heap, value)

if __name__ == "__main__":
    try:
        print(top_k(iter([7, 2, 5, 1, 9, 5]), 3))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
