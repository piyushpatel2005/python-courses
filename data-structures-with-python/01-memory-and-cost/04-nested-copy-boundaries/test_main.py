from solution import *


def test_01_complete_operation():
    """Separate row containers without cloning the cells."""
    cell = []
    row = [cell]
    source = [row, [], row]
    result = copy_rows(source)
    assert result == source and result is not source
    assert all(a is not b for a, b in zip(result, source))
    assert result[0] is not result[2]
    assert result[0][0] is cell and result[2][0] is cell
    result[0].append(9)
    assert len(row) == 1 and len(result[2]) == 1
    result[1].append(8)
    assert source[1] == []
    assert copy_rows([]) == []
    assert copy_rows([[1, 2], [3]]) == [[1, 2], [3]]
