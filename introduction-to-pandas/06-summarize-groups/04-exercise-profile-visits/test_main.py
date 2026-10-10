from solution import *

def test_01():
    """Return the numeric visitors description in the first tuple slot."""
    a = pd.DataFrame({'type': ['Food', None, 'Food', 'Book'], 'visitors': [3.0, 9.0, None, 12.0]})
    actual = visit_profile(a)
    pd.testing.assert_series_equal(actual[0], a['visitors'].describe())

def test_02():
    """Return type frequencies, including missing labels, in the second tuple slot."""
    a = pd.DataFrame({'type': ['Food', None, 'Food', 'Book'], 'visitors': [3.0, 9.0, None, 12.0]})
    actual = visit_profile(a)
    pd.testing.assert_series_equal(actual[1], a['type'].value_counts(dropna=False))
