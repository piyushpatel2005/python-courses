from solution import *

def test_01():
    """Complete audit_badges(a, b) with an inner merge on badge and validate="one_to_one"."""
    a=pd.DataFrame({"badge":["P7","P8"],"time":[8,9]})
    b=pd.DataFrame({"badge":["P8","P7"],"name":["Lin","Kim"]})
    actual = audit_badges(a, b)
    expected = a.merge(b,on="badge",how="inner")
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
    for left,right in [(pd.concat([a,a.iloc[[0]]],ignore_index=True),b),(a,pd.concat([b,b.iloc[[0]]],ignore_index=True))]:
        try:
            audit_badges(left,right)
        except pd.errors.MergeError:
            pass
        else:
            assert False, "Reject duplicate keys on either side."
