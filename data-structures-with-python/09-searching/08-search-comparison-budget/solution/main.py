from __future__ import annotations
from collections.abc import Callable

def compare_int(left: int, right: int) -> int:
    return (left > right) - (left < right)


def measured_binary_search(
    values: list[int],
    target: int,
    compare: Callable[[int, int], int] = compare_int,
) -> tuple[int, int]:
    lo, hi = 0, len(values)
    probes = 0
    while lo < hi:
        mid = lo + (hi - lo) // 2
        relation = compare_at(values, mid, target, compare)
        probes += 1
        if relation == 0:
            return mid, probes
        if relation < 0:
            lo = mid + 1
        else:
            hi = mid
    return -1, probes


def compare_at(values: list[int], index: int, target: int, compare: Callable[[int, int], int]) -> int:
    return compare(values[index], target)


if __name__ == "__main__":
    try:
        print(measured_binary_search([1, 4, 9, 13, 18], 9))
        print(measured_binary_search([1, 4, 9, 13, 18], 12))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
