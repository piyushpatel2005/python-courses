from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_deposit():
    """Apply only valid positive-cent deposits"""
    account = Account("Ada", 100)
    untouched = Account("Bea", 50)
    assert account.deposit(1) == 101
    assert account.deposit(999) == 1100
    assert account.balance_cents == 1100 and untouched.balance_cents == 50
    assert type(account.balance_cents) is int
    for bad in [0, -1, -40, 1.0, "10", True, False, None]:
        _expect_value_error(lambda: account.deposit(bad))
        assert account.balance_cents == 1100
    empty = Account("Zero")
    assert empty.deposit(7) == 7
