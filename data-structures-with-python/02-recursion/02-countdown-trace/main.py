from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def countdown_trace(n: int) -> list[tuple[str, int]]:
    pass  # Step 1: validate n.
    events: list[tuple[str, int]] = []
    def walk(k: int) -> None:
        events.append(("enter", k))
        if k > 0:
            pass  # Step 2: visit the next smaller argument.
        pass  # Step 3: record leaving this call.
    walk(n)
    return events


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(countdown_trace(3))
    except NotImplementedError as error:
        print("Not ready yet:", error)
