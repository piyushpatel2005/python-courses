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
        if type(left) is not int or type(right) is not int:
            raise TypeError('boundaries must be integers')
        if not 0 <= left <= right <= self.n:
            raise IndexError('invalid half-open interval')
        left += self.size
        right += self.size
        left_total = self.identity
        right_total = self.identity
        while left < right:
            if left % 2:
                left_total = self._combine(left_total, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                right_total = self._combine(self.tree[right], right_total)
            left //= 2
            right //= 2
        return self._combine(left_total, right_total)

    def update(self: SegmentTree, position: int, value: int) -> None:
        if type(position) is not int or type(value) is not int:
            raise TypeError('position and value must be integers')
        if not 0 <= position < self.n:
            raise IndexError('position outside sequence')
        index = self.size + position
        self.tree[index] = value
        index //= 2
        while index >= 1:
            self.tree[index] = self._combine(self.tree[2 * index], self.tree[2 * index + 1])
            index //= 2

class MinTree(SegmentTree):
    identity: int | float = float('inf')

    def _combine(self: MinTree, left: int | float, right: int | float) -> int | float:
        return min(left, right)
if __name__ == '__main__':
    try:
        tree = MinTree([4, -2, 7, 1, 3])
        tree.build()
        print('Minimum:', tree.query(1, 5))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
