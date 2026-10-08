from solution import *

def test_01_hold_settings():
    for settings, frames in ((np.array([1, 4, 7]), 2), (np.array([9, 3]), 3)):
        assert np.array_equal(hold_settings(settings, frames), np.repeat(settings, frames))

def test_02_cycle_settings():
    for settings, cycles in ((np.array([1, 4, 7]), 2), (np.array([9, 3]), 3)):
        assert np.array_equal(cycle_settings(settings, cycles), np.tile(settings, cycles))
