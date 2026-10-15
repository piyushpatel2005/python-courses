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
        return [item == parent for item, parent in enumerate(self.parent)]

    @staticmethod
    def count_root_flags(flags: list[bool]) -> int:
        return sum(flags)

    def component_count(self) -> int:
        return self.count_root_flags(self.root_flags())


def _validate_edges(
    n: int, edges: list[tuple[int, ...] | list[int]], weighted: bool = False
) -> None:
    if type(n) is not int or n < 0:
        raise ValueError("invalid vertex count")
    for edge in edges:
        if len(edge) != (3 if weighted else 2):
            raise ValueError("wrong edge shape")
        for item in edge[:2]:
            if type(item) is not int or not 0 <= item < n:
                raise IndexError("unknown vertex")
        if weighted and type(edge[2]) is not int:
            raise ValueError("weights must be integers")


def edge_is_redundant(groups: DisjointSet, a: int, b: int) -> bool:
    return not groups.union_by_size(a, b)


def edge_pair(a: int, b: int) -> tuple[int, int]:
    return (a, b)


def first_redundant(
    n: int, edges: list[tuple[int, ...] | list[int]]
) -> tuple[int, int] | None:
    _validate_edges(n, edges)
    groups = DisjointSet(n)
    for a, b in edges:
        if edge_is_redundant(groups, a, b):
            return edge_pair(a, b)
    return None


def ordered_edges(
    edges: list[tuple[int, ...] | list[int]],
) -> list[tuple[int, ...] | list[int]]:
    return sorted(edges, key=lambda edge: edge[2])


def choose_forest_edges(
    groups: DisjointSet, edges: list[tuple[int, ...] | list[int]]
) -> list[tuple[int, int, int]]:
    chosen = []
    for a, b, weight in edges:
        if groups.union_by_size(a, b):
            chosen.append((a, b, weight))
    return chosen


def forest_weight(chosen: list[tuple[int, int, int]]) -> int:
    return sum(weight for _, _, weight in chosen)


def kruskal_forest(
    n: int, edges: list[tuple[int, ...] | list[int]]
) -> tuple[list[tuple[int, int, int]], int]:
    _validate_edges(n, edges, weighted=True)
    groups = DisjointSet(n)
    chosen = choose_forest_edges(groups, ordered_edges(edges))
    return chosen, forest_weight(chosen)


if __name__ == "__main__":
    try:
        print(kruskal_forest(5, [(0, 1, 7), (1, 2, 2), (0, 2, 4), (3, 4, -1)]))
    except NotImplementedError as error:
        print(error)
