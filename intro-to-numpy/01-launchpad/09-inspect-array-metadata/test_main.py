from solution import pads
import numpy as np


def test_board_metadata():
    """The stack has three axes, eight values, and two frames"""
    assert isinstance(pads, np.ndarray), "Keep pads as a NumPy array."
    assert pads.shape == (2, 2, 2), "Wrap the original board as frame one and add the new board as frame two."
    assert pads.ndim == 3 and pads.size == 8 and len(pads) == 2, "The completed stack needs three axes and eight values."
    assert pads.tolist() == [[[2, 4], [6, 8]], [[10, 12], [14, 16]]], "Preserve the first frame and put the new readings in the second frame."
