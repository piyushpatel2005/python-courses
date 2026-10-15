from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_count():
    'Reject negative or non-integer input before entering the loop.'
    expect_error(ValueError, lambda: count_bits(-1))
    expect_error(TypeError, lambda: count_bits(1.5))


def test_count_active_bits():
    'Replace the loop placeholder with a bitwise loop that counts each set bit once.'
    for value in [0, 1, 6, 31, 64, (1 << 130) | 3]:
        assert count_bits(value) == bin(value).count('1')
    import ast, inspect
    syntax = ast.parse(inspect.getsource(count_bits))
    assert any(isinstance(n, (ast.While, ast.For)) for n in ast.walk(syntax))
    assert any(isinstance(n, (ast.BitAnd, ast.RShift)) for n in ast.walk(syntax))
    for n in ast.walk(syntax):
        if isinstance(n, ast.Call):
            assert getattr(n.func, 'id', getattr(n.func, 'attr', '')) not in {'bit_count', 'bin', 'str', 'format', 'count'}
