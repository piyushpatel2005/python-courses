from solution import *
import numpy as np

def test_mute():
    """Assign into a stepped slice, leaving endpoints alone"""
    assert np.array_equal(mute_interior(np.array([3, 4, 5, 6, 7])), [3, -9, 5, -9, 7])
    assert np.array_equal(mute_interior(np.array([1, 2, 3, 4, 5, 6])), [1, -9, 3, -9, 5, 6])
    source = np.array([8, 7, 6, 5, 4, 3, 2])
    assert np.array_equal(mute_interior(source), [8, -9, 6, -9, 4, -9, 2])
    assert np.array_equal(source, [8, 7, 6, 5, 4, 3, 2])
    class SliceProbe(np.ndarray):
        def __array_finalize__(self, obj):
            self.assigned = []

        def __setitem__(self, index, value):
            self.assigned.append(index)
            super().__setitem__(index, value)

    marked = mute_interior(np.array([8, 7, 6, 5, 4, 3, 2]).view(SliceProbe))
    assert any(isinstance(index, slice) and index.indices(len(marked)) == (1, 6, 2)
               for index in getattr(marked, 'assigned', [])), "Assign to one stepped interior slice"
