from solution import *

def test_01():
    """Change dropna=True to dropna=False in profile_sales."""
    a=pd.DataFrame({"category":["Repair",None,"Repair","Plant",None],"amount":[2.0,None,6.0,10.0,14.0]})
    actual = profile_sales(a)
    expected = (a["amount"].describe(),a["category"].value_counts(dropna=False))
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
