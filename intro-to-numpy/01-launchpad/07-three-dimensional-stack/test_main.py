from solution import *
import numpy as np

def test_three_frames():
    """The stack contains three two-by-two frames"""
    assert frames.shape == (3, 2, 2) and frames[-1].tolist() == [[9, 8], [7, 6]]
