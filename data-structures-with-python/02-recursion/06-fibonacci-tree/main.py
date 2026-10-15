from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def fibonacci_tree(n: int) -> tuple[int, int]:
    pass  # Step 1: validate n.
    if n < 2:
        return None, 0  # Step 2: answer either Fibonacci base case.
    return None, 0  # Step 3: combine both recursive branches.


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(fibonacci_tree(6))
    except NotImplementedError as error:
        print("Not ready yet:", error)
