from solution import *

def test_01():
    """Complete shift_totals(a) by grouping on market and shift and summing revenue."""
    a=pd.DataFrame({"market":["Square","Square","Square","Garden"],"shift":["AM","PM","AM","PM"],"revenue":[7,3,8,2]})
    actual = shift_totals(a)
    expected = a.groupby(["market","shift"])["revenue"].sum()
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
