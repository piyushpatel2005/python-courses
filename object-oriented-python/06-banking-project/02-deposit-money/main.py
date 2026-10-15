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
        # TODO: accept a positive integer deposit and return the new balance.
        pass

if __name__ == "__main__":
    account = Account("Mira", 1250)
    print("Opening cents:", getattr(account, "balance_cents", "unfinished"))

    deposit_account = Account("Mira", 1250)
    print("After deposit:", deposit_account.deposit(250))
