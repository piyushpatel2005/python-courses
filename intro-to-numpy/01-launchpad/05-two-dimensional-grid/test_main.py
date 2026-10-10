from solution import levels
import numpy as np


def test_third_row():
    """Keep the first two rows and add the third"""
    assert isinstance(levels, np.ndarray), "Keep the nested rows inside np.array(...)."
    assert levels.shape == (3, 2), "Add one row of two readings; the shape should be (3, 2)."
    assert levels.tolist() == [[1, 2], [4, 5], [7, 8]], "Keep the original two rows and add [7, 8] after them."
