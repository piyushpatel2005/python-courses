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


if __name__ == "__main__":
    try:
        print(binary_search([1, 4, 4, 9, 15], 4))
        print(binary_search([1, 4, 4, 9, 15], 8))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
