from __future__ import annotations

def append_costs(n: int) -> tuple[list[int], int]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    size = capacity = 0
    costs = []
    for _ in range(n):
        cost = 1
        if size == capacity:
            cost += size
            capacity = 1 if capacity == 0 else capacity * 2
        size += 1
        costs.append(cost)
    return costs, capacity


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(append_costs(7))
    except NotImplementedError as error:
        print("Not ready yet:", error)
