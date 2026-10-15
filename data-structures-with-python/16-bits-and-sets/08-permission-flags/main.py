from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')
VIEW = 1 << 0
EDIT = 1 << 1
EXPORT = 1 << 2

def allows_all(held: int, requested: int) -> bool:
    pass  # TODO: validate both masks
    return None  # TODO: compare the complete requested mask
if __name__ == '__main__':
    try:
        print('Edit allowed:', allows_all(VIEW | EXPORT, VIEW | EDIT))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
