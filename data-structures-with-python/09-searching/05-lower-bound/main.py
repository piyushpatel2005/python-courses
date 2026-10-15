from __future__ import annotations

def lower_bound(values: list[int], target: int) -> int:
    # TODO: complete the numbered steps for this function.
    return None


def lower_step(values: list[int], target: int, lo: int, hi: int) -> tuple[int, int]:
    # TODO: complete the numbered steps for this function.
    return lo, hi


if __name__ == "__main__":
    try:
        print(lower_bound([2, 4, 4, 4, 8], 4))
        print(lower_bound([2, 4, 4, 4, 8], 6))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
