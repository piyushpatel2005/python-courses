from __future__ import annotations

def growth_report(sizes: list[int]) -> list[tuple[int, int, int, int]]:
    report = []
    for n in sizes:
        pass  # Step 1: reject a negative size.
        visits = 0
        pass  # Step 2: run and count the single pass.
        pairs = 0
        pass  # Step 3: run and count distinct pairs.
        reductions = 0
        remaining = n
        pass  # Step 4: count repeated halving to at most one.
        report.append((n, visits, pairs, reductions))
    return report


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(growth_report([0, 5, 10, 20]))
    except NotImplementedError as error:
        print("Not ready yet:", error)
