from __future__ import annotations

from typing import Any, Callable, Iterable

import heapq

def top_k(values: Iterable[int], k: int) -> list[int]:
    # TODO task 2: In `top_k`, reject negative k and return immediately for zero without consuming input.
    pass
    heap: list[int] = []
    for value in values:
        retain_candidate(heap, value, k)
    # TODO task 3: In `top_k`, drain and reverse the retained heap to return descending results.
    raise NotImplementedError('Complete this step')

def retain_candidate(heap: list[int], value: int, k: int) -> None:
    # TODO task 1: In `retain_candidate`, keep one incoming candidate only when capacity or its value justifies admission.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(top_k(iter([7, 2, 5, 1, 9, 5]), 3))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
