from solution import *
def test_01_rotated_tick_labels():
    assert ax is fig.axes[0] and len(ax.lines) == 1
    assert ax.get_xticklabels()
    assert all(round(label.get_rotation()) == 45 for label in ax.get_xticklabels())
