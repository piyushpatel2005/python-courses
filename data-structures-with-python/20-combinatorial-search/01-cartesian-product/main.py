from __future__ import annotations


def _options(items: list[object] | tuple[object, ...]) -> list[object]:
    values = list(items)
    if len(values) > 8:
        raise ValueError("use at most eight options")
    if any(values[i] == values[j] for i in range(len(values)) for j in range(i)):
        raise ValueError("options must be distinct")
    return values


def _length(r: int) -> None:
    if type(r) is not int or not 0 <= r <= 6:
        raise ValueError("length must be an integer from zero through six")


def pair_row(first: object, right: list[object]) -> list[tuple[object, object]]:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete pair_row")


def product_rows(
    left: list[object], right: list[object]
) -> list[tuple[object, object]]:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete product_rows")


def cartesian_product(
    left: list[object] | tuple[object, ...], right: list[object] | tuple[object, ...]
) -> list[tuple[object, object]]:
    left, right = _options(left), _options(right)
    return product_rows(left, right)


if __name__ == "__main__":
    try:
        print(cartesian_product(["red", "blue"], [1, 2]))
    except NotImplementedError as error:
        print(error)
