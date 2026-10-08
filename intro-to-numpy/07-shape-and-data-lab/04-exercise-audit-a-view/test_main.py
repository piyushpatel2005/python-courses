from solution import *

def test_01_column_scan():
    for grid in (np.arange(6).reshape(2, 3), np.arange(12).reshape(4, 3)):
        assert np.array_equal(column_scan(grid), grid.T.ravel())

def test_02_check_storage():
    for grid in (np.arange(6).reshape(2, 3), np.arange(12).reshape(3, 4).T):
        row, col = grid.ravel(), grid.T.ravel()
        assert audit_scans(grid) == (np.shares_memory(grid, row), np.shares_memory(grid, col))
