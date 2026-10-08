from solution import *

def test_01_column_axis():
    assert column.shape == (3, 1)
    assert np.array_equal(column[:, 0], values)
