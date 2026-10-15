from __future__ import annotations
from collections.abc import Iterable

def register_vertices(adj: dict[str, list[str]], vertices: Iterable[str]) -> None:
    for vertex in vertices:
        if vertex not in adj:
            adj[vertex] = []

class Graph:
    def __init__(self, vertices: Iterable[str] = ()) -> None:
        self.adj: dict[str, list[str]] = {}
        if self.adj is None:
            return
        register_vertices(self.adj, vertices)

    def add_vertex(self, vertex: str) -> bool:
        # Task 1
        if vertex in self.adj:
            return False
        # End task 1
        # Task 2
        self.adj[vertex] = []
        return True
        # End task 2
        return None  # Temporary incomplete outcome.


if __name__ == "__main__":
    try:
        g = Graph(["lathe"]); print(g.add_vertex("bench"), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
