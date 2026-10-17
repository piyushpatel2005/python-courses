from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, a, b in [([1, 2], [3, 7], [12, 9]), ([2, 4, 6], [6, 2, 8], [20, 31, 25])]:
            fig, axes = community_panels(days, a, b)
            assert [ax.get_title() for ax in axes] == ["(a) Garden", "(b) Library"]
            assert [ax.get_ylabel() for ax in axes] == ["Beds watered", "Visits"]
            assert np.array_equal(axes[0].lines[0].get_ydata(), a)
            assert np.array_equal(axes[1].lines[0].get_ydata(), b)
            plt.close(fig)
