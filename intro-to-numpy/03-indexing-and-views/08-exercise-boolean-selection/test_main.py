from solution import *
import numpy as np

def test_censor():
    """Mask values below the supplied threshold"""
    assert np.array_equal(censor_weak(np.array([5, 2, 8, 3]), 4), [5, -1, 8, -1])
    assert np.array_equal(censor_weak(np.array([7, 10, 4, 12]), 9), [-1, 10, -1, 12])
    source = np.array([0, 5, 9, 5])
    assert np.array_equal(censor_weak(source, 5), [-1, 5, 9, 5])
    assert np.array_equal(source, [0, 5, 9, 5])
    class MaskProbe(np.ndarray):
        def __array_finalize__(self, obj):
            self.assigned = []

        def __setitem__(self, index, value):
            self.assigned.append(index)
            super().__setitem__(index, value)

    marked = censor_weak(np.array([0, 5, 9, 5]).view(MaskProbe), 5)
    assert any(isinstance(index, np.ndarray) and index.dtype.kind == 'b'
               and index.shape == marked.shape for index in getattr(marked, 'assigned', [])), "Assign using a boolean mask"
