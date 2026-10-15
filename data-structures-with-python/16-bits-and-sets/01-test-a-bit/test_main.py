from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_value():
    'Validate `value` with the supplied nonnegative-integer helper.'
    expect_error(ValueError, lambda: read_bit(-1, 0))
    expect_error(TypeError, lambda: read_bit(2.5, 0))


def test_validate_position():
    'Validate `position` with the same helper.'
    expect_error(ValueError, lambda: read_bit(3, -1))
    expect_error(TypeError, lambda: read_bit(3, 0.5))


def test_isolate_bit():
    'Return only the selected bit as integer 0 or 1 using bitwise operations.'
    for value in [0, 1, 22, (1 << 100) | 9]:
        for position in [0, 1, 3, 100, 101]:
            answer = read_bit(value, position)
            assert type(answer) is int
            assert answer == (value // (2 ** position)) % 2
    import ast, inspect
    assert any(isinstance(n, (ast.BitAnd, ast.RShift)) for n in ast.walk(ast.parse(inspect.getsource(read_bit))))
