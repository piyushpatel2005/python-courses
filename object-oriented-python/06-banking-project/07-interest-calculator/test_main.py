from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_interest_calculation():
    """Calculate integer simple interest without account state"""
    assert not issubclass(InterestCalculator, Account)
    calculator = InterestCalculator()
    for principal, rate, months, expected in [(20000, 600, 3, 300), (10001, 333, 7, 194), (119999, 1, 1, 0), (120000, 1, 1, 1), (0, 500, 12, 0), (10000, 0, 12, 0), (10000, 500, 0, 0), (999, 10000, 24, 1998)]:
        result = calculator.calculate(principal, rate, months)
        assert type(result) is int, "Return integer cents, not a float"
        assert result == expected
    for position in range(3):
        for bad in [-1, 1.5, "2", True, False, None]:
            arguments = [10000, 300, 12]
            arguments[position] = bad
            _expect_value_error(lambda: calculator.calculate(*arguments))
