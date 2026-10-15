from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def count_bits(value: int) -> int:
    pass  # TODO: validate value
    count = 0
    pass  # TODO: consume bits and update count
    return count
if __name__ == '__main__':
    try:
        print('Active flags:', count_bits(43))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
