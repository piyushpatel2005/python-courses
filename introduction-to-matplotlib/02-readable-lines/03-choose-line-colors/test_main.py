from solution import *
import matplotlib.pyplot as plt

def test_01_choose_line_colors():
    """Change the second rain-gauge line from `"tab:blue"` to `"tab:orange"`."""
    try:
        assert len(ax.lines) == 2
        assert [line.get_color() for line in ax.lines] == ["tab:blue", "tab:orange"]
        assert [line.get_label() for line in ax.lines] == ["North gauge", "South gauge"]
    finally:
        plt.close('all')
