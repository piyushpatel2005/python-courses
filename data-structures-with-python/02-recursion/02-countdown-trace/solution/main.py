from __future__ import annotations

def _check_n(n: int, limit: int = 100) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if not 0 <= n <= limit:
        raise ValueError("n is outside the exercise's safe range")

def countdown_trace(n: int) -> list[tuple[str, int]]:
    _check_n(n)
    events: list[tuple[str, int]] = []
    def walk(k: int) -> None:
        events.append(("enter", k))
        if k > 0:
            walk(k - 1)
        events.append(("leave", k))
    walk(n)
    return events


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        print(countdown_trace(3))
    except NotImplementedError as error:
        print("Not ready yet:", error)
