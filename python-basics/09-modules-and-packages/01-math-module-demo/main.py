import math

def shelves_needed(items):
    return math.ceil(items / 4)

print(shelves_needed(9))
