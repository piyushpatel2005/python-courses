from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["A", "B", "C"], [2, 7, 3]), (["D", "E", "F", "G"], [6, 1, 9, 4])]:
            fig, ax = choose_view("compare", names, values)
            assert [p.get_height() for p in ax.patches] == values
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_xticklabels()] == names
            plt.close(fig)
            fig, ax = choose_view("distribution", names, values)
            counts, edges = np.histogram(values, bins=3)
            assert len(ax.patches) == 3
            assert np.array_equal([p.get_height() for p in ax.patches], counts)
            assert np.allclose([p.get_x() for p in ax.patches], edges[:-1])
            plt.close(fig)
