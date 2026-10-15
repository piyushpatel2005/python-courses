from __future__ import annotations


class DisjointSet:
    @staticmethod
    def validate_size(n: int) -> None:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete validate_size")

    @staticmethod
    def initial_parents(n: int) -> list[int]:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete initial_parents")

    @staticmethod
    def initial_sizes(n: int) -> list[int]:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete initial_sizes")

    def __init__(self, n: int) -> None:
        self.validate_size(n)
        self.parent: list[int] = self.initial_parents(n)
        self.size: list[int] = self.initial_sizes(n)

    def _check(self, item: int) -> None:
        if type(item) is not int or not 0 <= item < len(self.parent):
            raise IndexError("unknown item")


if __name__ == "__main__":
    try:
        groups = DisjointSet(3)
        print(groups.parent, groups.size)
    except NotImplementedError as error:
        print(error)
