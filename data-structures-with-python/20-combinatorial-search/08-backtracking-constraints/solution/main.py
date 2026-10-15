from __future__ import annotations


def _budget_inputs(weights: list[int] | tuple[int, ...], capacity: int) -> list[int]:
    values = list(weights)
    if len(values) > 8 or any(type(w) is not int or w < 0 for w in values):
        raise ValueError("use at most eight nonnegative integer weights")
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    return values


def fits_budget(total: int, weight: int, capacity: int) -> bool:
    return total + weight <= capacity


def budget_snapshot(path: list[int]) -> tuple[int, ...]:
    return tuple(path)


def budget_selections(
    weights: list[int] | tuple[int, ...], capacity: int
) -> tuple[list[tuple[int, ...]], int]:
    values = _budget_inputs(weights, capacity)
    result, path = [], []
    visited = 0

    def visit(index: int, total: int) -> None:
        nonlocal visited
        visited += 1
        if index == len(values):
            result.append(budget_snapshot(path))
            return
        visit(index + 1, total)
        if fits_budget(total, values[index], capacity):
            path.append(index)
            visit(index + 1, total + values[index])
            path.pop()

    visit(0, 0)
    return result, visited


if __name__ == "__main__":
    try:
        print(budget_selections([3, 2, 4], 4))
    except NotImplementedError as error:
        print(error)
