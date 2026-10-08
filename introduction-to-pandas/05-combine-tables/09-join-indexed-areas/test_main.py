from solution import *

def test_01():
    """Change how to left in attach_areas."""
    a=pd.DataFrame({"area":["S","E","S"],"stall":["A","B","C"]})
    b=pd.DataFrame({"manager":["Jo"]},index=["S"])
    actual = attach_areas(a, b)
    expected = a.set_index("area").join(b,how="left")
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
