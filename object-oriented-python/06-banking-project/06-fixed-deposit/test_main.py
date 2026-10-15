from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_fixed_deposit_lock():
    """Reject all withdrawals from a fixed deposit"""
    assert issubclass(FixedDeposit, SavingsAccount)
    for opening in [0, 1, 35000]:
        account = FixedDeposit("Lee", opening, 450)
        for amount in [1, opening, 0, -1, 1.5, "all", True, None]:
            _expect_value_error(lambda: account.withdraw(amount))
            assert account.balance_cents == opening
        assert account.deposit(2) == opening + 2
        _expect_value_error(lambda: account.withdraw(2))
        assert account.balance_cents == opening + 2
