from solution import *

def test_01_column_offsets():
    for offsets in (np.array([1, 3, 5, 7]), np.array([8, 2])):
        result = as_column(offsets)
        assert result.shape == (len(offsets), 1) and np.array_equal(result[:, 0], offsets)

def test_02_row_ticks():
    for ticks in (np.array([0, 10, 20]), np.array([6, 9])):
        result = as_row(ticks)
        assert result.shape == (1, len(ticks)) and np.array_equal(result[0], ticks)
