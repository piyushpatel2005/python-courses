import math

def boards_needed(length):
    return math.ceil(length / 6)

print(boards_needed(13))
