from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [11, 14], [4, 8]), ([3, 5, 7], [35, 29, 41], [7, 5, 3])]:
            fig, axes = shared_timeline(days, a, b)
            assert len(fig.axes) == 2 and axes[0].get_shared_x_axes().joined(axes[0], axes[1])
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            axes[0].set_xlim(2, 8)
            assert np.allclose(axes[1].get_xlim(), (2, 8))
            plt.close(fig)
