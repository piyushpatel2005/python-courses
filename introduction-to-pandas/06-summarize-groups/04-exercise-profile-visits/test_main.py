from solution import *

def test_01():
    """Complete visit_profile(a) to return a numeric visitors description and type frequencies including missing labels."""
    a=pd.DataFrame({"type":["Food",None,"Food","Book"],"visitors":[3.0,9.0,None,12.0]})
    actual = visit_profile(a)
    expected = (a["visitors"].describe(),a["type"].value_counts(dropna=False))
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
