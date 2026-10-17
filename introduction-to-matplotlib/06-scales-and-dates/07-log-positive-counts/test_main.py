from solution import *
def test_01_log_and_visible_positive_range():
    assert ax is fig.axes[0] and ax.get_yscale() == "log"
    assert ax.get_ylim() == (1, 1000)
    assert list(ax.lines[0].get_ydata()) == [1, 10, 100, 1000]
