from solution import *


def test_bit_membership():
    assert selected_bit(5, 0) is True and selected_bit(5, 1) is False
    assert selected_bit(5, 2) is True and selected_bit(0, 0) is False
    import ast, inspect

    assert any(
        isinstance(n, ast.BitAnd)
        for n in ast.walk(ast.parse(inspect.getsource(selected_bit)))
    )


def test_materialize_one_mask():
    import solution as submitted

    original = submitted.selected_bit
    submitted.selected_bit = lambda mask, i: bool(mask & (1 << i))
    try:
        assert subset_for_mask([8, 2, 6], 5) == (8, 6)
        assert subset_for_mask([8, 2, 6], 0) == ()
        assert subset_for_mask([], 0) == ()
    finally:
        submitted.selected_bit = original
