from solution import *
import numpy as np

def test_transform():
    """Compute sine and safe logarithms elementwise"""
    for angles, intensities in [([0.0, np.pi / 2], [1.0, np.e]), ([np.pi, -np.pi / 2], [np.e ** 2, 2.0])]:
        wave, levels = transform(np.array(angles), np.array(intensities))
        assert np.allclose(wave, np.sin(angles))
        assert np.allclose(levels, np.log(intensities))
        assert np.all(np.isfinite(levels))
