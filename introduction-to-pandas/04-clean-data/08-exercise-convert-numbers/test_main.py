from solution import *
import pandas as pd

def test_numeric_cases():
    """Coerce invalid text, preserve zero, and keep a nullable integer dtype"""
    for raw in [["3", "unknown", "0"], ["17", "", None, "-2"]]:
        frame = pd.DataFrame({"item": list("ABCD")[:len(raw)], "cases": raw}, index=[f"i{i}" for i in range(len(raw))])
        before = frame.copy(deep=True)
        expected = frame.copy()
        expected["cases"] = pd.to_numeric(frame["cases"], errors="coerce").astype("Int64")
        pd.testing.assert_frame_equal(numeric_cases(frame), expected)
        pd.testing.assert_frame_equal(frame, before)
