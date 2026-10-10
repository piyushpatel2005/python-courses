from solution import frames
import numpy as np


def test_three_frames():
    """Add a frame without changing the two existing frames"""
    assert isinstance(frames, np.ndarray), "Keep frames as a NumPy array."
    assert frames.shape == (3, 2, 2), "Place the new two-by-two frame beside the other frames inside the outer list."
    expected = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 8], [7, 6]]]
    assert frames.tolist() == expected, "Keep the first two frames and append [[9, 8], [7, 6]] as frame three."
