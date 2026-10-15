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


def word_complete(path: tuple[object, ...], r: int) -> bool:
    return len(path) == r


def extend_word(path: tuple[object, ...], value: object) -> tuple[object, ...]:
    return path + (value,)


def words(
    symbols: list[object] | tuple[object, ...], r: int
) -> list[tuple[object, ...]]:
    values = _options(symbols)
    _length(r)
    result = []

    def visit(path: tuple[object, ...]) -> None:
        if word_complete(path, r):
            result.append(path)
            return
        for value in values:
            visit(extend_word(path, value))

    visit(())
    return result


if __name__ == "__main__":
    try:
        print(words(["short", "long"], 2))
    except NotImplementedError as error:
        print(error)
