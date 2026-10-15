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
            pass  # TODO: combine this parent's two children
if __name__ == '__main__':
    try:
        tree = SegmentTree([4, -2, 7, 1, 3])
        tree.build()
        print('Root sum:', tree.tree[1])
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
