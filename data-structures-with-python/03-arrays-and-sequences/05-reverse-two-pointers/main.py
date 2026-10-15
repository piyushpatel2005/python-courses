from __future__ import annotations

def reverse_in_place(values: list[int]) -> list[int]:
    left = 0
    right = len(values) - 1
    while left < right:
        pass  # Step 1: swap the two current endpoints.
        break  # Step 2: replace this safe stop with inward pointer updates.
    return values


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        route = [4, 9, 2, 7, 5]
        print(reverse_in_place(route))
    except NotImplementedError as error:
        print("Not ready yet:", error)
