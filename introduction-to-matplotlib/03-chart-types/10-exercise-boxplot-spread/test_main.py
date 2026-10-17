from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for values in ([1, 3, 4, 8, 10], [12, 13, 17, 21, 29, 42]):
            fig, ax = trip_boxplot(values)
            assert len(ax.patches) == 1
            assert len(ax.lines) == 6
            assert np.allclose(ax.lines[4].get_ydata(), np.median(values))
            assert ax.get_ylabel() == "Trip (minutes)"
            plt.close(fig)
