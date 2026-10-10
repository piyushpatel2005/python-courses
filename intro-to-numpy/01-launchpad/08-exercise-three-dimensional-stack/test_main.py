from solution import sky_stack
import numpy as np


def test_sky_stack():
    """Preserve frame, row, and column counts and values"""
    for snapshots in ([[[1, 0]], [[0, 1]]], [[[2, 3], [4, 5]]]):
        result = sky_stack(snapshots)
        assert isinstance(result, np.ndarray), "Return a NumPy array of snapshots, not None or a list."
        expected_shape = (len(snapshots), len(snapshots[0]), len(snapshots[0][0]))
        assert result.shape == expected_shape, "Keep the input's three nesting levels: frames, rows, and columns."
        assert result.tolist() == snapshots, "Keep all supplied pixel values in their original frames."
