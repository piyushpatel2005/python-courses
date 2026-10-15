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
    position = upper_bound(values, target)
    shift_right(values, position)
    values[position] = target
    return position


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
    values.append(0)
    i = len(values) - 1
    while i > position:
        values[i] = values[i - 1]
        i -= 1


if __name__ == "__main__":
    try:
        values = [1, 5, 5, 9]
        position = insert_sorted(values, 5)
        print(position, values)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
