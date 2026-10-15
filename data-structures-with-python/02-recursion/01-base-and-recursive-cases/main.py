from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def steps_to_zero(n: int) -> int:
    pass  # Step 1: validate n.
    if n == 0:
        return None  # Step 2: answer the base case.
    return None  # Step 3: solve and combine the smaller problem.


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(steps_to_zero(5))
    except NotImplementedError as error:
        print("Not ready yet:", error)
