from solution import *

def test_01_roundtrip():
    """Preserve columns and values, not an old row index"""
    for frame in [
        pd.DataFrame({"product": ["Tea", "Bread"], "units": [2, 5]}, index=[8, 9]),
        pd.DataFrame({"product": ["Honey"], "units": [12]}, index=[77]),
        pd.DataFrame({"product": ["East Side", "Jam, nuts"], "units": [4, 6]}, index=[31, 45]),
    ]:
        text, restored = roundtrip_table(frame)
        assert text.splitlines()[0] == "product,units"
        assert list(restored.columns) == ["product", "units"]
        pd.testing.assert_frame_equal(restored, frame.reset_index(drop=True))
