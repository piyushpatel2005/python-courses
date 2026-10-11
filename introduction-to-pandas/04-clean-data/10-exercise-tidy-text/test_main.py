from solution import *
import pandas as pd

def test_host_header():
    """Rename host_name to host without changing other headers"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'host_name': [' A ', None], 'dept': ['arts', 'food'], 'seats': [2, 4]}, index=['x', 'y'])
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        result = tidy_registrations(frame)
        assert list(result.columns) == ['host', 'dept', 'seats'], 'Rename host_name to host and keep the other headers.'
        pd.testing.assert_index_equal(result.index, frame.index)
        pd.testing.assert_frame_equal(frame, before)

def test_host_values():
    """Strip and lowercase host values, preserving missing names"""
    for names in [['  ADA ', ' Ben '], [' ZOE', None, 'Li  ']]:
        frame = pd.DataFrame({'host_name': names, 'dept': ['food'] * len(names), 'seats': range(len(names))}, index=[f'h{i}' for i in range(len(names))])
        before = frame.copy(deep=True)
        result = tidy_registrations(frame)
        assert 'host' in result, 'Rename the column before cleaning host values.'
        pd.testing.assert_series_equal(result['host'], frame['host_name'].str.strip().str.lower().rename('host'))
        pd.testing.assert_frame_equal(frame, before)

def test_department_names():
    """Replace only arts and preserve other columns and the input"""
    frame = pd.DataFrame({'host_name': ['A', 'B', 'C'], 'dept': ['arts', 'food', None], 'seats': [1, 2, 3]}, index=list('xyz'))
    before = frame.copy(deep=True)
    result = tidy_registrations(frame)
    pd.testing.assert_series_equal(result['dept'], frame['dept'].replace({'arts': 'creative'}))
    pd.testing.assert_series_equal(result['seats'], frame['seats'])
    pd.testing.assert_frame_equal(frame, before)
