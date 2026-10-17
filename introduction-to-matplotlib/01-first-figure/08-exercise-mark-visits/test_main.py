from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_mark_visits():
    """Complete `marked_visits(hours, visits)` to plot the paired inputs with diamond markers and return the figure."""
    try:
        for hours, visits in [([10, 12, 14], [8, 15, 11]), ([9, 13], [2, 7])]:
            chart = marked_visits(hours, visits)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            assert len(chart.axes[0].lines) == 1
            line = chart.axes[0].lines[0]
            assert list(line.get_xdata()) == hours and list(line.get_ydata()) == visits
            assert line.get_marker() == "D" and line.get_linestyle() != "None"
    finally:
        plt.close('all')
