from __future__ import annotations
from collections.abc import Iterable, Iterator
from collections import deque
import heapq
from math import inf

class WeightedGraph:
    def __init__(self, vertices: Iterable[str] = ()) -> None:
        self.adj: dict[str, list[tuple[str, int]]] = {v: [] for v in vertices}

    def add_edge(self, source: str, target: str, weight: int) -> bool:
        if source not in self.adj or target not in self.adj:
            raise KeyError("Unknown endpoint")
        if type(weight) is not int or weight < 0:
            raise ValueError("Weight must be a nonnegative integer")
        if any(neighbor == target for neighbor, _ in self.adj[source]):
            return False
        self.adj[source].append((target, weight))
        return True
        return None

def validate_weighted(adj: dict[str, list[tuple[str, int]]]) -> None:
    for source, edges in adj.items():
        targets: set[str] = set()
        for target, weight in edges:
            if target not in adj:
                raise KeyError(target)
            if type(weight) is not int or weight < 0:
                raise ValueError("Weight must be a nonnegative integer")
            if target in targets:
                raise ValueError("Parallel arcs are not supported")
            targets.add(target)

def edge_weight(adj: dict[str, list[tuple[str, int]]], source: str, target: str) -> int:
    # Task 1
    for neighbor, weight in adj[source]:
        if neighbor == target:
            return weight
    # End task 1
    raise KeyError((source, target))

def path_cost(adj: dict[str, list[tuple[str, int]]], path: list[str]) -> int:
    validate_weighted(adj)
    for vertex in path:
        if vertex not in adj:
            raise KeyError(vertex)
    total: int = 0
    # Task 2
    for source, target in zip(path, path[1:]):
        total += edge_weight(adj, source, target)
    # End task 2
    return total


if __name__ == "__main__":
    try:
        g = {"dock": [("shed", 4)], "shed": [("desk", 2)], "desk": []}; print(path_cost(g, ["dock", "shed", "desk"]))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
