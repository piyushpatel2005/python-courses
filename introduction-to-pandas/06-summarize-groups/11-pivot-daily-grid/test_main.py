from solution import *

def test_01():
    """Add fill_value=0 to daily_grid."""
    a=pd.DataFrame({"zone":["E","E","W","E"],"day":["Mon","Tue","Tue","Mon"],"amount":[2,3,4,5]})
    actual = daily_grid(a)
    expected = pd.pivot_table(a,index="zone",columns="day",values="amount",aggfunc="sum",fill_value=0)
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
