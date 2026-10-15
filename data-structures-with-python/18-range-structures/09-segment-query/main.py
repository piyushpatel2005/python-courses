from __future__ import annotations

class SegmentTree:
    identity: int | float = 0

    def _combine(self: SegmentTree, left: int | float, right: int | float) -> int | float:
        return left + right

    def __init__(self: SegmentTree, values: list[int]) -> None:
        self.n: int = len(values)
        self.size: int = 1
        while self.size < self.n:
            self.size *= 2
        self.tree: list[int | float] = [self.identity] * (2 * self.size)
        for position, value in enumerate(values):
            self.tree[self.size + position] = value

    def build(self: SegmentTree) -> None:
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = self._combine(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self: SegmentTree, left: int, right: int) -> int | float:
        pass  # TODO: validate the public interval
        left += self.size
        right += self.size
        left_total = self.identity
        right_total = self.identity
        while left < right:
            pass  # TODO: consume an unmatched left boundary node
            pass  # TODO: consume the node before the right boundary
            left //= 2
            right //= 2
        return self._combine(left_total, right_total)
if __name__ == '__main__':
    try:
        tree = SegmentTree([4, -2, 7, 1, 3])
        tree.build()
        print('Range:', tree.query(1, 4))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
