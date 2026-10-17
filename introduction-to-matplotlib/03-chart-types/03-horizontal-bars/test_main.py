from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for names, values in [(["Long Road", "Hill"], [7, 12]), (["Lake", "Park", "Depot"], [1, 8, 4])]:
            fig, ax = route_ranking(names, values)
            assert [p.get_width() for p in ax.patches] == values
            fig.canvas.draw()
            assert [t.get_text() for t in ax.get_yticklabels()] == names
            assert ax.get_xlabel() == "Riders"
            plt.close(fig)
