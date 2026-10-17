from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [3, 8], [11, 14]), ([2, 4, 6], [7, 2, 9], [31, 24, 41])]:
            fig, axes = garden_and_library(days, a, b)
            assert len(fig.axes) == 2 and axes.shape == (2,)
            assert [len(ax.lines) for ax in axes] == [1, 1]
            assert np.array_equal(axes[0].lines[0].get_xdata(), days)
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
