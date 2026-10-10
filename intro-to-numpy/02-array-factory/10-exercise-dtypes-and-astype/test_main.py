from solution import *
import numpy as np

def _check_conversion(index, dtype, kind):
    for readings in ([0, 2, -3], [4, 0], [0.0, -1.5, 2.25]):
        original = list(readings)
        actual = typed_feeds(readings)[index]
        assert isinstance(actual, np.ndarray), "Return a converted NumPy array"
        assert actual.dtype.kind == kind
        assert np.array_equal(actual, np.array(readings).astype(dtype))
        assert readings == original, "Keep the supplied readings unchanged"

def test_boolean_flags():
    """Convert zeros and nonzeros to Boolean flags"""
    _check_conversion(0, bool, 'b')

def test_text_labels():
    """Convert each reading to text"""
    _check_conversion(1, str, 'U')

def test_complex_values():
    """Convert each reading to a complex value"""
    _check_conversion(2, complex, 'c')
