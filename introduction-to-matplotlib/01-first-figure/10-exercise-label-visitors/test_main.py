from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_label_visitors():
    """Complete `labeled_visits(days, visits)` to plot the paired inputs, label the x-axis `"Day"` and the y-axis `"Visitors"`, and return the figure."""
    try:
        for days, visits in [([1, 2, 3], [18, 23, 21]), ([4, 7], [11, 33])]:
            chart = labeled_visits(days, visits)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert axis.get_xlabel() == "Day" and axis.get_ylabel() == "Visitors"
            assert len(axis.lines) == 1
            assert list(axis.lines[0].get_xdata()) == days
            assert list(axis.lines[0].get_ydata()) == visits
    finally:
        plt.close('all')
