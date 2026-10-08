from solution import *

def test_01_export_report_text():
    """Export variable neighborhood totals without an index column"""
    for rows, index in [([("North", 3, 7.5), ("South", 4, 16.0)], [20, 21]), (["East", 2, 3.25], [91])]:
        if isinstance(rows[0], tuple):
            frame = pd.DataFrame(rows, columns=["neighborhood", "units", "revenue"], index=index)
        else:
            frame = pd.DataFrame([rows], columns=["neighborhood", "units", "revenue"], index=index)
        text = export_report(frame)
        assert text.splitlines()[0] == "neighborhood,units,revenue"
        recovered = pd.read_csv(StringIO(text))
        pd.testing.assert_frame_equal(recovered, frame.reset_index(drop=True))
