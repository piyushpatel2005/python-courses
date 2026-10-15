from __future__ import annotations

from typing import Any, Callable, Iterable

def minimum_index(values: list[Any], start: int) -> int:
    # TODO task 1: In `minimum_index`, reject an empty or invalid suffix before reading a candidate.
    pass
    # TODO task 2: In `minimum_index`, scan the suffix and return the first minimum position without mutation.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(minimum_index([6, 8, 2, 2], 1))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
