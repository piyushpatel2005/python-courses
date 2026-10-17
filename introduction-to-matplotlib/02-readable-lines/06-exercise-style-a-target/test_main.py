from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_style_a_target():
    """Complete `attendance_target(days, actual, target)` to plot actual as solid and target as dotted, include a legend, and return the figure."""
    try:
        for days, actual, target in [([1, 2, 3], [18, 21, 16], [20, 20, 20]), ([5, 8], [15, 32], [25, 25])]:
            chart = attendance_target(days, actual, target)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 2
            assert [list(line.get_xdata()) for line in axis.lines] == [days, days]
            assert [list(line.get_ydata()) for line in axis.lines] == [actual, target]
            assert [line.get_linestyle() for line in axis.lines] == ["-", ":"]
            assert [text.get_text() for text in axis.get_legend().get_texts()] == ["Actual", "Target"]
    finally:
        plt.close('all')
