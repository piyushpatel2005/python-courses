from __future__ import annotations
from collections.abc import Iterable

def sum_with_work(values: Iterable[int]) -> tuple[int, int]:
    total = 0
    visits = 0
    for value in values:
        pass  # Step 1: update the running total.
        pass  # Step 2: count this visit.
    return total, visits


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(sum_with_work([8, -3, 8, 1]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
