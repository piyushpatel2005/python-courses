from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for values, edges in [([1, 2, 7, 8], [0, 5, 10]), ([2, 3, 4, 9, 12, 15], [0, 4, 8, 12, 16])]:
            fig, ax = wait_hist(values, edges)
            bars = ax.patches
            assert len(bars) == len(edges) - 1
            assert not ax.lines
            assert np.allclose([p.get_x() for p in bars], edges[:-1])
            assert np.allclose([p.get_width() for p in bars], np.diff(edges))
            assert np.array_equal([p.get_height() for p in bars], np.histogram(values, bins=edges)[0])
            assert ax.get_xlabel() == "Wait (minutes)"
            plt.close(fig)
