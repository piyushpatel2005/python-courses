from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, values in [([1, 2], [4, 8]), ([3, 5, 7], [12, 6, 14])]:
            fig, ax = garden_canvas(days, values)
            assert np.allclose(fig.get_size_inches(), (7, 4))
            assert len(fig.axes) == 1 and len(ax.lines) == 1
            assert np.array_equal(ax.lines[0].get_xdata(), days)
            assert np.array_equal(ax.lines[0].get_ydata(), values)
            plt.close(fig)
