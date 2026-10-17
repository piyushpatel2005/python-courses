from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["A", "B", "C"], [3, 9, 4]), (["North", "East", "South", "West"], [12, 2, 8, 5])]:
            fig, ax = neighborhood_view("compare", names, values)
            assert [p.get_width() for p in ax.patches] == values
            assert not ax.lines
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_yticklabels()] == names
            plt.close(fig)
            fig, ax = neighborhood_view("distribution", names, values)
            counts, edges = np.histogram(values, bins=3)
            assert len(ax.patches) == 3
            assert not ax.lines
            assert np.array_equal([p.get_height() for p in ax.patches], counts)
            assert np.allclose([p.get_x() for p in ax.patches], edges[:-1])
            plt.close(fig)
