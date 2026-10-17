from solution import *
def test_01_series_coordinates_and_marker():
    assert ax is fig.axes[0] and len(ax.lines) == 1
    line = ax.lines[0]
    assert list(line.get_xdata()) == ["Mon", "Tue", "Wed"]
    assert list(line.get_ydata()) == [54, 58, 63]
    assert line.get_marker() == "s"
