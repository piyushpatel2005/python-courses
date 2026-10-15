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

class UpdatingQueue:

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, Any]] = []
        self._counter: int = 0
        self._active: dict[str, int] = {}

    def update(self, task: str, priority: int) -> None:
        ticket = self._publish(task)
        heapq.heappush(self._heap, (priority, ticket, task))

    def _discard_stale(self) -> None:
        while self._heap:
            priority, ticket, task = self._heap[0]
            if self._active.get(task) == ticket:
                return
            heapq.heappop(self._heap)

    def peek(self) -> tuple[str, int]:
        self._discard_stale()
        if not self._heap:
            raise IndexError('peek from empty priority queue')
        priority, ticket, task = self._heap[0]
        return (task, priority)

    def pop(self) -> tuple[str, int]:
        task, priority = self.peek()
        heapq.heappop(self._heap)
        del self._active[task]
        return (task, priority)

    def _publish(self, task: str) -> int:
        ticket = self._counter
        self._counter += 1
        self._active[task] = ticket
        return ticket

class Scheduler:

    def __init__(self) -> None:
        self.queue: UpdatingQueue = UpdatingQueue()

    def schedule(self, task: str, due: int) -> None:
        self.queue.update(task, due)

    def run_due(self, now: int) -> list[str]:
        # TODO task 2: In `Scheduler.run_due`, drain ready jobs through `now`, stopping before the first future job.
        raise NotImplementedError('Complete this step')

    def has_due(self, now: int) -> bool:
        # TODO task 1: In `Scheduler.has_due`, check whether the earliest live job is due, without removing that job.
        raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        scheduler = Scheduler()
        scheduler.schedule("labels", 8)
        scheduler.schedule("tickets", 4)
        scheduler.schedule("labels", 3)
        print(scheduler.run_due(4))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
