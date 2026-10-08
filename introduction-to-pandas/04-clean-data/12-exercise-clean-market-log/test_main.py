from solution import *
import pandas as pd

def test_rename_seller():
    """Rename only the seller column and preserve the source"""
    frame = pd.DataFrame({"seller_name": [" A ", "B"], "units": ["2", "5"]}, index=["x", "y"])
    before = frame.copy(deep=True)
    pd.testing.assert_frame_equal(rename_seller(frame), frame.rename(columns={"seller_name": "seller"}))
    pd.testing.assert_frame_equal(frame, before)

def test_tidy_seller():
    """Strip and lowercase names on an already renamed table"""
    frame = pd.DataFrame({"seller": [" A ", "  B", None], "units": ["2", "5", "9"]}, index=list("xyz"))
    before = frame.copy(deep=True)
    expected = frame.copy()
    expected["seller"] = expected["seller"].str.strip().str.lower()
    pd.testing.assert_frame_equal(tidy_seller(frame), expected)
    pd.testing.assert_frame_equal(frame, before)

def test_convert_units():
    """Coerce changing quantity text to nullable integers"""
    for units in [["2", "oops", "0"], ["9", None, "-3"]]:
        frame = pd.DataFrame({"seller": ["a", "b", "c"], "units": units}, index=list("xyz"))
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected["units"] = pd.to_numeric(expected["units"], errors="coerce").astype("Int64")
        pd.testing.assert_frame_equal(convert_units(frame), expected)
        pd.testing.assert_frame_equal(frame, before)

def test_drop_incomplete():
    """Discard rows with either missing seller or missing units"""
    frame = pd.DataFrame({"seller": ["a", None, "b", "c"], "units": pd.Series([2, 4, None, 0], index=list("wxyz"), dtype="Int64"), "status": ["pending"] * 4}, index=list("wxyz"))
    before = frame.copy(deep=True)
    pd.testing.assert_frame_equal(drop_incomplete(frame), frame.dropna(subset=["seller", "units"]))
    pd.testing.assert_frame_equal(frame, before)

def test_fill_category():
    """Replace missing categories without dropping rows"""
    frame = pd.DataFrame({"seller": ["a", "b", "c"], "category": [None, "food", None]}, index=list("xyz"))
    before = frame.copy(deep=True)
    pd.testing.assert_frame_equal(fill_category(frame), frame.fillna({"category": "unassigned"}))
    pd.testing.assert_frame_equal(frame, before)

def test_keep_latest():
    """Retain the final seller/day revision and original index"""
    frame = pd.DataFrame({"seller": ["a", "b", "a", "a"], "day": ["Fri", "Fri", "Fri", "Sat"], "units": [1, 2, 3, 4]}, index=list("abcd"))
    before = frame.copy(deep=True)
    pd.testing.assert_frame_equal(keep_latest(frame), frame.drop_duplicates(subset=["seller", "day"], keep="last"))
    pd.testing.assert_frame_equal(frame, before)

def test_mark_ready():
    """Apply changing thresholds without mutating the input"""
    for minimum in [0, 3, 8]:
        frame = pd.DataFrame({"seller": ["a", "b", "c"], "units": pd.Series([0, 3, 7], index=list("xyz"), dtype="Int64"), "status": ["pending", "review", "pending"]}, index=list("xyz"))
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected.loc[expected["units"] >= minimum, "status"] = "ready"
        pd.testing.assert_frame_equal(mark_ready(frame, minimum), expected)
        pd.testing.assert_frame_equal(frame, before)
