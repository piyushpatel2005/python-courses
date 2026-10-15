from __future__ import annotations

def recursive_sum(values: list[int]) -> int:
    if len(values) > 100:
        raise ValueError("Use at most 100 values")
    def total_from(index: int) -> int:
        if index == len(values):
            return 0
        return values[index] + total_from(index + 1)
    return total_from(0)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(recursive_sum([7, -4, 7]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
