from __future__ import annotations

def recursive_sum(values: list[int]) -> int:
    pass  # Step 1: reject an input longer than 100.
    def total_from(index: int) -> int:
        if index == len(values):
            return None  # Step 2: answer the empty suffix.
        return None  # Step 3: combine this value with the smaller suffix.
    return total_from(0)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(recursive_sum([7, -4, 7]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
