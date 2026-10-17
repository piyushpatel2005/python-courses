from solution import *
def test_01_sorted_pairs_and_color():
    assert ax is fig.axes[0] and len(ax.lines) == 1
    assert list(ax.lines[0].get_xdata()) == [1, 2, 3]
    assert list(ax.lines[0].get_ydata()) == [4, 7, 9]
    assert ax.lines[0].get_color() == "purple"
