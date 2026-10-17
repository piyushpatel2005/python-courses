from solution import *
import matplotlib.pyplot as plt

def test_01_point_to_the_peak():
    """Change the annotation text from `"Noon"` to `"Wind peak"` while keeping its arrow at hour 12, reading 9."""
    try:
        assert len(ax.lines) == 1
        assert len(ax.texts) == 1
        note = ax.texts[0]
        assert note.get_text() == "Wind peak" and tuple(note.xy) == (12, 9)
        assert note.arrow_patch is not None
    finally:
        plt.close('all')
