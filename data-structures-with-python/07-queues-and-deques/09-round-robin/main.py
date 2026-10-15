from __future__ import annotations

from collections import deque


def round_robin(jobs: list[tuple[str, int]]) -> list[str]:
    # TODO: complete the numbered steps for this function.
    return []


def validate_jobs(jobs: list[tuple[str, int]]) -> None:
    # TODO: complete the numbered steps for this function.
    pass


def queue_jobs(jobs: list[tuple[str, int]]) -> deque[tuple[str, int]]:
    # TODO: complete the numbered steps for this function.
    return deque()


if __name__ == "__main__":
    try:
        print(round_robin([("scan", 3), ("stamp", 1), ("file", 2)]))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
