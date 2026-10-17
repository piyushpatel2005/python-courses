from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, visits, riders, waits in [([1, 2], [8, 5], [15, 17], [2, 3, 6, 8]), ([2, 4, 6], [11, 19, 13], [21, 28, 23], [1, 4, 5, 7, 9])]:
            fig, axes = neighborhood_report(days, visits, riders, waits)
            assert len(fig.axes) == 3 and fig._suptitle.get_text() == "Neighborhood pulse"
            assert np.array_equal(axes[0].lines[0].get_ydata(), visits)
            assert [p.get_height() for p in axes[1].patches] == riders
            assert np.array_equal([p.get_height() for p in axes[2].patches], np.histogram(waits, bins=3)[0])
            plt.close(fig)
