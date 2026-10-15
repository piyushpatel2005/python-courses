from __future__ import annotations

from typing import Any, Callable, Iterable

def family_indices(index: int, size: int) -> tuple[int | None, int | None, int | None]:
    # TODO task 1: In `family_indices`, reject an index outside the heap shape.
    pass
    # TODO task 2: In `family_indices`, return the parent and existing child positions, using `None` for missing relatives.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(family_indices(1, 6))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
