from __future__ import annotations

from collections import deque


def window_maxima(values: list[int], k: int) -> list[int]:
    validate_window(values, k)
    candidates = deque()
    result = []
    for i in range(len(values)):
        advance_candidates(values, candidates, i, k)
        if i >= k - 1:
            result.append(values[candidates[0]])
    return result


def validate_window(values: list[int], k: int) -> None:
    if type(k) is not int or not 1 <= k <= len(values):
        raise ValueError("invalid window width")


def advance_candidates(values: list[int], candidates: deque[int], i: int, k: int) -> None:
    while candidates and candidates[0] < i - k + 1:
        candidates.popleft()
    while candidates and values[candidates[-1]] <= values[i]:
        candidates.pop()
    candidates.append(i)


if __name__ == "__main__":
    try:
        print(window_maxima([8, 3, 5, 9, 2], 3))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
