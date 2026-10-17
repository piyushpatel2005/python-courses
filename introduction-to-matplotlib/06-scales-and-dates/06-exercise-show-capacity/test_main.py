from solution import *
def test_01_dynamic_counts_and_capacity():
    figure, axis = plot_rack_use([7, 11, 16], [2, 19, 8], 25)
    assert axis in figure.axes and len(axis.lines) == 1
    assert list(axis.lines[0].get_xdata()) == [7, 11, 16]
    assert list(axis.lines[0].get_ydata()) == [2, 19, 8]
    assert axis.get_ylim() == (0, 25)
    _, changed = plot_rack_use([6, 8], [4, 8], 40)
    assert changed.get_ylim() == (0, 40)

def test_02_unit_labels():
    _, axis = plot_rack_use([8], [2], 10)
    assert axis.get_xlabel() == "Hour of day" and axis.get_ylabel() == "Bikes (count)"
