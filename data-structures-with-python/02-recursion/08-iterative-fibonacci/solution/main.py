from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def fibonacci_loop(n: int) -> tuple[int, int]:
    _check_n(n)
    a, b = 0, 1
    updates = 0
    for _ in range(n):
        a, b = b, a + b
        updates += 1
    return a, updates


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(fibonacci_loop(9))
    except NotImplementedError as error:
        print("Not ready yet:", error)
