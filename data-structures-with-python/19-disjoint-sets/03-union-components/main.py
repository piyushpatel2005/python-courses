from __future__ import annotations


class DisjointSet:
    @staticmethod
    def validate_size(n: int) -> None:
        if type(n) is not int or n < 0:
            raise ValueError("n must be a nonnegative integer")

    @staticmethod
    def initial_parents(n: int) -> list[int]:
        return list(range(n))

    @staticmethod
    def initial_sizes(n: int) -> list[int]:
        return [1] * n

    def __init__(self, n: int) -> None:
        self.validate_size(n)
        self.parent: list[int] = self.initial_parents(n)
        self.size: list[int] = self.initial_sizes(n)

    def _check(self, item: int) -> None:
        if type(item) is not int or not 0 <= item < len(self.parent):
            raise IndexError("unknown item")

    def is_root(self, item: int) -> bool:
        return self.parent[item] == item

    def root_from(self, item: int) -> int:
        while not self.is_root(item):
            item = self.parent[item]
        return item

    def find(self, item: int) -> int:
        self._check(item)
        return self.root_from(item)

    def _link(self, child: int, root: int) -> None:
        self.parent[child] = root
        self.size[root] += self.size[child]

    def union_roots(self, a: int, b: int) -> tuple[int, int]:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete union_roots")

    def merge_roots(self, root_a: int, root_b: int) -> bool:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete merge_roots")

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.union_roots(a, b)
        return self.merge_roots(root_a, root_b)


if __name__ == "__main__":
    try:
        groups = DisjointSet(4)
        print(groups.union(0, 2))
        print(groups.find(0) == groups.find(2))
    except NotImplementedError as error:
        print(error)
