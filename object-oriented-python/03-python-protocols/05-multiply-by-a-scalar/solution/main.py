class SheetBatch:
    def __init__(self, sheets):
        self.sheets = sheets

    def __mul__(self, factor):
        if type(factor) is not int:
            return NotImplemented
        return SheetBatch(self.sheets * factor)


if __name__ == "__main__":
    try:
        print("Scaled sheets:", (SheetBatch(7) * 3).sheets)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
