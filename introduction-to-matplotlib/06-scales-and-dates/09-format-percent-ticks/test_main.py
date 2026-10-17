from solution import *
def test_01_fraction_values_percent_display():
    assert ax is fig.axes[0] and list(ax.lines[0].get_ydata()) == [0.20, 0.35, 0.50]
    formatter = ax.yaxis.get_major_formatter()
    assert formatter(0.25) == "25%" and formatter(0.375) == "38%"
