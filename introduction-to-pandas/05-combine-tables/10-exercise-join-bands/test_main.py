from solution import *

def test_01():
    """Complete attach_bands(a, b) by rejecting a nonunique lookup index with ValueError, then left-joining b after setting band as the left index."""
    a=pd.DataFrame({"band":["C","D","C"],"tables":[2,1,4]})
    b=pd.DataFrame({"fee":[8]},index=["C"])
    actual = attach_bands(a, b)
    expected = a.set_index("band").join(b,how="left")
    if isinstance(expected,tuple):
        assert len(actual)==len(expected), "Return every requested result."
        for got,want in zip(actual,expected):
            pd.testing.assert_series_equal(got,want)
    elif isinstance(expected,pd.DataFrame):
        pd.testing.assert_frame_equal(actual,expected)
    elif isinstance(expected,pd.Series):
        pd.testing.assert_series_equal(actual,expected)
    else:
        assert actual == expected, "Check the result with different input values."
    try:
        attach_bands(a,pd.DataFrame({"fee":[8,9]},index=["C","C"]))
    except ValueError:
        pass
    else:
        assert False, "Reject repeated lookup keys."
