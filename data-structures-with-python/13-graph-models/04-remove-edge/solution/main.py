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
        if a not in self.adj or b not in self.adj:
            raise KeyError("Both endpoints must exist")
        if a == b:
            raise ValueError("Self-loops are not supported")
        if b in self.adj[a]:
            return False
        self.adj[a].append(b)
        self.adj[b].append(a)
        return True
        return None

    def remove_edge(self, a: str, b: str) -> bool:
        # Task 1
        if a not in self.adj or b not in self.adj or b not in self.adj[a]:
            return False
        # End task 1
        # Task 2
        self.adj[a].remove(b)
        self.adj[b].remove(a)
        return True
        # End task 2
        return None


if __name__ == "__main__":
    try:
        g = Graph(["lathe", "bench"]); g.add_edge("lathe", "bench"); print(g.remove_edge("lathe", "bench"), g.adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
