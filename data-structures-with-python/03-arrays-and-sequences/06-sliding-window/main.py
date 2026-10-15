from __future__ import annotations

def max_window_sum(values: list[int], width: int) -> int:
    pass  # Step 1: reject an invalid width.
    current = 0
    for index in range(width):
        pass  # Step 2: add this first-window value.
    best = current
    for end in range(width, len(values)):
        pass  # Step 3: slide once and update the best total.
    return best


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(max_window_sum([4, -2, 7, 1, -3], 2))
    except NotImplementedError as error:
        print("Not ready yet:", error)
