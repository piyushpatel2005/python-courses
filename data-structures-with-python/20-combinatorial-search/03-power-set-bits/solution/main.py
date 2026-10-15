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


def selected_bit(mask: int, index: int) -> bool:
    return bool(mask & (1 << index))


def subset_for_mask(values: list[object], mask: int) -> tuple[object, ...]:
    return tuple(value for i, value in enumerate(values) if selected_bit(mask, i))


def power_set_bits(
    items: list[object] | tuple[object, ...],
) -> list[tuple[object, ...]]:
    values = _options(items)
    return [subset_for_mask(values, mask) for mask in range(1 << len(values))]


if __name__ == "__main__":
    try:
        print(power_set_bits(["pen", "tape"]))
    except NotImplementedError as error:
        print(error)
