from __future__ import annotations
from typing import Any

def pair_matches(values: list[Any]) -> tuple[list[tuple[int, int]], int]:
    matches = []
    comparisons = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            comparisons += 1
            if values[i] == values[j]:
                matches.append((i, j))
    return matches, comparisons


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(pair_matches([4, 9, 4, 4]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
