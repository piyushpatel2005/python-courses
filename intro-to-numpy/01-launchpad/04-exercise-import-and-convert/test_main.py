from solution import make_feed
import numpy as np


def test_make_feed():
    """Convert the supplied readings, including a different feed"""
    for values in ([11, 14, 17], [2, 8], [0.5, -1.5]):
        original = values.copy()
        result = make_feed(values)
        assert isinstance(result, np.ndarray), "Return np.array(values), not the original list or None."
        assert result.ndim == 1, "Keep the incoming list as a one-dimensional array."
        assert np.array_equal(result, values), "Use the values passed to your function rather than fixed sample numbers."
        assert values == original, "Convert the input without changing its list values."
