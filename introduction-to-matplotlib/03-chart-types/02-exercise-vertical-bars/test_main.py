from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["A", "B"], [4, 11]), (["North", "South", "West"], [19, 3, 8])]:
            fig, ax = library_bars(names, values)
            assert len(ax.patches) == len(names)
            assert not ax.lines
            assert [p.get_height() for p in ax.patches] == values
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_xticklabels()] == names
            assert ax.get_ylabel() == "Visits"
            plt.close(fig)
