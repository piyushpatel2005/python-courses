from solution import *
import matplotlib.pyplot as plt

def test_01_vary_line_styles():
    """Change the planned line style from solid (`"-"`) to dashed (`"--"`)."""
    try:
        assert len(ax.lines) == 2
        assert [line.get_linestyle() for line in ax.lines] == ["-", "--"]
        assert [line.get_label() for line in ax.lines] == ["Observed", "Planned"]
    finally:
        plt.close('all')
