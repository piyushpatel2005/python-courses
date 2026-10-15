from __future__ import annotations

def growth_report(sizes: list[int]) -> list[tuple[int, int, int, int]]:
    report = []
    for n in sizes:
        if n < 0:
            raise ValueError("sizes must be nonnegative")
        visits = 0
        for i in range(n):
            visits += 1
        pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                pairs += 1
        reductions = 0
        remaining = n
        while remaining > 1:
            reductions += 1
            remaining //= 2
        report.append((n, visits, pairs, reductions))
    return report


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(growth_report([0, 5, 10, 20]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
