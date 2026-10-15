from __future__ import annotations

from collections import deque


def round_robin(jobs: list[tuple[str, int]]) -> list[str]:
    validate_jobs(jobs)
    waiting = queue_jobs(jobs)
    log = []
    while waiting:
        name, units = waiting.popleft()
        log.append(name)
        units -= 1
        if units:
            waiting.append((name, units))
    return log


def validate_jobs(jobs: list[tuple[str, int]]) -> None:
    for name, units in jobs:
        if type(units) is not int or units < 0:
            raise ValueError("units must be nonnegative integers")


def queue_jobs(jobs: list[tuple[str, int]]) -> deque[tuple[str, int]]:
    waiting = deque()
    for name, units in jobs:
        if units:
            waiting.append((name, units))
    return waiting


if __name__ == "__main__":
    try:
        print(round_robin([("scan", 3), ("stamp", 1), ("file", 2)]))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
