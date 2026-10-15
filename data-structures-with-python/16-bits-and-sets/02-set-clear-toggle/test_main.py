from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_flags():
    'Reject negative or non-integer values and positions with the supplied helper.'
    expect_error(ValueError, lambda: change_bit(-1, 0, 'set'))
    expect_error(TypeError, lambda: change_bit(1.5, 0, 'set'))
    expect_error(ValueError, lambda: change_bit(1, -1, 'set'))


def test_set_flag():
    'In the `set` branch, return the value with the selected bit on.'
    for value in [0, 3, 19, 1 << 90]:
        for position in [0, 4, 90]:
            assert change_bit(value, position, 'set') == value | (1 << position)


def test_clear_flag():
    'In the `clear` branch, return the value with only the selected bit off.'
    for value in [0, 3, 19, (1 << 90) | 1]:
        for position in [0, 4, 90]:
            assert change_bit(value, position, 'clear') == value & ~(1 << position)


def test_toggle_flag():
    'In the `toggle` branch, return the value with the selected bit reversed.'
    for value in [0, 3, 19, (1 << 90) | 1]:
        for position in [0, 4, 90]:
            changed = change_bit(value, position, 'toggle')
            assert changed == value ^ (1 << position)
            assert change_bit(changed, position, 'toggle') == value
