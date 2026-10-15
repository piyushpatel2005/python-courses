from __future__ import annotations
from collections.abc import Iterable

def register_vertices(adj: dict[str, list[str]], vertices: Iterable[str]) -> None:
    for vertex in vertices:
        if vertex not in adj:
            adj[vertex] = []

class DirectedGraph:
    def __init__(self, vertices: Iterable[str] = ()) -> None:
        self.adj: dict[str, list[str]] = {}
        if self.adj is None:
            return
        register_vertices(self.adj, vertices)

    def add_vertex(self, vertex: str) -> bool:
        if vertex in self.adj:
            return False
        self.adj[vertex] = []
        return True
        return None  # Temporary incomplete outcome.

    def add_edge(self, source: str, target: str) -> bool:
        if source not in self.adj or target not in self.adj:
            raise KeyError("Both endpoints must exist")
        if source == target:
            raise ValueError("Self-loops are not supported")
        if target in self.adj[source]:
            return False
        self.adj[source].append(target)
        return True
        return None

def zero_matrix(labels: list[str]) -> list[list[int]]:
    # Task 2
    return []
    # End task 2


def fill_matrix(adj: dict[str, list[str]], positions: dict[str, int], matrix: list[list[int]]) -> None:
    # Task 3
    pass
    # End task 3


def adjacency_matrix(adj: dict[str, list[str]]) -> tuple[list[str], list[list[int]]]:
    # Task 1
    labels: list[str] = []
    # End task 1
    positions = {vertex: i for i, vertex in enumerate(labels)}
    matrix = zero_matrix(labels)
    if len(matrix) != len(labels):
        return labels, matrix
    fill_matrix(adj, positions, matrix)
    return labels, matrix


if __name__ == "__main__":
    try:
        print(adjacency_matrix({"cut": ["join"], "join": [], "idle": []}))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
