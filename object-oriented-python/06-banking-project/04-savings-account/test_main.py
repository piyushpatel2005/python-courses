from solution import *

def _expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    assert False, "Reject this value with ValueError"


def test_savings_record():
    """Extend Account with a valid annual rate"""
    assert issubclass(SavingsAccount, Account)
    default = SavingsAccount("Eli")
    assert (default.owner, default.balance_cents, default.rate_bps) == ("Eli", 0, 300)
    for rate in [0, 1, 475]:
        account = SavingsAccount("Flo", 600, rate)
        assert account.rate_bps == rate and account.balance_cents == 600
        assert account.deposit(50) == 650
        assert account.withdraw(650) == 0
    for bad in [-1, 1.5, "300", True, None]:
        _expect_value_error(lambda: SavingsAccount("Gus", 0, bad))
    _expect_value_error(lambda: SavingsAccount("Gus", -1, 300))
    calls = []
    original = Account.__init__
    def tracked(self, owner, balance_cents=0):
        calls.append((owner, balance_cents))
        original(self, owner, balance_cents)
    Account.__init__ = tracked
    try:
        SavingsAccount("Hal", 17, 0)
        assert calls == [("Hal", 17)]
    finally:
        Account.__init__ = original
