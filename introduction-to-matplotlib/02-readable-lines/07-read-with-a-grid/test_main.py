from solution import *
import matplotlib.pyplot as plt

def test_01_read_with_a_grid():
    """Change the grid call so horizontal y guides are visible."""
    try:
        assert len(ax.lines) == 1
        assert any(line.get_visible() for line in ax.get_ygridlines())
        assert not any(line.get_visible() for line in ax.get_xgridlines())
    finally:
        plt.close('all')
