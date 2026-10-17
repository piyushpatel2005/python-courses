from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_first_figure():
    """Complete `arrival_figure(counts)` to create a figure and axes, plot the supplied counts against positions starting at 1, and return the figure."""
    try:
        for counts in ([5, 9, 7], [12, 4]):
            chart = arrival_figure(counts)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            lines = chart.axes[0].lines
            assert len(lines) == 1
            assert list(lines[0].get_xdata()) == list(range(1, len(counts) + 1))
            assert list(lines[0].get_ydata()) == list(counts)
    finally:
        plt.close('all')
