from solution import *
def test_01_grouped_means_and_title():
    assert ax is fig.axes[0] and ax.get_title() == "Mean visitors by park"
    assert [round(bar.get_height(), 4) for bar in ax.patches] == [15, 35]
    assert [t.get_text() for t in ax.get_xticklabels()] == ["Oak", "Pine"]
