from solution import *

def test_01_csv_columns():
    assert readings.shape == (2, 2)
    assert np.array_equal(readings, [[3, 8], [5, 2]])
