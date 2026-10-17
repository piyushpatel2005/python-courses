from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_coordinate_pairs():
    """Complete `reading_room(hours, counts)` so it plots the paired inputs and returns its figure."""
    try:
        for hours, counts in [([9, 11, 15], [4, 10, 6]), ([8, 12], [3, 13])]:
            chart = reading_room(hours, counts)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            assert len(chart.axes[0].lines) == 1
            assert list(chart.axes[0].lines[0].get_xdata()) == hours
            assert list(chart.axes[0].lines[0].get_ydata()) == counts
    finally:
        plt.close('all')
