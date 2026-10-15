from __future__ import annotations

from collections import deque


def window_maxima(values: list[int], k: int) -> list[int]:
    # TODO: complete the numbered steps for this function.
    return []


def validate_window(values: list[int], k: int) -> None:
    # TODO: complete the numbered steps for this function.
    pass


def advance_candidates(values: list[int], candidates: deque[int], i: int, k: int) -> None:
    # TODO: complete the numbered steps for this function.
    pass


if __name__ == "__main__":
    try:
        print(window_maxima([8, 3, 5, 9, 2], 3))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
