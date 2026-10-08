from solution import *

def test_01():
    """Change the operation in zone_baseline from sum to mean."""
    a=pd.DataFrame({"zone":["A","B","A","B"],"amount":[2.0,6.0,10.0,None]},index=[7,4,9,3])
    actual = zone_baseline(a)
    expected = a.groupby("zone")["amount"].transform("mean")
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
