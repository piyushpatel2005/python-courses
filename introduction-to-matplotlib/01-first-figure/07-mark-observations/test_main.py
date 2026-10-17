from solution import *
import matplotlib.pyplot as plt

def test_01_mark_observations():
    """Change the marker from a circle (`"o"`) to a square (`"s"`)."""
    try:
        assert len(ax.lines) == 1
        assert ax.lines[0].get_marker() == "s"
        assert list(ax.lines[0].get_ydata()) == [2, 5, 4]
    finally:
        plt.close('all')
