from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [3, 8], [2, 7]), ([2, 4, 6], [4, 9, 5], [0, 6, 1])]:
            fig, axes = garden_pair(days, a, b)
            assert fig.get_constrained_layout() and len(fig.axes) == 2
            assert [len(ax.lines) for ax in axes] == [1, 1]
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
