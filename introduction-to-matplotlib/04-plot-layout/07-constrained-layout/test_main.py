from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [9, 14], [4, 2]), ([2, 4, 6], [25, 30, 28], [8, 3, 6])]:
            fig, axes = roomy_panels(days, a, b)
            assert fig.get_constrained_layout()
            assert [ax.get_title() for ax in axes] == ["Daily boardings", "Average wait"]
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
