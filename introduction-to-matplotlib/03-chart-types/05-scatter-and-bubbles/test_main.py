from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for x, y, sizes in [([2, 5], [8, 3], [30, 90]), ([1, 4, 7], [6, 2, 9], [70, 40, 130])]:
            fig, ax = garden_bubbles(x, y, sizes)
            assert len(ax.collections) == 1
            dots = ax.collections[0]
            assert np.array_equal(np.asarray(dots.get_offsets()), np.column_stack((x, y)))
            assert np.array_equal(dots.get_sizes(), sizes)
            assert np.isclose(dots.get_alpha(), 0.7)
            plt.close(fig)
