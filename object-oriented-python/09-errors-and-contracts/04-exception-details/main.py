class StockShortage(Exception):
    def __init__(self, requested, available):
        pass


if __name__ == "__main__":
    try:
        print(StockShortage(6, 2))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
