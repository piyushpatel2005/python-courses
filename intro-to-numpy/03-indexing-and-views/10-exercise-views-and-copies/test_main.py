from solution import *
import numpy as np

_VALUES = ([2, 4, 6, 8], [9, 11, 13, 15])

def test_middle_view():
    """The middle window shares its source storage"""
    for values in _VALUES:
        source = np.array(values)
        view, _ = calibrate(source)
        assert isinstance(view, np.ndarray) and view.shape == (2,)
        assert np.shares_memory(source, view)
        assert np.array_equal(view, source[1:3])
        view[1] = 123
        assert source[2] == 123

def test_independent_snapshot():
    """The snapshot has its own middle-two-item storage"""
    for values in _VALUES:
        source = np.array(values)
        _, snapshot = calibrate(source)
        assert isinstance(snapshot, np.ndarray) and snapshot.shape == (2,)
        assert not np.shares_memory(source, snapshot)
        assert snapshot[1] == values[2]
        assert snapshot[0] in (values[1], -5), "Take the snapshot before editing the view"
        snapshot[1] = 123
        assert source[2] == values[2]

def test_edit_view():
    """Editing the view changes only the source's second item"""
    for values in _VALUES:
        source = np.array(values)
        view, _ = calibrate(source)
        assert view.shape == (2,) and view[0] == 50
        assert np.array_equal(source, [values[0], 50, values[2], values[3]])

def test_edit_snapshot():
    """Editing the snapshot leaves the source alone"""
    for values in _VALUES:
        source = np.array(values)
        _, snapshot = calibrate(source)
        assert np.array_equal(snapshot, [-5, values[2]])
        assert source[1] != -5
