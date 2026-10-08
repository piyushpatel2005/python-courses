from solution import *

def test_01():
    """Complete category_report(a) with named revenue (amount sum) and entries (amount size) by category."""
    a=pd.DataFrame({"category":["Plant","Plant","Book","Plant"],"amount":[4.0,None,7.0,3.0]})
    actual = category_report(a)
    expected = a.groupby("category").agg(revenue=("amount","sum"),entries=("amount","size"))
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
