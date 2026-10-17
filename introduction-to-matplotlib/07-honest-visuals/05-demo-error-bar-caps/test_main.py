from solution import *
import matplotlib.pyplot as plt

def test_01_uncertainty_and_caps():
    """Error-bar intervals follow inputs and have visible caps"""
    import numpy as np
    for days, values, margins in [(['Mon', 'Tue'], [19, 21], [.5, .8]), (['A', 'B', 'C'], [17, 18, 20], [1, .2, .7])]:
        plt.close('all')
        _, chart = plot_estimates(days, values, margins)
        container = chart.containers[0]
        assert list(container.lines[0].get_ydata()) == values
        assert len(container.lines[1]) == 2
        segments = container.lines[2][0].get_segments()
        assert np.allclose([segment[1][1] - segment[0][1] for segment in segments], np.array(margins) * 2)
