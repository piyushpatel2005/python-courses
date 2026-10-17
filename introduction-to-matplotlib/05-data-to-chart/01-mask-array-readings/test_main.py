from solution import *
def test_01_strictly_hot_days():
    assert len(fig.axes) == 1 and ax is fig.axes[0]
    assert list(ax.lines[0].get_xdata()) == [3]
    assert list(ax.lines[0].get_ydata()) == [30]
