from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for x, y, sizes in [([1, 3], [7, 2], [50, 80]), ([4, 5, 8], [11, 6, 12], [20, 90, 150])]:
            fig, ax = reading_bubbles(x, y, sizes)
            assert len(ax.collections) == 1
            assert not ax.lines
            dots = ax.collections[0]
            assert np.array_equal(np.asarray(dots.get_offsets()), np.column_stack((x, y)))
            assert np.array_equal(dots.get_sizes(), sizes)
            assert ax.get_xlabel() == "Open hours"
            plt.close(fig)
