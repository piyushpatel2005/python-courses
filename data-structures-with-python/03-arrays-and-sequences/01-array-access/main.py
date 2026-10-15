from __future__ import annotations
from typing import Any
from collections.abc import Iterable

class Array:
    def __init__(self, values: Iterable[Any] = ()) -> None:
        initial = list(values)
        self.size: int = len(initial)
        self.capacity: int = max(1, self.size)
        self._data: list[Any] = initial + [None] * (self.capacity - self.size)

    def snapshot(self) -> list[Any]:
        return self._data[:self.size]

    def get(self, index: int) -> Any:
        pass  # Step 1: reject invalid indices before mutation.
        return None  # Step 2: read the validated slot.


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        array = Array(["compass", "rope"])
        print(array.get(1))
    except NotImplementedError as error:
        print("Not ready yet:", error)
