from solution import *

def test_01_convert_without_mutation():
    """Convert changing dates and leave the input untouched"""
    for dates in [["2026-09-03", "2026-09-04"], ["2024-01-31"]]:
        original = pd.DataFrame({"signed_on": dates, "volunteer": list(range(len(dates)))})
        result = convert_signups(original)
        assert pd.api.types.is_datetime64_any_dtype(result.signed_on)
        assert result.signed_on.dt.strftime("%Y-%m-%d").tolist() == dates
        assert original.signed_on.tolist() == dates
