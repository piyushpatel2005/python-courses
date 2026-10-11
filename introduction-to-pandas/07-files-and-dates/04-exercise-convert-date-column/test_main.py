from solution import *


def test_01_convert_without_mutation():
    """Convert valid dates and preserve rows with invalid or missing dates"""
    for dates in [["2026-09-03", "2026-09-04"], ["2024-02-29", "bad", None, "2025-02-29"]]:
        original = pd.DataFrame({"signed_on": dates, "volunteer": list(range(len(dates)))}, index=list(range(20, 20 + len(dates))))
        before = original.copy(deep=True)
        result = convert_signups(original)
        expected = before.copy()
        expected["signed_on"] = pd.to_datetime(expected["signed_on"], format="%Y-%m-%d", errors="coerce")
        assert pd.api.types.is_datetime64_any_dtype(result.signed_on)
        pd.testing.assert_frame_equal(result, expected)
        pd.testing.assert_frame_equal(original, before)
