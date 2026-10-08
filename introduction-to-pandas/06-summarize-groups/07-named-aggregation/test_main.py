from solution import *

def test_01():
    """Change average=("total", "sum") to use mean."""
    a=pd.DataFrame({"vendor":["Fern","Fern","Ash"],"total":[2.0,8.0,None]})
    actual = vendor_report(a)
    expected = a.groupby("vendor").agg(average=("total","mean"),orders=("total","size"))
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
