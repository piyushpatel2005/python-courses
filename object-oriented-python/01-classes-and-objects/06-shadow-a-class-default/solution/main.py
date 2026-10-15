class Tool:
    loan_days = 7

def extend_loan(tool, days):
    tool.loan_days = days


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = Tool(), Tool()
        extend_loan(first, 14)
        print("Loan periods:", first.loan_days, second.loan_days, Tool.loan_days)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
