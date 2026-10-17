from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["A", "B"], [3, 9]), (["East", "West", "North"], [12, 2, 7])]:
            fig, ax = garden_bars(names, values)
            assert len(ax.patches) == len(names)
            assert [p.get_height() for p in ax.patches] == values
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_xticklabels()] == names
            assert all(p.get_facecolor()[:3] == to_rgb("seagreen") for p in ax.patches)
            plt.close(fig)
