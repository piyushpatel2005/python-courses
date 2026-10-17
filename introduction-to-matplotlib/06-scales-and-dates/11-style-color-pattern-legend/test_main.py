from solution import *
def test_01_distinct_style_and_legend():
    assert ax is fig.axes[0] and len(ax.lines) == 2
    assert ax.lines[0].get_linestyle() == "-" and ax.lines[1].get_linestyle() == "--"
    assert ax.lines[0].get_color() != ax.lines[1].get_color()
    assert [t.get_text() for t in ax.get_legend().get_texts()] == ["North pickup", "South pickup"]
    assert fig.get_constrained_layout()
