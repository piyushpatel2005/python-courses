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
        return self.find(a), self.find(b)

    def merge_roots(self, root_a: int, root_b: int) -> bool:
        if root_a == root_b:
            return False
        self._link(root_a, root_b)
        return True

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.union_roots(a, b)
        return self.merge_roots(root_a, root_b)

    def redirect_parent(self, item: int, root: int) -> int:
        previous = self.parent[item]
        self.parent[item] = root
        return previous

    def compress_to(self, item: int, root: int) -> None:
        while item != root:
            item = self.redirect_parent(item, root)

    def find_compressed(self, item: int) -> int:
        self._check(item)
        root = self.root_from(item)
        self.compress_to(item, root)
        return root

    def compressed_roots(self, a: int, b: int) -> tuple[int, int]:
        return self.find_compressed(a), self.find_compressed(b)

    def smaller_first(self, root_a: int, root_b: int) -> tuple[int, int]:
        if self.size[root_a] > self.size[root_b]:
            return root_b, root_a
        return root_a, root_b

    def union_by_size(self, a: int, b: int) -> bool:
        root_a, root_b = self.compressed_roots(a, b)
        small, large = self.smaller_first(root_a, root_b)
        return self.merge_roots(small, large)

    def root_flags(self) -> list[bool]:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete root_flags")

    @staticmethod
    def count_root_flags(flags: list[bool]) -> int:
        # Complete this small step before moving to the next task.
        raise NotImplementedError("Complete count_root_flags")

    def component_count(self) -> int:
        return self.count_root_flags(self.root_flags())


if __name__ == "__main__":
    try:
        groups = DisjointSet(4)
        print(groups.component_count())
        groups.union_by_size(1, 3)
        print(groups.component_count())
    except NotImplementedError as error:
        print(error)
