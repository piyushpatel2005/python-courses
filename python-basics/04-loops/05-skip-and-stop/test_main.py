from solution import *

def test_skip_third_order():
    assert packed == "Packed 1 | Packed 2 | Packed 4 | ", "Skip order 3 but still stop before order 5"
