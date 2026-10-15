from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def factorial_recursive(n: int) -> tuple[int, int]:
    pass  # Step 1: validate n.
    if n == 0:
        return None, 0  # Step 2: return the base product and its call count.
    return None, 0  # Step 3: combine the recursive answer.


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(factorial_recursive(5))
    except NotImplementedError as error:
        print("Not ready yet:", error)
