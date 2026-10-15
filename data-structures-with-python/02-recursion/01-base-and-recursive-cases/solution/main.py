from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def steps_to_zero(n: int) -> int:
    _check_n(n)
    if n == 0:
        return 0
    return 1 + steps_to_zero(n - 1)


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(steps_to_zero(5))
    except NotImplementedError as error:
        print("Not ready yet:", error)
