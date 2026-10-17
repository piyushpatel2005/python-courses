from solution import *
import matplotlib.colors as colors

def test_01_two_distinct_series_on_changed_data():
    figure, axis = plot_school_routes([3, 5, 8], [5, 17, 6], [22, 9, 14])
    assert axis in figure.axes and len(axis.lines) == 2
    assert [list(line.get_xdata()) for line in axis.lines] == [[3, 5, 8], [3, 5, 8]]
    assert [list(line.get_ydata()) for line in axis.lines] == [[5, 17, 6], [22, 9, 14]]
    assert axis.lines[0].get_color() != axis.lines[1].get_color()
    assert axis.lines[0].get_linestyle() != axis.lines[1].get_linestyle()

def test_02_legend_names_both_series():
    _, axis = plot_school_routes([1], [3], [4])
    assert axis.get_legend() is not None
    assert [text.get_text() for text in axis.get_legend().get_texts()] == ["Walkers", "Riders"]

def test_03_temporary_style_and_layout():
    figure, axis = plot_school_routes([1, 2], [4, 8], [3, 9])
    assert figure.get_constrained_layout()
    assert colors.to_rgba(axis.get_facecolor()) != colors.to_rgba("white")
