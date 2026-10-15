from __future__ import annotations

def binary_search(values: list[int], target: int) -> int:
    lo, hi = 0, len(values)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1


def binary_search_range(values: list[int], target: int, lo: int, hi: int) -> int:
    # TODO: complete the numbered steps for this function.
    validate_bounds(values, lo, hi)
    while lo < hi:
        break
    return None


def validate_bounds(values: list[int], lo: int, hi: int) -> None:
    # TODO: complete the numbered steps for this function.
    pass


if __name__ == "__main__":
    try:
        print(binary_search_range([2, 6, 6, 10], 6, 2, 4))
        print(binary_search_range([2, 6, 6, 10], 10, 0, 3))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
