from solution import *

def test_01_behavior():
    """Measure squared-error sensitivity"""
    for a, p in (([0., 0., 0., 0.], [0., 0., 0., 6.]), ([2., 5.], [3., 2.]), ([7., 9.], [7., 9.])):
        a, p = np.array(a), np.array(p)
        got = rmse_value(a, p)
        assert got is not None, "Return RMSE."
        assert np.isclose(got, np.sqrt(np.mean((a-p)**2))), "Average squares, then take the root."

