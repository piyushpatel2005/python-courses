from solution import *
import pandas as pd

def test_rename_seller():
    """Rename only the seller column and preserve the source"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'seller_name': [' A ', 'B'], 'units': ['2', '5']}, index=['x', 'y'])
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        pd.testing.assert_frame_equal(rename_seller(frame), frame.rename(columns={'seller_name': 'seller'}))
        pd.testing.assert_frame_equal(frame, before)

def test_tidy_seller():
    """Strip and lowercase names on an already renamed table"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'seller': [' A ', '  B', None], 'units': ['2', '5', '9']}, index=list('xyz'))
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected['seller'] = expected['seller'].str.strip().str.lower()
        pd.testing.assert_frame_equal(tidy_seller(frame), expected)
        pd.testing.assert_frame_equal(frame, before)

def test_convert_units():
    """Coerce changing quantity text to nullable integers"""
    for units in [['2', 'oops', '0'], ['9', None, '-3']]:
        frame = pd.DataFrame({'seller': ['a', 'b', 'c'], 'units': units}, index=list('xyz'))
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected['units'] = pd.to_numeric(expected['units'], errors='coerce').astype('Int64')
        pd.testing.assert_frame_equal(convert_units(frame), expected)
        pd.testing.assert_frame_equal(frame, before)

def test_drop_incomplete():
    """Discard rows with either missing seller or missing units"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'seller': ['a', None, 'b', 'c'], 'units': pd.Series([2, 4, None, 0], index=list('wxyz'), dtype='Int64'), 'status': ['pending'] * 4}, index=list('wxyz'))
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        pd.testing.assert_frame_equal(drop_incomplete(frame), frame.dropna(subset=['seller', 'units']))
        pd.testing.assert_frame_equal(frame, before)

def test_fill_category():
    """Replace missing categories without dropping rows"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'seller': ['a', 'b', 'c'], 'category': [None, 'food', None]}, index=list('xyz'))
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        pd.testing.assert_frame_equal(fill_category(frame), frame.fillna({'category': 'unassigned'}))
        pd.testing.assert_frame_equal(frame, before)

def test_keep_latest():
    """Retain the final seller/day revision and original index"""
    for reverse_rows in [False, True]:
        frame = pd.DataFrame({'seller': ['a', 'b', 'a', 'a'], 'day': ['Fri', 'Fri', 'Fri', 'Sat'], 'units': [1, 2, 3, 4]}, index=list('abcd'))
        if reverse_rows:
            frame = frame.iloc[::-1].copy()
            frame.index = ['changed-' + str(i) for i in range(len(frame))]
        before = frame.copy(deep=True)
        pd.testing.assert_frame_equal(keep_latest(frame), frame.drop_duplicates(subset=['seller', 'day'], keep='last'))
        pd.testing.assert_frame_equal(frame, before)

def test_mark_ready():
    _uses('loc', 'mark_ready')
    'Apply changing thresholds without mutating the input'
    for minimum in [0, 3, 8]:
        frame = pd.DataFrame({'seller': ['a', 'b', 'c'], 'units': pd.Series([0, 3, 7], index=list('xyz'), dtype='Int64'), 'status': ['pending', 'review', 'pending']}, index=list('xyz'))
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected.loc[expected['units'] >= minimum, 'status'] = 'ready'
        pd.testing.assert_frame_equal(mark_ready(frame, minimum), expected)
        pd.testing.assert_frame_equal(frame, before)

def _uses(attribute, function=None):
    import ast
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    if function:
        tree = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function))
    assert any((isinstance(n, ast.Attribute) and n.attr == attribute for n in ast.walk(tree))), 'Use ' + attribute + ' for this task, rather than a fixed answer.'
