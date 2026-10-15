from __future__ import annotations

def halving_trace(n: int) -> tuple[list[int], int]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    sizes = []
    reductions = 0
    while n > 1:
        sizes.append(n)
        reductions += 1
        n //= 2
    return sizes, reductions


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(halving_trace(19))
    except NotImplementedError as error:
        print("Not ready yet:", error)
