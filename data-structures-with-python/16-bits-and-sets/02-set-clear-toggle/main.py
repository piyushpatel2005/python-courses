from __future__ import annotations

def require_nonnegative(value: int, name: str) -> None:
    if type(value) is not int:
        raise TypeError(name + ' must be an integer')
    if value < 0:
        raise ValueError(name + ' must be nonnegative')

def change_bit(value: int, position: int, action: str) -> int:
    pass  # TODO: validate both arguments
    mask = 1 << position
    if action == 'set':
        return None  # TODO: set the bit
    if action == 'clear':
        return None  # TODO: clear the bit
    if action == 'toggle':
        return None  # TODO: toggle the bit
    raise ValueError('unknown action')
if __name__ == '__main__':
    try:
        print('Changed:', change_bit(19, 4, 'clear'))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
