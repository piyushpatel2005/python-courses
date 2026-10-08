from solution import *
import pandas as pd

def test_01_preview_and_summarize():
    """Set `preview` to the first three rows using `head(3)`."""
    assert isinstance(preview, pd.DataFrame) and preview["stall"].tolist() == ["tea", "bread", "jam"] and preview.index.tolist() == [0, 1, 2]

