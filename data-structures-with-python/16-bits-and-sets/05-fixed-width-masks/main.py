from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def invert_field(value: int, width: int) -> int:
    pass  # TODO: check value type
    pass  # TODO: validate width
    mask = (1 << width) - 1
    return None  # TODO: apply complement and mask
if __name__ == '__main__':
    try:
        print('Five bits:', invert_field(13, 5))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
