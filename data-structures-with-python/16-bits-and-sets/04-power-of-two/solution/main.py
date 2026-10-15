from __future__ import annotations

def is_power_of_two(value: int) -> bool:
    if type(value) is not int:
        raise TypeError('value must be an integer')
    return value > 0 and (value & (value - 1)) == 0
if __name__ == '__main__':
    try:
        print('Capacities:', [is_power_of_two(v) for v in [0, 1, 32, 36]])
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
