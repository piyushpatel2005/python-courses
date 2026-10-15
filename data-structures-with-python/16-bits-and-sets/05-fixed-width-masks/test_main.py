from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_field_value():
    'Reject non-integer `value`; negative integers remain valid.'
    expect_error(TypeError, lambda: invert_field(1.5, 3))
    expect_error(TypeError, lambda: invert_field('1', 3))


def test_validate_field_width():
    'Validate `width` as a nonnegative integer with the supplied helper.'
    expect_error(ValueError, lambda: invert_field(2, -1))
    expect_error(TypeError, lambda: invert_field(2, 1.5))
    expect_error(TypeError, lambda: invert_field(2, True))


def test_invert_low_field():
    'Return the complemented low-width field using the supplied mask.'
    for width in [0, 1, 5, 90]:
        for value in [-17, -1, 0, 9, (1 << 120)+3]:
            assert invert_field(value, width) == (2**width-1) - value % (2**width)
