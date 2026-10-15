from solution import *


def test_copy_and_extend_one_subset():
    old = (4, 1)
    assert append_choice(old, 8) == (4, 1, 8) and old == (4, 1)
    assert append_choice((), 7) == (7,)


def test_snapshot_additions():
    import solution as submitted

    original = submitted.append_choice
    submitted.append_choice = lambda subset, value: subset + (value,)
    try:
        old = [(), (3,)]
        assert subsets_with(old, 9) == [(9,), (3, 9)]
        assert old == [(), (3,)] and subsets_with([], 9) == []
    finally:
        submitted.append_choice = original
