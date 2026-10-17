from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [4, 7], [12, 9]), ([2, 4, 6], [1, 5, 2], [15, 8, 11])]:
            fig, axes = two_signals(days, a, b)
            assert len(fig.axes) == 2 and axes.shape == (2,)
            assert [ax.get_title() for ax in axes] == ["Library visits", "Bus boardings"]
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
