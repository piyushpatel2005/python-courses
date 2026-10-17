from solution import *
import matplotlib.pyplot as plt

def test_01_compare_two_lines():
    """Change the second line label from `"Second bed"` to `"Shade"` while keeping both series and the legend."""
    try:
        assert len(ax.lines) == 2
        assert [line.get_label() for line in ax.lines] == ["Sun", "Shade"]
        assert [text.get_text() for text in ax.get_legend().get_texts()] == ["Sun", "Shade"]
        assert list(ax.lines[1].get_ydata()) == [12, 15, 17]
    finally:
        plt.close('all')
