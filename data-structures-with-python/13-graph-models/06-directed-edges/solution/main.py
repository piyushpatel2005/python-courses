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
        # Task 1
        if source not in self.adj or target not in self.adj:
            raise KeyError("Both endpoints must exist")
        # End task 1
        # Task 2
        if source == target:
            raise ValueError("Self-loops are not supported")
        # End task 2
        # Task 3
        if target in self.adj[source]:
            return False
        # End task 3
        # Task 4
        self.adj[source].append(target)
        return True
        # End task 4
        return None


if __name__ == "__main__":
    try:
        g = DirectedGraph(["cut", "join"]); print(g.add_edge("cut", "join"), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
