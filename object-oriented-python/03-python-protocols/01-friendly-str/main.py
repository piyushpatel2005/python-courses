class TrailMarker:
    def __init__(self, destination, km):
        self.destination = destination
        self.km = km

    def __str__(self):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print(str(TrailMarker("Lake", 4)))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
