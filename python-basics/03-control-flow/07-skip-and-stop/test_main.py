from solution import *

def test_skip_third_tile():
    assert cleared == "Cleared 1 | Cleared 2 | Cleared 4 | ", "Skip tile 3 but still stop at tile 5"
