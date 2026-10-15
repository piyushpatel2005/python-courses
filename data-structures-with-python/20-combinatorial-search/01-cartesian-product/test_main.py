from solution import *


def test_one_cartesian_row():
    assert pair_row("m", [3, 1]) == [("m", 3), ("m", 1)]
    assert pair_row(2, [2]) == [(2, 2)]
    assert pair_row("m", []) == []


def test_join_cartesian_rows():
    import solution as submitted

    original = submitted.pair_row
    submitted.pair_row = lambda first, right: [(first, v) for v in right]
    try:
        assert product_rows([9, 4], [2, 1]) == [(9, 2), (9, 1), (4, 2), (4, 1)]
        assert product_rows([], [2]) == [] and product_rows([2], []) == []
    finally:
        submitted.pair_row = original
