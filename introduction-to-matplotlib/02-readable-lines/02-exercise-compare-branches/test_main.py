from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_compare_branches():
    """Complete `compare_branches(days, east, west)` to plot both sequences with labels `"East"` and `"West"`, show a legend, and return the figure."""
    try:
        for days, east, west in [([1, 2, 3], [8, 11, 14], [6, 10, 12]), ([2, 5], [21, 8], [10, 24])]:
            chart = compare_branches(days, east, west)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 2
            assert [list(line.get_xdata()) for line in axis.lines] == [days, days]
            assert [list(line.get_ydata()) for line in axis.lines] == [east, west]
            assert [line.get_label() for line in axis.lines] == ["East", "West"]
            assert axis.get_legend() is not None
            assert [text.get_text() for text in axis.get_legend().get_texts()] == ["East", "West"]
    finally:
        plt.close('all')
