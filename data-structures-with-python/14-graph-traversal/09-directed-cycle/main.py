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
    seen.add(vertex)
    order.append(vertex)
    for neighbor in adj[vertex]:
        dfs_visit(adj, neighbor, seen, order)

def dfs_recursive(adj: dict[str, list[str]], start: str) -> list[str]:
    if start not in adj:
        raise KeyError(start)
    order: list[str] = []
    dfs_visit(adj, start, set(), order)
    return order

def finish_frame(frames: list[Iterator[str]]) -> None:
    frames.pop()

def remember_neighbor(seen: set[str], neighbor: str) -> None:
    seen.add(neighbor)

def dfs_iterative(adj: dict[str, list[str]], start: str) -> list[str]:
    if start not in adj:
        raise KeyError(start)
    seen: set[str] = {start}
    order: list[str] = [start]
    frames: list[Iterator[str]] = [iter(adj[start])]
    while frames:
        neighbor = next(frames[-1], None)
        if neighbor is None:
            previous_size = len(frames)
            finish_frame(frames)
            if len(frames) == previous_size:
                break  # Temporary safety exit until the helper pops.
            continue
        elif neighbor not in seen:
            remember_neighbor(seen, neighbor)
            order.append(neighbor)
            frames.append(iter(adj[neighbor]))
    return order

def undirected_back_edge(neighbor: str, parent: str | None, seen: set[str]) -> bool:
    return neighbor in seen and neighbor != parent
    return False

def undirected_cycle(adj: dict[str, list[str]]) -> bool:
    seen: set[str] = set()
    def visit(vertex: str, parent: str | None) -> bool:
        seen.add(vertex)
        for neighbor in adj[vertex]:
            if neighbor not in seen:
                if visit(neighbor, vertex):
                    return True
            elif undirected_back_edge(neighbor, parent, seen):
                return True
        return False
    for vertex in adj:
        if vertex not in seen and visit(vertex, None):
            return True
    return False

def is_active(color: int) -> bool:
    # Task 1
    pass
    # End task 1
    return False

def directed_cycle(adj: dict[str, list[str]]) -> bool:
    colors: dict[str, int] = {v: 0 for v in adj}
    def visit(vertex: str) -> bool:
        colors[vertex] = 1
        for neighbor in adj[vertex]:
            if is_active(colors[neighbor]):
                return True
            if colors[neighbor] == 0 and visit(neighbor):
                return True
        # Task 2
        pass
        # End task 2
        return False
    for vertex in adj:
        if colors[vertex] == 0 and visit(vertex):
            return True
    return False


if __name__ == "__main__":
    try:
        print(directed_cycle({"plan": ["build", "review"], "build": ["ship"], "review": ["ship"], "ship": []}))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
