from __future__ import annotations
from collections.abc import Iterable, Iterator
from collections import deque
import heapq
from math import inf

def discover(neighbors: list[str], seen: set[str], frontier: deque[str]) -> None:
    for neighbor in neighbors:
        if neighbor not in seen:
            # Task 1
            seen.add(neighbor)
            # End task 1
            # Task 2
            frontier.append(neighbor)
            # End task 2


if __name__ == "__main__":
    try:
        seen = {"gate"}; frontier = deque(["gate"]); discover(["yard", "yard", "desk"], seen, frontier); print(list(frontier), sorted(seen))
    except (NotImplementedError, KeyError, TypeError, AttributeError, ValueError) as error:
        print("Checkpoint not ready:", error)
