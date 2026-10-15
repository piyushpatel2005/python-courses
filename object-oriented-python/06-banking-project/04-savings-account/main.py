class Account:
    def __init__(self, owner, balance_cents=0):
        if type(balance_cents) is not int or balance_cents < 0:
            raise ValueError("Opening balance must be nonnegative integer cents")
        self.owner = owner
        self._balance_cents = balance_cents

    @property
    def balance_cents(self):
        return self._balance_cents

    def deposit(self, amount_cents):
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("Deposit must be positive integer cents")
        self._balance_cents += amount_cents
        return self.balance_cents

    def withdraw(self, amount_cents):
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("Withdrawal must be positive integer cents")
        if amount_cents > self.balance_cents:
            raise ValueError("Insufficient balance")
        self._balance_cents -= amount_cents
        return self.balance_cents


class SavingsAccount(Account):
    def __init__(self, owner, balance_cents=0, rate_bps=300):
        # TODO: initialize the account and store a valid rate.
        pass

if __name__ == "__main__":
    account = Account("Mira", 1250)
    print("Opening cents:", getattr(account, "balance_cents", "unfinished"))

    deposit_account = Account("Mira", 1250)
    print("After deposit:", deposit_account.deposit(250))

    withdrawal_account = Account("Mira", 1500)
    print("After withdrawal:", withdrawal_account.withdraw(400))

    savings = SavingsAccount("Mira", 10000)
    print("Savings rate:", getattr(savings, "rate_bps", "unfinished"))
