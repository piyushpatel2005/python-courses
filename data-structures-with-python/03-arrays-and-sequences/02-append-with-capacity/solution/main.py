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
        if not 0 <= index < self.size:
            raise IndexError("index outside occupied positions")
        return self._data[index]

    def _grow(self) -> None:
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for index in range(self.size):
            new_data[index] = self._data[index]
        self._data = new_data
        self.capacity = new_capacity

    def append(self, value: Any) -> None:
        if self.size == self.capacity:
            self._grow()
        self._data[self.size] = value
        self.size += 1


# Supplied Run probe; the unfinished operation is reported safely.
if __name__ == "__main__":
    try:
        array = Array([3])
        array.append(8)
        array.append(None)
        print(array.snapshot(), array.size, array.capacity)
    except NotImplementedError as error:
        print("Not ready yet:", error)
