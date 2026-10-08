from solution import *

def test_01():
    """Change the second calculation in zone_counts from count() to size()."""
    a=pd.DataFrame({"zone":["East","East","West","West"],"amount":[2.0,None,4.0,None]})
    actual = zone_counts(a)
    expected = (a.groupby("zone")["amount"].count(),a.groupby("zone")["amount"].size())
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
