from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [5, 8], [35, 49]), ([3, 5, 7], [21, 18, 25], [44, 33, 51])]:
            fig, axes = label_panels(days, a, b)
            assert [ax.get_title() for ax in axes] == ["(a) Temperature", "(b) Moisture"]
            assert [ax.get_ylabel() for ax in axes] == ["°C", "%"]
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
