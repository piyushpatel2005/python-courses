from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_grid_counts():
    """Complete `guided_counts(hours, counts)` to plot both inputs, turn on only horizontal y grid lines, and return the figure."""
    try:
        for hours, counts in [([9, 11, 13], [14, 20, 18]), ([8, 15], [9, 28])]:
            chart = guided_counts(hours, counts)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 1
            assert list(axis.lines[0].get_xdata()) == hours
            assert list(axis.lines[0].get_ydata()) == counts
            assert any(line.get_visible() for line in axis.get_ygridlines())
            assert not any(line.get_visible() for line in axis.get_xgridlines())
    finally:
        plt.close('all')
