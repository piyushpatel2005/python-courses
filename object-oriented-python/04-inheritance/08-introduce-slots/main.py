class MapCell:
    pass  # TODO: complete the requested behavior.

    def __init__(self, row, column):
        self.row = row
        self.column = column


if __name__ == "__main__":
    try:
        point = MapCell(2, 5)
        print("Coordinates:", point.row, point.column)
        try:
            point.colum = 9
            print("Extra attribute accepted; add slots.")
        except AttributeError:
            print("Extra attribute rejected.")
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
