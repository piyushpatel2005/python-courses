from solution import *
import numpy as np

def test_board_metadata():
    """Two frames yield eight cells but first-axis length two"""
    assert pads.ndim == 3 and pads.shape == (2, 2, 2) and pads.size == 8 and len(pads) == 2
    assert pads.tolist() == [[[2, 4], [6, 8]], [[10, 12], [14, 16]]]
