from solution import *

def test_01():
    """Complete stack_visits(a, b) with row concatenation and a fresh index."""
    a=pd.DataFrame({"stall":["Birch"],"visits":[4]},index=[91])
    b=pd.DataFrame({"stall":["Yew","Beech"],"visits":[2,8]},index=[61,74])
    actual = stack_visits(a, b)
    expected = pd.concat([a,b],ignore_index=True)
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
