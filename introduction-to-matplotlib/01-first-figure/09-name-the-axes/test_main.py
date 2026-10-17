from solution import *
import matplotlib.pyplot as plt

def test_01_name_the_axes():
    """Change the vertical label from `"Reading"` to `"Humidity (%)"`."""
    try:
        assert ax.get_xlabel() == "Hour" and ax.get_ylabel() == "Humidity (%)"
        assert len(ax.lines) == 1
    finally:
        plt.close('all')
