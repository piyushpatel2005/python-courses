from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def fibonacci_tree(n: int) -> tuple[int, int]:
    _check_n(n, 12)
    if n < 2:
        return n, 1
    left, left_calls = fibonacci_tree(n - 1)
    right, right_calls = fibonacci_tree(n - 2)
    return left + right, 1 + left_calls + right_calls


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(fibonacci_tree(6))
    except NotImplementedError as error:
        print("Not ready yet:", error)
