def locker_label(directory, number):
    try:
        return directory[number]
    except KeyError:
        return "Unknown locker"


if __name__ == "__main__":
    try:
        print(locker_label({4: "Noor"}, 9))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
