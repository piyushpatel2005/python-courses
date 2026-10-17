from solution import *
import matplotlib.pyplot as plt

def test_01_title_the_story():
    """Change the title from `"Garden report"` to `"Garden soil moisture"`."""
    try:
        assert ax.get_title() == "Garden soil moisture"
        assert ax.get_xlabel() == "Day" and ax.get_ylabel() == "Moisture (%)"
        assert len(ax.lines) == 1
    finally:
        plt.close('all')
