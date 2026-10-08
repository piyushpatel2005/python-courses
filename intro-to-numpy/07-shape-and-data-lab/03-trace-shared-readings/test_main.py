from solution import *

def test_01_shape_and_actual_sharing():
    assert card.shape == (3, 2)
    assert shared == np.shares_memory(raw, card)
