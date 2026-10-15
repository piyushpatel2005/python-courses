from __future__ import annotations

def is_power_of_two(value: int) -> bool:
    pass  # TODO: reject non-integers
    return None  # TODO: test positivity and one-bit shape
if __name__ == '__main__':
    try:
        print('Capacities:', [is_power_of_two(v) for v in [0, 1, 32, 36]])
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
