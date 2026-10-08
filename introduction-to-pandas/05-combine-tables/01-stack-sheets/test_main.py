from solution import *

def test_01():
    """Change ignore_index to True in stack_sheets."""
    a=pd.DataFrame({"stall":["Oak"],"crates":[7]},index=[12])
    b=pd.DataFrame({"stall":["Pine","Elm"],"crates":[4,9]},index=[41,43])
    actual = stack_sheets(a, b)
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
