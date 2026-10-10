from solution import *
import numpy as np

class _CoordinateProbe(np.ndarray):
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            self.coordinates.append(index)
        return super().__getitem__(index)

def _grid(values):
    grid = np.array(values).view(_CoordinateProbe)
    grid.coordinates = []
    return grid

def test_column():
    """Select column 1 across every row"""
    for values in ([[2, 6, 4], [7, 5, 8]], [[9, 1, 2], [3, 4, 5], [6, 8, 7]]):
        grid = _grid(values)
        column = locate(grid)[0]
        assert isinstance(column, np.ndarray)
        assert np.array_equal(column, [row[1] for row in values])
        assert any(isinstance(row, slice) and col == 1 for row, col in grid.coordinates), "Select with grid[:, 1]"

def test_corner():
    """Select the final row and final column"""
    for values in ([[2, 6, 4], [7, 5, 8]], [[9, 1, 2], [3, 4, 5], [6, 8, 7]]):
        grid = _grid(values)
        assert locate(grid)[1] == values[-1][-1]
        assert any(isinstance(row, (int, np.integer)) and isinstance(col, (int, np.integer))
                   and row % len(values) == len(values) - 1 and col % 3 == 2
                   for row, col in grid.coordinates), "Select the corner with row and column coordinates"
