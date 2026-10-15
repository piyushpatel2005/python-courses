from __future__ import annotations

class PrefixSums:
    def __init__(self, values: list[int]) -> None:
        self.prefix: list[int] = [0]
        running = 0
        for value in values:
            running += value
            self.prefix.append(running)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        report = PrefixSums([5, -3, 8, 2])
        print(report.prefix)
    except NotImplementedError as error:
        print("Not ready yet:", error)
