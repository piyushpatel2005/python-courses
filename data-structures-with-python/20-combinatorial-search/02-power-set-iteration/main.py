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


def append_choice(subset: tuple[object, ...], value: object) -> tuple[object, ...]:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete append_choice")


def subsets_with(
    subsets: list[tuple[object, ...]], value: object
) -> list[tuple[object, ...]]:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete subsets_with")


def power_set(items: list[object] | tuple[object, ...]) -> list[tuple[object, ...]]:
    values = _options(items)
    result = [()]
    for value in values:
        result.extend(subsets_with(result, value))
    return result


if __name__ == "__main__":
    try:
        print(power_set(["pen", "tape"]))
    except NotImplementedError as error:
        print(error)
