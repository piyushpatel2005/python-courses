from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for values in ([11, 13, 18, 23], [10, 14, 15, 16, 20, 24, 25]):
            fig, ax = temperature_hist(values)
            bars = ax.patches
            assert len(bars) == 3
            assert np.allclose([p.get_x() for p in bars], [10, 15, 20])
            assert np.allclose([p.get_width() for p in bars], [5, 5, 5])
            assert np.array_equal([p.get_height() for p in bars], np.histogram(values, bins=[10, 15, 20, 25])[0])
            plt.close(fig)
