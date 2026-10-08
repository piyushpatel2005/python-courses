from solution import *
import numpy as np

def test_station_grid():
    """Nested rows become a two-dimensional grid"""
    grid = station_grid([[5, 6], [7, 8]])
    assert isinstance(grid, np.ndarray) and grid.shape == (2, 2)
    assert station_grid([[1, 2, 3], [4, 5, 6]]).tolist() == [[1, 2, 3], [4, 5, 6]]
