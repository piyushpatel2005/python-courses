from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_title_a_branch():
    """Complete `branch_figure(branch, days, visits)` to title the plotted figure `"{branch} visitors"` and return it."""
    try:
        for branch, days, visits in [("North", [1, 2, 3], [20, 27, 24]), ("Creek", [2, 5], [7, 19])]:
            chart = branch_figure(branch, days, visits)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert axis.get_title() == f"{branch} visitors"
            assert axis.get_xlabel() == "Day" and axis.get_ylabel() == "Visitors"
            assert len(axis.lines) == 1
            assert list(axis.lines[0].get_xdata()) == days
            assert list(axis.lines[0].get_ydata()) == visits
    finally:
        plt.close('all')
