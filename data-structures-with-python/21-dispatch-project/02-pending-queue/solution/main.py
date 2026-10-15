from __future__ import annotations

from collections import deque
from heapq import heappush, heappop


class LoadIndex:
    """Supplied Fenwick adapter: zero-based add and half-open sum."""

    def __init__(self, days: int) -> None:
        self.days: int = days
        self.tree: list[int] = [0] * (days + 1)

    def add(self, day: int, amount: int) -> None:
        index = day + 1
        while index <= self.days:
            self.tree[index] += amount
            index += index & -index

    def prefix(self, stop: int) -> int:
        total = 0
        while stop:
            total += self.tree[stop]
            stop -= stop & -stop
        return total

    def range_sum(self, start: int, stop: int) -> int:
        return self.prefix(stop) - self.prefix(start)


def _network_copy(
    network: dict[str, list[tuple[str, int]]],
) -> dict[str, list[tuple[str, int]]]:
    """Validate and copy a directed, nonnegative weighted adjacency map."""
    graph = {site: list(edges) for site, edges in network.items()}
    if any(type(site) is not str for site in graph):
        raise ValueError("site IDs must be strings")
    for edges in graph.values():
        seen = set()
        for target, weight in edges:
            if target not in graph:
                raise ValueError("unknown edge endpoint")
            if target in seen or type(weight) is not int or weight < 0:
                raise ValueError("duplicate edge or invalid weight")
            seen.add(target)
    return {site: [tuple(edge) for edge in edges] for site, edges in graph.items()}


class DispatchWorkbench:
    def __init__(
        self, network: dict[str, list[tuple[str, int]]], days: int = 7
    ) -> None:
        if type(days) is not int or days < 1:
            raise ValueError("days must be positive")
        self.network: dict[str, list[tuple[str, int]]] = _network_copy(network)
        self.days: int = days
        self.catalog: dict[str, dict[str, str | int]] = {}
        self.pending: deque[str] = deque()
        self.ready: list[tuple[int, int, str]] = []
        self.sequence: int = 0
        self.active: set[str] = set()
        self.history: list[str] = []
        self.loads: LoadIndex = LoadIndex(days)

    def _job(self, job_id: str) -> dict[str, str | int]:
        if job_id not in self.catalog:
            raise KeyError(job_id)
        return self.catalog[job_id]

    def _validate_job(self, job: dict[str, str | int]) -> None:
        required = {"id", "destination", "priority", "day", "units"}
        if set(job) != required:
            raise ValueError("job fields do not match")
        if type(job["id"]) is not str or not job["id"]:
            raise ValueError("job ID must be a nonempty string")
        if job["destination"] not in self.network:
            raise ValueError("unknown destination")
        if type(job["priority"]) is not int:
            raise ValueError("priority must be an integer")
        if type(job["day"]) is not int or not 0 <= job["day"] < self.days:
            raise ValueError("day outside reporting window")
        if type(job["units"]) is not int or job["units"] < 0:
            raise ValueError("units must be nonnegative")

    def ensure_new_id(self, job_id: str) -> None:
        if job_id in self.catalog:
            raise ValueError("duplicate job ID")

    @staticmethod
    def copy_record(job: dict[str, str | int]) -> dict[str, str | int]:
        return dict(job)

    def store_record(self, job_id: str, record: dict[str, str | int]) -> None:
        self.catalog[job_id] = record

    def register(self, job: dict[str, str | int]) -> str:
        self._validate_job(job)
        job_id = job["id"]
        self.ensure_new_id(job_id)
        self.store_record(job_id, self.copy_record(job))
        return job_id

    def claim_id(self, job_id: str) -> bool:
        if job_id in self.active:
            return False
        self.active.add(job_id)
        return True

    def append_pending(self, job_id: str) -> None:
        self.pending.append(job_id)

    def enqueue(self, job_id: str) -> bool:
        self._job(job_id)
        if not self.claim_id(job_id):
            return False
        self.append_pending(job_id)
        return True

    def take_pending(self) -> str | None:
        return self.pending.popleft() if self.pending else None


if __name__ == "__main__":
    try:
        desk = DispatchWorkbench({"pier": []})
        for name in ("r1", "r2"):
            desk.register(
                {"id": name, "destination": "pier", "priority": 2, "day": 0, "units": 3}
            )
            print(desk.enqueue(name))
        print(desk.take_pending(), desk.take_pending(), desk.take_pending())
    except NotImplementedError as error:
        print(error)
