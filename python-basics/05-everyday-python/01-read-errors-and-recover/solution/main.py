def parse_energy(text):
    try:
        return int(text)
    except ValueError:
        return 0


print("Valid energy:", parse_energy("3"))
print("Invalid energy:", parse_energy("unknown"))
