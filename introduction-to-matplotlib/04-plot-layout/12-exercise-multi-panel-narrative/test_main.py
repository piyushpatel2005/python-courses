from solution import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def test_chart_semantics_with_new_data():
    for days, garden, library, transit in [([1, 2], [16, 18], [32, 25], [48, 61]), ([2, 4, 6], [21, 17, 23], [42, 38, 49], [73, 66, 81])]:
            fig, axes = weekly_story(days, garden, library, transit)
            assert len(fig.axes) == 3 and fig.get_constrained_layout()
            assert fig._suptitle.get_text() == "Neighborhood week"
            assert [ax.get_title() for ax in axes] == ["Garden temperature", "Library visits", "Transit boardings"]
            assert np.array_equal(axes[0].lines[0].get_ydata(), garden)
            assert np.array_equal(axes[1].lines[0].get_ydata(), library)
            assert [p.get_height() for p in axes[2].patches] == transit
            plt.close(fig)
