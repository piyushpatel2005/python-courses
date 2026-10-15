from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def fibonacci_memo(n: int) -> tuple[int, int]:
    pass  # Step 1: validate n.
    cache: dict[int, int] = {}
    misses = 0
    def fib(k: int) -> int:
        nonlocal misses
        if k in cache:
            pass  # Step 3: reuse a cached result before counting a miss.
        misses += 1
        if k < 2:
            value = k
        else:
            value = 0  # Step 2: compute this index from the two smaller indices.
        cache[k] = value
        return value
    value = fib(n)
    return value, misses


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(fibonacci_memo(9))
        print(fibonacci_memo(9))
    except NotImplementedError as error:
        print("Not ready yet:", error)
