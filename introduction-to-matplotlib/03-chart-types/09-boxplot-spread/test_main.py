from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for values in ([1, 2, 3, 4, 9], [5, 7, 8, 11, 13, 30]):
            fig, ax = soil_boxplot(values)
            assert len(ax.lines) >= 7
            assert np.allclose(ax.lines[5].get_ydata(), np.median(values))
            assert np.allclose(ax.lines[6].get_ydata(), np.mean(values))
            assert ax.get_ylabel() == "Soil moisture (%)"
            plt.close(fig)
