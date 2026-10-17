from solution import *
import matplotlib.pyplot as plt

def test_01_choose_x_and_y():
    """Change the last hour from 12 to 14 while keeping the three soil readings."""
    try:
        assert list(ax.lines[0].get_xdata()) == [8, 10, 14]
        assert list(ax.lines[0].get_ydata()) == [19, 23, 21]
    finally:
        plt.close('all')
