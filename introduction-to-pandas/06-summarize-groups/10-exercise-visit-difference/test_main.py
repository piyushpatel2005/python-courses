from solution import *

def test_01():
    """Complete visit_difference(a) using groupby(...).transform("mean") to subtract each category baseline."""
    a=pd.DataFrame({"category":["Book","Food","Book","Food"],"visitors":[3.0,10.0,9.0,18.0]},index=[8,2,6,4])
    actual = visit_difference(a)
    expected = a["visitors"]-a.groupby("category")["visitors"].transform("mean")
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
