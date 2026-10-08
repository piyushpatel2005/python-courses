from solution import *

def test_01():
    """Change how="inner" to how="left" in attach_vendors."""
    a=pd.DataFrame({"stall":["C4","X0","B1"],"tables":[1,3,2]})
    b=pd.DataFrame({"stall":["B1","C4"],"vendor":["Zed","Ivy"]})
    actual = attach_vendors(a, b)
    expected = a.merge(b,on="stall",how="left")
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
