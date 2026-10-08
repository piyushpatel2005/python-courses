from solution import *

def test_01_unroll_rows():
    for grid in (np.array([[3, 1], [4, 2]]), np.arange(12).reshape(3, 4)):
        result = unroll_counts(grid)
        assert result.shape == (grid.size,) and np.array_equal(result, grid.ravel())

def test_02_pack_four_columns():
    for values in (np.arange(8), np.arange(12) + 9):
        result = pack_counts(values)
        assert result.shape == (values.size // 4, 4)
        assert np.array_equal(result.ravel(), values)
