from solution import *

def test_01_step():
    """Reject invalid indices without changing the array."""
    for values in ([], [5, 8, 13]):
        array = Array(values)
        for index in (-1, len(values) + 0, len(values) + 2):
            before = (list(array._data), array.size, array.capacity)
            try:
                array.get(index)
                assert False, "Reject the index."
            except IndexError:
                pass
            assert (list(array._data), array.size, array.capacity) == before

def test_02_complete_operation():
    """Read occupied slots and reject every invalid boundary."""
    for values in ([], [None], [4, 4, 7]):
        array = Array(values)
        before = (array.snapshot(), array.size, array.capacity)
        for index, value in enumerate(values):
            assert array.get(index) is value
        for index in (-1, len(values), len(values) + 2):
            try:
                array.get(index)
                assert False, "Reject indices outside occupied slots."
            except IndexError:
                pass
        assert (array.snapshot(), array.size, array.capacity) == before
    payload = []
    first, second = Array([payload]), Array([])
    assert first.get(0) is payload and second.size == 0
