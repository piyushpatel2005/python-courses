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


def repeated_next(index: int) -> int:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete repeated_next")


def repeated_snapshot(path: list[object]) -> tuple[object, ...]:
    # Complete this small step before moving to the next task.
    raise NotImplementedError("Complete repeated_snapshot")


def combinations_repeated(
    items: list[object] | tuple[object, ...], r: int
) -> list[tuple[object, ...]]:
    values = _options(items)
    _length(r)
    result, path = [], []

    def visit(start: int) -> None:
        if len(path) == r:
            result.append(repeated_snapshot(path))
            return
        for index in range(start, len(values)):
            path.append(values[index])
            visit(repeated_next(index))
            path.pop()

    visit(0)
    return result


if __name__ == "__main__":
    try:
        print(combinations_repeated(["matte", "gloss"], 2))
    except NotImplementedError as error:
        print(error)
