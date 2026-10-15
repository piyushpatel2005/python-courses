from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def read_bit(value: int, position: int) -> int:
    pass  # TODO: validate value
    pass  # TODO: validate position
    return None  # TODO: isolate one bit
if __name__ == '__main__':
    try:
        print('Bits:', read_bit(22, 1), read_bit(22, 3))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
