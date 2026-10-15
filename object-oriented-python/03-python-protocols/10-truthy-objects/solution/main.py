class Battery:
    def __init__(self, charge, enabled=True):
        self.charge = charge
        self.enabled = bool(enabled)

    def __bool__(self):
        return self.enabled and self.charge > 0


if __name__ == "__main__":
    try:
        print("Charged:", bool(Battery(8)))
        print("Switched off:", bool(Battery(8, False)))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
