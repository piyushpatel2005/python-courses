from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def lowbit(index: int) -> int:
    require_nonnegative(index, 'index')
    return index & -index

class Fenwick:

    def __init__(self: Fenwick, size: int) -> None:
        require_nonnegative(size, 'size')
        self.n: int = size
        self.tree: list[int] = [0] * (size + 1)

    def add(self: Fenwick, position: int, delta: int) -> None:
        if type(position) is not int or type(delta) is not int:
            raise TypeError('position and delta must be integers')
        if not 0 <= position < self.n:
            raise IndexError('position outside sequence')
        index = position + 1
        while index <= self.n:
            self.tree[index] += delta
            index += lowbit(index)

    def prefix(self: Fenwick, end: int) -> int:
        if type(end) is not int:
            raise TypeError('end must be an integer')
        if not 0 <= end <= self.n:
            raise IndexError('boundary outside sequence')
        total = 0
        index = end
        while index > 0:
            total += self.tree[index]
            index -= lowbit(index)
        return total

    def range_sum(self: Fenwick, left: int, right: int) -> int:
        if type(left) is not int or type(right) is not int:
            raise TypeError('boundaries must be integers')
        if not 0 <= left <= right <= self.n:
            raise IndexError('invalid half-open interval')
        return self.prefix(right) - self.prefix(left)

    @classmethod
    def from_values(cls: type[Fenwick], values: list[int]) -> Fenwick:
        result = cls(len(values))
        for position, value in enumerate(values):
            result.add(position, value)
        return result

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

class RangeDashboard:

    def __init__(self: RangeDashboard, values: list[int]) -> None:
        self.values: list[int] = values[:]
        self.sums: Fenwick = Fenwick.from_values(values)
        self.minimums: MinTree = MinTree(values)
        self.minimums.build()

    def replace(self: RangeDashboard, position: int, value: int) -> None:
        if type(position) is not int or type(value) is not int:
            raise TypeError('position and value must be integers')
        if not 0 <= position < len(self.values):
            raise IndexError('position outside sequence')
        delta = value - self.values[position]
        self.sums.add(position, delta)
        self.minimums.update(position, value)
        self.values[position] = value

    def report(self: RangeDashboard, left: int, right: int) -> dict[str, int | float]:
        return {'sum': self.sums.range_sum(left, right), 'minimum': self.minimums.query(left, right)}
if __name__ == '__main__':
    try:
        dashboard = RangeDashboard([4, -2, 7, 1, 3])
        dashboard.replace(1, 6)
        print('Report:', dashboard.report(1, 4))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
