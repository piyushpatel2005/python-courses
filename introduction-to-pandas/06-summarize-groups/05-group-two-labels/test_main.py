from solution import *

def test_01():
    """Change the grouping key in daily_gifts to ["zone", "day"]."""
    a=pd.DataFrame({"zone":["East","East","East","West"],"day":["Mon","Tue","Mon","Mon"],"amount":[2,4,3,9]})
    actual = daily_gifts(a)
    expected = a.groupby(["zone","day"])["amount"].sum()
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
