from solution import *

def test_01():
    """Complete align_fees(a, b) by concatenating columns along axis 1."""
    a=pd.DataFrame({"jars":[2,7]},index=["K9","J8"])
    b=pd.DataFrame({"fee":[3,5]},index=["J8","Q7"])
    actual = align_fees(a, b)
    expected = pd.concat([a,b],axis=1)
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
