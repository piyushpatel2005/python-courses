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


def unused_indices(used: list[bool]) -> list[int]:
    return [index for index, taken in enumerate(used) if not taken]


def choose_position(
    values: list[object], index: int, path: list[object], used: list[bool]
) -> None:
    path.append(values[index])
    used[index] = True


def release_position(index: int, path: list[object], used: list[bool]) -> None:
    path.pop()
    used[index] = False


def permutations(
    items: list[object] | tuple[object, ...], r: int
) -> list[tuple[object, ...]]:
    values = _options(items)
    _length(r)
    if r > len(values):
        return []
    result, path = [], []
    used = [False] * len(values)

    def visit() -> None:
        if len(path) == r:
            result.append(tuple(path))
            return
        for index in unused_indices(used):
            choose_position(values, index, path, used)
            visit()
            release_position(index, path, used)

    visit()
    return result


if __name__ == "__main__":
    try:
        print(permutations(["north", "south", "west"], 2))
    except NotImplementedError as error:
        print(error)
