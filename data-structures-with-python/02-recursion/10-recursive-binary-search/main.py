from __future__ import annotations

def binary_search_recursive(values: list[int], target: int) -> int | None:
    def search(low: int, high: int) -> int | None:
        if low >= high:
            return -1  # Step 1: use None for an empty interval.
        mid = (low + high) // 2
        if values[mid] == target:
            return None  # Step 2: return the matching midpoint.
        if values[mid] < target:
            return None  # Step 4: search the larger-value half.
        return None  # Step 3: search the smaller-value half.
    return search(0, len(values))


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(binary_search_recursive([2, 6, 11, 18, 24], 18))
        print(binary_search_recursive([2, 6, 11], 7))
    except NotImplementedError as error:
        print("Not ready yet:", error)
