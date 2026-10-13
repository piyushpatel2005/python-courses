from solution import *

def test_01_behavior():
    """Exercise: read residuals and absolute error"""
    for actual, predicted in (([4., 8., 12.], [8., 4., 12.]), ([2., 6.], [1., 10.])):
        a, p = np.array(actual), np.array(predicted)
        got = error_report(a, p)
        assert got is not None, "Return residuals and MAE."
        residuals, mae = got
        assert np.array_equal(residuals, a-p), "Residual sign is observed minus predicted."
        assert np.isclose(mae, np.abs(a-p).mean()), "Take absolute errors before averaging."

