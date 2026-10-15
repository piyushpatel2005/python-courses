from __future__ import annotations

def max_window_sum(values: list[int], width: int) -> int:
    if not 1 <= width <= len(values):
        raise ValueError("width must fit a nonempty window")
    current = 0
    for index in range(width):
        current += values[index]
    best = current
    for end in range(width, len(values)):
        current -= values[end - width]
        current += values[end]
        if current > best:
            best = current
    return best


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(max_window_sum([4, -2, 7, 1, -3], 2))
    except NotImplementedError as error:
        print("Not ready yet:", error)
