from solution import *
import matplotlib.pyplot as plt
import numpy as np

def test_01_numpy_readings():
    """Change the final wind reading from 7 to 10 in the NumPy array."""
    try:
        assert isinstance(hours, np.ndarray) and isinstance(wind, np.ndarray)
        assert list(ax.lines[0].get_xdata()) == [7, 9, 11]
        assert list(ax.lines[0].get_ydata()) == [3, 6, 10]
    finally:
        plt.close('all')
