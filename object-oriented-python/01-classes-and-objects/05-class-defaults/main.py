class Tool:
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        print("Class loan period:", Tool.loan_days)
        print("Instance loan period:", Tool().loan_days)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
