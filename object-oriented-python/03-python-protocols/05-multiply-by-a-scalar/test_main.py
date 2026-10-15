from solution import *


def test_01_multiply_by_a_scalar():
    for count, factor in ((7, 3), (4, 0), (2, -5)):
        source = ScoreDelta(count)
        result = source * factor
        assert isinstance(result, ScoreDelta)
        assert result.points == count * factor
        assert result is not source and source.points == count
    for bad in (True, 2.0, "2", None):
        assert ScoreDelta(4).__mul__(bad) is NotImplemented
