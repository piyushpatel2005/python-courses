from solution import *


def test_01_complete_operation():
    """Copy the outer list while keeping nested objects shared."""
    for source in ([], [1, 2], [[], []]):
        result = copy_outer(source)
        assert result == source and result is not source
        assert all(a is b for a, b in zip(result, source))
        result.append("new")
        assert len(result) == len(source) + 1
    row = []
    source = [row, row]
    result = copy_outer(source)
    row.append(7)
    assert result == [[7], [7]] and result[0] is result[1]
