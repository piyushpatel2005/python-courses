from __future__ import annotations

class SegmentTree:
    identity: int | float = 0

    def _combine(self: SegmentTree, left: int | float, right: int | float) -> int | float:
        return left + right

    def __init__(self: SegmentTree, values: list[int]) -> None:
        self.n: int = 0  # TODO: record input length
        self.size: int = 1
        pass  # TODO: find the padded power-of-two capacity
        self.tree: list[int | float] = []  # TODO: allocate tree cells
        pass  # TODO: copy real leaf values
if __name__ == '__main__':
    try:
        tree = SegmentTree([4, -2, 7, 1, 3])
        print('Length and capacity:', tree.n, tree.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
