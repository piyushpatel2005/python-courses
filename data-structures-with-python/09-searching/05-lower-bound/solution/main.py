from __future__ import annotations

def lower_bound(values: list[int], target: int) -> int:
    lo, hi = 0, len(values)
    while lo < hi:
        lo, hi = lower_step(values, target, lo, hi)
    return lo


def lower_step(values: list[int], target: int, lo: int, hi: int) -> tuple[int, int]:
    mid = lo + (hi - lo) // 2
    if values[mid] < target:
        return mid + 1, hi
    return lo, mid


if __name__ == "__main__":
    try:
        print(lower_bound([2, 4, 4, 4, 8], 4))
        print(lower_bound([2, 4, 4, 4, 8], 6))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
