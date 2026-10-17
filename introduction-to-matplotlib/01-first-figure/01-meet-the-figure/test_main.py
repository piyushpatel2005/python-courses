from solution import *
import matplotlib.pyplot as plt

def test_01_meet_the_figure():
    """Change the last soil reading from 12 to 16."""
    try:
        assert isinstance(fig, plt.Figure)
        assert ax in fig.axes and len(ax.lines) == 1
        assert list(ax.lines[0].get_ydata()) == [8, 11, 16]
    finally:
        plt.close('all')
