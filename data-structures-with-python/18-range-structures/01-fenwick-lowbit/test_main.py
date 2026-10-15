from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_lowbit():
    'Validate `index` as a nonnegative integer.'
    expect_error(ValueError, lambda: lowbit(-1))
    expect_error(TypeError, lambda: lowbit(1.5))


def test_isolate_lowbit():
    'Return the isolated lowest set bit, or zero for index zero.'
    for index, step in [(0,0), (1,1), (6,2), (12,4), (13,1), (1<<95,1<<95), ((1<<95)+8,8)]:
        assert lowbit(index) == step
