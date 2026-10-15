from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_current_withdrawal():
    """Enforce the current account's own withdrawal boundary"""
    assert issubclass(CurrentAccount, Account)
    account = CurrentAccount("Ira", 200, 500)
    assert account.withdraw(201) == -1
    assert account.withdraw(499) == -500
    assert type(account.balance_cents) is int
    for bad in [1, 0, -1, 2.0, "1", True, None]:
        _expect_value_error(lambda: account.withdraw(bad))
        assert account.balance_cents == -500
    assert account.deposit(500) == 0
    assert account.withdraw(500) == -500
    no_overdraft = CurrentAccount("Jay", 3)
    assert no_overdraft.withdraw(3) == 0
    _expect_value_error(lambda: no_overdraft.withdraw(1))
    fresh = CurrentAccount("Kay", 10, 20)
    _expect_value_error(lambda: fresh.withdraw(31))
    assert fresh.balance_cents == 10
    for bad in [0, -1, 2.0, "1", True, False, None]:
        _expect_value_error(lambda: fresh.withdraw(bad))
        assert fresh.balance_cents == 10, "Reject invalid amounts even when the account has spending room."
