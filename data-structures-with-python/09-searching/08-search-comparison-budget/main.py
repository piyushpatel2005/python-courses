from __future__ import annotations
from collections.abc import Callable

def compare_int(left: int, right: int) -> int:
    return (left > right) - (left < right)


def measured_binary_search(
    values: list[int],
    target: int,
    compare: Callable[[int, int], int] = compare_int,
) -> tuple[int, int]:
    # TODO: complete the numbered steps for this function.
    return None


def compare_at(values: list[int], index: int, target: int, compare: Callable[[int, int], int]) -> int:
    # TODO: complete the numbered steps for this function.
    return None


if __name__ == "__main__":
    try:
        print(measured_binary_search([1, 4, 9, 13, 18], 9))
        print(measured_binary_search([1, 4, 9, 13, 18], 12))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
