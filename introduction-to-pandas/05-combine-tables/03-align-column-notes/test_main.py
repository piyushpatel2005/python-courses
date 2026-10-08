from solution import *

def test_01():
    """Change axis=0 to axis=1 in align_notes."""
    a=pd.DataFrame({"visits":[5,6]},index=["Fri","Sat"])
    b=pd.DataFrame({"weather":["sun","wind"]},index=["Sat","Sun"])
    actual = align_notes(a, b)
    expected = pd.concat([a,b],axis=1)
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
