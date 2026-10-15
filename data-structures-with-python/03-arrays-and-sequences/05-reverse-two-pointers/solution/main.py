from __future__ import annotations

def reverse_in_place(values: list[int]) -> list[int]:
    left = 0
    right = len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return values


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        route = [4, 9, 2, 7, 5]
        print(reverse_in_place(route))
    except NotImplementedError as error:
        print("Not ready yet:", error)
