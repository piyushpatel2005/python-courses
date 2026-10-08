from solution import *

def test_01():
    """Complete zone_metrics(a) to return grouped amount mean, sum, count, and size, in that order."""
    a=pd.DataFrame({"zone":["N","N","N","S"],"amount":[3.0,5.0,None,1.0]})
    actual = zone_metrics(a)
    expected = (a.groupby("zone")["amount"].mean(),a.groupby("zone")["amount"].sum(),a.groupby("zone")["amount"].count(),a.groupby("zone")["amount"].size())
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
