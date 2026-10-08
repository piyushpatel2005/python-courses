from solution import *
import pandas as pd

def test_host_names():
    """Rename and clean names with changing values"""
    for names in [["  ADA ", " Ben "], ["  ZOE", " TESS  ", "Li"]]:
        frame = pd.DataFrame({"host_name": names, "dept": ["food"] * len(names), "seats": range(len(names))}, index=[f"h{i}" for i in range(len(names))])
        before = frame.copy(deep=True)
        result = tidy_registrations(frame)
        assert "host_name" not in result.columns
        pd.testing.assert_series_equal(result["host"], frame["host_name"].str.strip().str.lower().rename("host"))
        pd.testing.assert_frame_equal(frame, before)

def test_department_names():
    """Change only the arts code and keep other columns"""
    frame = pd.DataFrame({"host_name": ["A", "B", "C"], "dept": ["arts", "food", "arts"], "seats": [1, 2, 3]}, index=list("xyz"))
    result = tidy_registrations(frame)
    pd.testing.assert_series_equal(result["dept"], pd.Series(["creative", "food", "creative"], index=list("xyz"), name="dept"))
    pd.testing.assert_series_equal(result["seats"], frame["seats"])
