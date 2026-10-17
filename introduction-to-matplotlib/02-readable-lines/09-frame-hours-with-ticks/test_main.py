from solution import *
import matplotlib.pyplot as plt

def test_01_frame_hours_with_ticks():
    """Extend the right x limit from 13 to 14; keep ticks at the sampled hours."""
    try:
        assert list(ax.get_xticks()) == [8, 10, 12]
        assert tuple(ax.get_xlim()) == (7.0, 14.0)
        assert list(ax.lines[0].get_xdata()) == hours
    finally:
        plt.close('all')
