from __future__ import annotations
from collections.abc import Iterable

def extremes(values: Iterable[int]) -> tuple[int, int] | None:
    seen = False
    low = high = None
    for value in values:
        if not seen:
            low = high = value
            seen = True
        else:
            if value < low:
                low = value
            if value > high:
                high = value
    return (low, high) if seen else None


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(extremes([14, 6, 19, 6]))
        print(extremes([]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
