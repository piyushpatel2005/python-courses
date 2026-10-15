from __future__ import annotations

class PrefixSums:
    def __init__(self, values: list[int]) -> None:
        self.prefix: list[int] = [0]
        running = 0
        for value in values:
            running += value
            self.prefix.append(running)

    def range_sum(self, start: int, stop: int) -> int:
        size = len(self.prefix) - 1
        if not 0 <= start <= stop <= size:
            raise ValueError("range must satisfy 0 <= start <= stop <= size")
        return self.prefix[stop] - self.prefix[start]


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        report = PrefixSums([5, -3, 8, 2])
        print(report.range_sum(1, 4))
        print(report.range_sum(2, 2))
    except NotImplementedError as error:
        print("Not ready yet:", error)
