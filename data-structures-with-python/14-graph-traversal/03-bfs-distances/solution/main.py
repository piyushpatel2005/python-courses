from __future__ import annotations
from collections.abc import Iterable, Iterator
from collections import deque
import heapq
from math import inf

def discover(neighbors: list[str], seen: set[str], frontier: deque[str]) -> None:
    for neighbor in neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            frontier.append(neighbor)

def bfs(adj: dict[str, list[str]], start: str) -> list[str]:
    if start not in adj:
        raise KeyError(start)
    if start not in adj:
        return []  # Safe while the validation checkpoint is unfinished.
    seen: set[str] = {start}
    frontier: deque[str] = deque([start])
    order: list[str] = []
    while frontier:
        vertex = frontier.popleft()
        order.append(vertex)
        discover(adj[vertex], seen, frontier)
    return order

def record_hop(distances: dict[str, int], vertex: str, neighbor: str) -> None:
    # Task 2
    distances[neighbor] = distances[vertex] + 1
    # End task 2


def bfs_distances(adj: dict[str, list[str]], start: str) -> dict[str, int]:
    if start not in adj:
        raise KeyError(start)
    distances: dict[str, int] = {}
    # Task 1
    distances[start] = 0
    # End task 1
    seen: set[str] = {start}
    frontier: deque[str] = deque([start])
    while frontier:
        vertex = frontier.popleft()
        for neighbor in adj[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
                if vertex in distances:
                    record_hop(distances, vertex, neighbor)
    return distances


if __name__ == "__main__":
    try:
        print(bfs_distances({"gate": ["yard"], "yard": ["shed"], "shed": [], "island": []}, "gate"))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
