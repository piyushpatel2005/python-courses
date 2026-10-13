from solution import *

def test_01_behavior():
    """Inspect residual patterns"""
    for a, p in (([14., 19., 27., 39., 54.], [10., 20., 30., 40., 50.]), ([7., 3., 12.], [5., 6., 10.])):
        a, p = np.array(a), np.array(p)
        got = residual_plot(a, p)
        assert got is not None, "Return figure and axes."
        fig, ax = got
        try:
            assert len(ax.collections) == 1
            assert np.allclose(ax.collections[0].get_offsets(), np.column_stack([p, a-p])), "Pair predictions with observed-minus-predicted residuals."
            assert any(np.allclose(line.get_ydata(), 0) for line in ax.lines), "Include a zero reference."
            assert ax.get_xlabel() and ax.get_ylabel()
        finally:
            plt.close(fig)

