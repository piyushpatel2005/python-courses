from __future__ import annotations

from typing import Any, Callable, Iterable

import heapq

class PriorityQueue:

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, Any]] = []
        self._counter: int = 0

    def push(self, task: Any, priority: int) -> None:
        ticket = self._take_ticket()
        heapq.heappush(self._heap, (priority, ticket, task))

    def pop(self) -> Any:
        if not self._heap:
            raise IndexError('pop from empty priority queue')
        return heapq.heappop(self._heap)[2]

    def _take_ticket(self) -> int:
        ticket = self._counter
        self._counter += 1
        return ticket

if __name__ == "__main__":
    try:
        queue = PriorityQueue()
        queue.push({"job": "labels"}, 2)
        queue.push({"job": "tickets"}, 2)
        print(queue.pop(), queue.pop())
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
