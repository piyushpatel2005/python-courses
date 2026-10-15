from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def tail_sum(n: int, accumulated: int = 0) -> int:
    _check_n(n)
    if n == 0:
        return accumulated
    return tail_sum(n - 1, accumulated + n)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(tail_sum(5, 10))
    except NotImplementedError as error:
        print("Not ready yet:", error)
