from __future__ import annotations

def lower_bound(values: list[int], target: int) -> int:
    lo, hi = 0, len(values)
    while lo < hi:
        lo, hi = lower_step(values, target, lo, hi)
    return lo


def upper_bound(values: list[int], target: int) -> int:
    lo, hi = 0, len(values)
    while lo < hi:
        lo, hi = upper_step(values, target, lo, hi)
    return lo


def insert_sorted(values: list[int], target: int) -> int:
    # TODO: complete the numbered steps for this function.
    return None


def lower_step(values: list[int], target: int, lo: int, hi: int) -> tuple[int, int]:
    mid = lo + (hi - lo) // 2
    if values[mid] < target:
        return mid + 1, hi
    return lo, mid


def upper_step(values: list[int], target: int, lo: int, hi: int) -> tuple[int, int]:
    mid = lo + (hi - lo) // 2
    if values[mid] <= target:
        return mid + 1, hi
    return lo, mid


def shift_right(values: list[int], position: int) -> None:
    # TODO: complete the numbered steps for this function.
    pass


if __name__ == "__main__":
    try:
        values = [1, 5, 5, 9]
        position = insert_sorted(values, 5)
        print(position, values)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
