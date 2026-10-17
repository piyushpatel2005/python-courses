from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["A", "B"], [5, 14]), (["West End", "Depot", "Market"], [9, 3, 17])]:
            fig, ax = transit_ranking(names, values)
            assert len(ax.patches) == len(names)
            assert not ax.lines
            assert [p.get_width() for p in ax.patches] == values
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_yticklabels()] == names
            assert ax.get_xlabel() == "Boardings"
            plt.close(fig)
