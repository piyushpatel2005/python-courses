from __future__ import annotations

def binary_search(values: list[int], target: int) -> int:
    # TODO: complete the numbered steps for this function.
    lo, hi = 0, len(values)
    while lo < hi:
        # Replace this pause with the halving step.
        break
    return None


if __name__ == "__main__":
    try:
        print(binary_search([1, 4, 4, 9, 15], 4))
        print(binary_search([1, 4, 4, 9, 15], 8))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
