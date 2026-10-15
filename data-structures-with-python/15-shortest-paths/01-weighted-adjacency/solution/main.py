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
        if source not in self.adj or target not in self.adj:
            raise KeyError("Unknown endpoint")
        # End task 1
        # Task 2
        if type(weight) is not int or weight < 0:
            raise ValueError("Weight must be a nonnegative integer")
        # End task 2
        # Task 3
        if any(neighbor == target for neighbor, _ in self.adj[source]):
            return False
        # End task 3
        # Task 4
        self.adj[source].append((target, weight))
        return True
        # End task 4
        return None


if __name__ == "__main__":
    try:
        g = WeightedGraph(["dock", "shed"]); print(g.add_edge("dock", "shed", 0), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
