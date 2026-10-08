from solution import *
import numpy as np

def test_sample_times():
    """Stepped times exclude the stop"""
    assert sample_times(1, 8, 2).tolist() == [1, 3, 5, 7]
    assert sample_times(0, 5, 2).tolist() == [0, 2, 4]

def test_calibration_marks():
    """Calibration marks include both ends"""
    assert np.allclose(calibration_marks(0, 2, 3), [0, 1, 2])
    assert np.allclose(calibration_marks(1, 3, 5), [1, 1.5, 2, 2.5, 3])
