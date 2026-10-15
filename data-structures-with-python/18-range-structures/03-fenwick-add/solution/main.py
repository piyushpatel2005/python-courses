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
if __name__ == '__main__':
    try:
        index = Fenwick(5)
        index.add(0, 4)
        index.add(4, 9)
        print('Blocks:', index.tree)
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
