from solution import *


def test_01_behavior():
    """Fit MinMaxScaler and show that new values can fall outside the fitted range."""
    for train in (np.array([[2., 10.], [4., 20.], [6., 30.]]), np.array([[10., 1.], [20., 3.], [50., 9.]])):
        query = np.vstack([train.min(axis=0)-10., train.max(axis=0)+20.])
        result = range_scale(train.copy(), query.copy())
        assert result is not None, "Return a fitted MinMaxScaler and its query transform."
        scaler, values = result
        assert isinstance(scaler, MinMaxScaler) and scaler.clip is False
        assert tuple(scaler.feature_range) == (0, 1)
        low, high = train.min(axis=0), train.max(axis=0)
        np.testing.assert_array_equal(scaler.data_min_, low)
        np.testing.assert_array_equal(scaler.data_max_, high)
        np.testing.assert_allclose(values, (query-low)/(high-low), rtol=1e-7, atol=1e-8)
        assert (values[0] < 0).all() and (values[1] > 1).all()
        other, _ = range_scale(train.copy(), query*100.)
        np.testing.assert_array_equal(other.data_min_, low)
