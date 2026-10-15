from __future__ import annotations

class PrefixSums:
    def __init__(self, values: list[int]) -> None:
        self.prefix: list[int] = []  # Step 1: include the empty-prefix boundary.
        running = 0
        for value in values:
            pass  # Step 2: extend the running total and record its boundary.


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        report = PrefixSums([5, -3, 8, 2])
        print(report.prefix)
    except NotImplementedError as error:
        print("Not ready yet:", error)
