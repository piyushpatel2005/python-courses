from solution import *

def test_01_checkpoint():
    'In `is_min_heap`, check every nonroot item against its parent without changing the list.'
    for a in [[], [2], [1, 6, 3, 9, 8, 4], [2, 2, 2]]:
        before = a[:]
        assert is_min_heap(a) is True and a == before
    for a in [[3, 1], [1, 6, 3, 9, 2], [1, 4, 2, 5, 6, 0]]:
        assert is_min_heap(a) is False

