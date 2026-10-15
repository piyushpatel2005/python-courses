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
    distances[neighbor] = distances[vertex] + 1


def bfs_distances(adj: dict[str, list[str]], start: str) -> dict[str, int]:
    if start not in adj:
        raise KeyError(start)
    distances: dict[str, int] = {}
    distances[start] = 0
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

def bfs_parents(adj: dict[str, list[str]], start: str) -> dict[str, str | None]:
    if start not in adj:
        raise KeyError(start)
    parents: dict[str, str | None] = {start: None}
    seen: set[str] = {start}
    frontier: deque[str] = deque([start])
    while frontier:
        vertex = frontier.popleft()
        for neighbor in adj[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
                parents[neighbor] = vertex
    return parents

def backward_chain(parents: dict[str, str | None], target: str) -> list[str]:
    chain: list[str] = []
    current: str | None = target
    while current is not None:
        chain.append(current)
        current = parents[current]
    return chain

def bfs_path(adj: dict[str, list[str]], start: str, target: str) -> list[str]:
    if start not in adj or target not in adj:
        raise KeyError("Unknown endpoint")
    parents = bfs_parents(adj, start)
    if target not in parents:
        return []
    path = backward_chain(parents, target)
    path.reverse()
    return path

def collect_component(adj: dict[str, list[str]], start: str, seen: set[str]) -> list[str]:
    members = bfs(adj, start)
    seen.update(members)
    return members

def components(adj: dict[str, list[str]]) -> list[list[str]]:
    seen: set[str] = set()
    groups: list[list[str]] = []
    for vertex in adj:
        if vertex not in seen:
            members = collect_component(adj, vertex, seen)
            groups.append(members)
    return groups

def dfs_visit(adj: dict[str, list[str]], vertex: str, seen: set[str], order: list[str]) -> None:
    if vertex in seen:
        return
    # Task 1
    pass
    # End task 1
    # Task 2
    pass
    # End task 2
    # Task 3
    pass
    # End task 3

def dfs_recursive(adj: dict[str, list[str]], start: str) -> list[str]:
    if start not in adj:
        raise KeyError(start)
    order: list[str] = []
    dfs_visit(adj, start, set(), order)
    return order


if __name__ == "__main__":
    try:
        print(dfs_recursive({"gate": ["yard", "desk"], "yard": ["shed"], "desk": [], "shed": []}, "gate"))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
