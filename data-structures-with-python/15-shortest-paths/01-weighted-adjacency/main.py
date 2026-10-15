from __future__ import annotations
from collections.abc import Iterable, Iterator
from collections import deque
import heapq
from math import inf

class WeightedGraph:
    def __init__(self, vertices: Iterable[str] = ()) -> None:
        self.adj: dict[str, list[tuple[str, int]]] = {v: [] for v in vertices}

    def add_edge(self, source: str, target: str, weight: int) -> bool:
        # Task 1
        pass
        # End task 1
        # Task 2
        pass
        # End task 2
        # Task 3
        pass
        # End task 3
        # Task 4
        pass
        # End task 4
        return None


if __name__ == "__main__":
    try:
        g = WeightedGraph(["dock", "shed"]); print(g.add_edge("dock", "shed", 0), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
