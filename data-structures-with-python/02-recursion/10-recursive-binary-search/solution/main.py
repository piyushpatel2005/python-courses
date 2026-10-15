from __future__ import annotations

def binary_search_recursive(values: list[int], target: int) -> int | None:
    def search(low: int, high: int) -> int | None:
        if low >= high:
            return None
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            return search(mid + 1, high)
        return search(low, mid)
    return search(0, len(values))


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(binary_search_recursive([2, 6, 11, 18, 24], 18))
        print(binary_search_recursive([2, 6, 11], 7))
    except NotImplementedError as error:
        print("Not ready yet:", error)
