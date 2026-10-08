from solution import *
import numpy as np

def test_sky_stack():
    """Snapshots preserve frame, row, and column axes"""
    data = sky_stack([[[1, 0]], [[0, 1]]])
    assert isinstance(data, np.ndarray) and data.shape == (2, 1, 2)
    assert sky_stack([[[2, 3], [4, 5]]]).tolist() == [[[2, 3], [4, 5]]]
