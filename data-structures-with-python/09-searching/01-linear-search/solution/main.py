from __future__ import annotations

def linear_search(values: list[object], target: object) -> int:
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    try:
        print(linear_search([12, 7, 12, 5], 12))
        print(linear_search([12, 7, 12, 5], 9))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
