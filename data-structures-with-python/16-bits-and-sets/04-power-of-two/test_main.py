from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_power_input():
    'Raise `TypeError` when the input is not an integer.'
    expect_error(TypeError, lambda: is_power_of_two(2.0))
    expect_error(TypeError, lambda: is_power_of_two('8'))


def test_recognize_one_bit():
    'Use bitwise operations to return a boolean that accepts exactly positive one-bit values, including 1.'
    for value in [-8, -1, 0, 1, 2, 3, 64, 72, 1 << 150, (1 << 150)+1]:
        assert is_power_of_two(value) is (value > 0 and bin(value).count('1') == 1)
    import ast, inspect
    assert any(isinstance(n, (ast.BitAnd, ast.RShift)) for n in ast.walk(ast.parse(inspect.getsource(is_power_of_two))))
