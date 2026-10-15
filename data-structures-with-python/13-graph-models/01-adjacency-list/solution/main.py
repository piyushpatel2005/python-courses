from __future__ import annotations
from collections.abc import Iterable

def register_vertices(adj: dict[str, list[str]], vertices: Iterable[str]) -> None:
    # Task 2
    for vertex in vertices:
        if vertex not in adj:
            adj[vertex] = []
    # End task 2

class Graph:
    def __init__(self, vertices: Iterable[str] = ()) -> None:
        # Task 1
        self.adj: dict[str, list[str]] = {}
        # End task 1
        if self.adj is None:
            return
        register_vertices(self.adj, vertices)


if __name__ == "__main__":
    try:
        print(Graph(["lathe", "bench", "lathe"]).adj)
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
