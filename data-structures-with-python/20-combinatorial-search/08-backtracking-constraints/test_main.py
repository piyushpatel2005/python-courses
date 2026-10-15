from solution import *


def test_include_budget_boundary():
    assert fits_budget(2, 3, 5) is True
    assert fits_budget(2, 4, 5) is False
    assert fits_budget(0, 0, 0) is True
    assert fits_budget(4, 0, 3) is False


def test_snapshot_selected_indices():
    path = [0, 2]
    saved = budget_snapshot(path)
    assert saved == (0, 2) and budget_snapshot([]) == ()
    path.clear()
    assert saved == (0, 2)
