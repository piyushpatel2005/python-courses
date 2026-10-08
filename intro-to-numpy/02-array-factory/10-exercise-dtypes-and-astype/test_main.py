from solution import *
import numpy as np

def test_typed_feeds():
    """Conversions retain values across three dtype families"""
    for values in ([0, 2, -3], [4, 0]):
        flags, labels, complex_values = typed_feeds(values)
        assert flags.dtype.kind == 'b' and flags.tolist() == [bool(x) for x in values]
        assert labels.dtype.kind == 'U' and labels.tolist() == [str(x) for x in values]
        assert complex_values.dtype.kind == 'c' and complex_values.tolist() == [complex(x) for x in values]
