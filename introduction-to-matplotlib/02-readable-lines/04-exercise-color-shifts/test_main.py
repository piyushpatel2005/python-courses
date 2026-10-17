from solution import *
import matplotlib.pyplot as plt

def test_01_exercise_color_shifts():
    """Complete `shift_colors(days, morning, afternoon)` to draw both labeled lines in `"tab:blue"` and `"tab:orange"` respectively, add a legend, and return the figure."""
    try:
        for days, morning, afternoon in [([1, 2, 3], [16, 20, 19], [13, 22, 23]), ([4, 9], [5, 13], [17, 8])]:
            chart = shift_colors(days, morning, afternoon)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            axis = chart.axes[0]
            assert len(axis.lines) == 2
            assert [list(line.get_xdata()) for line in axis.lines] == [days, days]
            assert [list(line.get_ydata()) for line in axis.lines] == [morning, afternoon]
            assert [line.get_color() for line in axis.lines] == ["tab:blue", "tab:orange"]
            assert [text.get_text() for text in axis.get_legend().get_texts()] == ["Morning", "Afternoon"]
    finally:
        plt.close('all')
