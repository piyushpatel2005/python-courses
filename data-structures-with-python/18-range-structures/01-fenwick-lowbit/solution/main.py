from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def lowbit(index: int) -> int:
    require_nonnegative(index, 'index')
    return index & -index
if __name__ == '__main__':
    try:
        print('Steps:', [lowbit(i) for i in [0, 1, 6, 8]])
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
