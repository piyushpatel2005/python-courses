from solution import *
import pandas as pd

def test_01_exercise_custom_labels():
    """Make `shift_card(names, counts)` return a Series whose index is `names` and whose values are `counts`."""
    assert isinstance(shift_card(["east", "west"], [4, 9]), pd.Series) and shift_card(["east", "west"], [4, 9]).to_dict() == {"east": 4, "west": 9} and shift_card(["solo"], [13]).index.tolist() == ["solo"]

