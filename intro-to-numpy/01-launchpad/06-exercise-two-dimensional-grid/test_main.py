from solution import station_grid
import numpy as np


def test_station_grid():
    """Convert rectangular rows without changing their layout"""
    for rows in ([[5, 6], [7, 8]], [[1, 2, 3], [4, 5, 6]]):
        grid = station_grid(rows)
        assert isinstance(grid, np.ndarray), "Return the NumPy array you create from rows."
        assert grid.shape == (len(rows), len(rows[0])), "Preserve the incoming row and column counts."
        assert grid.tolist() == rows, "Use the supplied rows so the readings stay unchanged."
