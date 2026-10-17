from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_ticks_for_hours():
    """Complete `hour_window(hours, counts)` to plot the inputs, set x ticks to `hours`, set x limits to one hour below the minimum and above the maximum, and return the figure."""
    try:
        for hours, counts in [([9, 12, 16], [11, 18, 7]), ([7, 10], [4, 14])]:
            chart = hour_window(hours, counts)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 1
            assert list(axis.lines[0].get_xdata()) == hours
            assert list(axis.lines[0].get_ydata()) == counts
            assert list(axis.get_xticks()) == hours
            assert tuple(axis.get_xlim()) == (min(hours) - 1, max(hours) + 1)
    finally:
        plt.close('all')
