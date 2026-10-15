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
    for neighbor, weight in adj[source]:
        if neighbor == target:
            return weight
    raise KeyError((source, target))

def path_cost(adj: dict[str, list[tuple[str, int]]], path: list[str]) -> int:
    validate_weighted(adj)
    for vertex in path:
        if vertex not in adj:
            raise KeyError(vertex)
    total: int = 0
    for source, target in zip(path, path[1:]):
        total += edge_weight(adj, source, target)
    return total

def candidate_cost(distance: int | float, weight: int) -> int | float:
    # Task 1
    return distance + weight
    # End task 1
    return inf

def relax(distances: dict[str, int | float], parents: dict[str, str | None], source: str, target: str, weight: int) -> bool:
    candidate = candidate_cost(distances[source], weight)
    if candidate >= distances[target]:
        return False
    # Task 2
    distances[target] = candidate
    # End task 2
    # Task 3
    parents[target] = source
    # End task 3
    return True


if __name__ == "__main__":
    try:
        d = {"dock": 2, "shed": 12}; p = {"dock": None, "shed": None}; print(relax(d, p, "dock", "shed", 3), d, p)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
