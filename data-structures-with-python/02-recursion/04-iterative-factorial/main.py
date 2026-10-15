from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def factorial_loop(n: int) -> tuple[int, int]:
    pass  # Step 1: validate n.
    product = 1
    multiplications = 0
    for factor in range(1, n + 1):
        pass  # Step 2: extend the product.
        pass  # Step 3: count this multiplication.
    return product, multiplications


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(factorial_loop(5))
    except NotImplementedError as error:
        print("Not ready yet:", error)
