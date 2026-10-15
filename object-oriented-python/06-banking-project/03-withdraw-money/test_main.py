from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_withdrawal():
    """Withdraw up to the exact available balance"""
    account = Account("Cal", 300)
    assert account.withdraw(1) == 299
    for bad in [300, 0, -1, 2.5, "20", True, False, None]:
        _expect_value_error(lambda: account.withdraw(bad))
        assert account.balance_cents == 299
    assert account.withdraw(299) == 0
    assert type(account.balance_cents) is int
    _expect_value_error(lambda: account.withdraw(1))
    assert account.balance_cents == 0
    other = Account("Dee", 8)
    assert other.withdraw(3) == 5
