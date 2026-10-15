from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_permissions():
    'Validate both masks as nonnegative integers.'
    expect_error(ValueError, lambda: allows_all(-1, 0))
    expect_error(ValueError, lambda: allows_all(1, -1))
    expect_error(TypeError, lambda: allows_all(1.5, 0))


def test_all_requested_bits():
    'Return whether the intersection contains every requested bit, including an empty request.'
    for held in [0, 1, 5, 7, (1 << 110) | 2]:
        for requested in [0, 1, 3, 7, 1 << 110]:
            assert allows_all(held, requested) is ((held & requested) == requested)
