from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_opening_balance():
    """Store valid opening cents and reject invalid balances"""
    for amount in [0, 1, 13579]:
        account = Account("Nia", amount)
        assert (account.owner, account.balance_cents) == ("Nia", amount)
    assert Account("Default").balance_cents == 0
    first, second = Account("A", 20), Account("B", 30)
    first.owner = "Changed"
    assert second.owner == "B" and second.balance_cents == 30
    for bad in [-1, -500, 1.5, "100", True, False, None]:
        _expect_value_error(lambda: Account("Bad", bad))
