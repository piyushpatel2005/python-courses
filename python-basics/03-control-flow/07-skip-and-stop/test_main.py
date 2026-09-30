from solution import *

def test_skip_third_parcel():
    assert loaded == "Loaded 1 | Loaded 2 | Loaded 4 | ", "Skip parcel 3 but still stop at parcel 5"
