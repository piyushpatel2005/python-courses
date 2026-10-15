from solution import *


def test_01_complete_operation():
    """Mark aliases without mistaking equal objects for aliases."""
    target = [1]
    other = [1]
    data = [other, target, [], target]
    result = identity_flags(data, target)
    assert result == [False, True, False, True]
    assert all(type(flag) is bool for flag in result)
    assert len(data) == 4 and data[0] is other
    assert identity_flags([], target) == []
    assert identity_flags([other], other) == [True]
    assert identity_flags([other], target) == [False]
    result.append(True)
    assert len(data) == 4
