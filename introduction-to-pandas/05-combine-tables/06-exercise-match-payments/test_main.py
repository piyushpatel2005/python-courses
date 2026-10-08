from solution import *

def test_01():
    """Complete match_payments(a, b) with a left merge on ticket."""
    a=pd.DataFrame({"ticket":["Q2","Q3","Q4"],"seats":[1,4,2]})
    b=pd.DataFrame({"ticket":["Q4","Q2"],"paid":[True,False]})
    actual = match_payments(a, b)
    expected = a.merge(b,on="ticket",how="left")
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
