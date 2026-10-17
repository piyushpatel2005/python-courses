from solution import *
def test_01_bounds_and_units():
    assert ax is fig.axes[0] and list(ax.lines[0].get_ydata()) == [3, 12, 18, 15]
    assert ax.get_ylim() == (0, 24)
    assert ax.get_ylabel() == "Occupancy (people)"
