def parse_seats(text):
    try:
        return int(text)
    except ValueError:
        return 0


print("Valid seats:", parse_seats("3"))
print("Invalid seats:", parse_seats("three"))
