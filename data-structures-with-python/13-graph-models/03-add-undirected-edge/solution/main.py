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
        if vertex in self.adj:
            return False
        self.adj[vertex] = []
        return True
        return None  # Temporary incomplete outcome.

    def add_edge(self, a: str, b: str) -> bool:
        # Task 1
        if a not in self.adj or b not in self.adj:
            raise KeyError("Both endpoints must exist")
        # End task 1
        # Task 2
        if a == b:
            raise ValueError("Self-loops are not supported")
        # End task 2
        # Task 3
        if b in self.adj[a]:
            return False
        # End task 3
        # Task 4
        self.adj[a].append(b)
        self.adj[b].append(a)
        return True
        # End task 4
        return None


if __name__ == "__main__":
    try:
        g = Graph(["cut", "join"]); print(g.add_edge("cut", "join"), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
