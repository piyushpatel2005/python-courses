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
    # Task 1
    pass
    # End task 1
    if start not in adj:
        return []  # Safe while the validation checkpoint is unfinished.
    seen: set[str] = {start}
    frontier: deque[str] = deque([start])
    order: list[str] = []
    while frontier:
        vertex = frontier.popleft()
        # Task 2
        pass
        # End task 2
        # Task 3
        pass
        # End task 3
    return order


if __name__ == "__main__":
    try:
        print(bfs({"gate": ["yard", "desk"], "yard": ["shed"], "desk": [], "shed": []}, "gate"))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
