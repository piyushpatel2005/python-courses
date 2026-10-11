from solution import *
import numpy as np

def test_gather():
    """Gather positions in the requested order"""
    assert np.array_equal(choose_pair(np.array([4, 9, 6, 2])), [2, 9])
    assert np.array_equal(choose_pair(np.array([7, 3, 8, 5, 1])), [1, 3])
    class IndexProbe(np.ndarray):
        def __getitem__(self, index):
            if isinstance(index, list):
                self.used_index_list = True
            return super().__getitem__(index)

    readings = np.array([11, 22, 33, 44, 55, 66]).view(IndexProbe)
    readings.used_index_list = False
    pair = choose_pair(readings)
    assert np.array_equal(pair, [66, 22])
    assert readings.used_index_list, "Gather with a list of indices, not a prebuilt answer"
    assert not np.shares_memory(pair, readings)
