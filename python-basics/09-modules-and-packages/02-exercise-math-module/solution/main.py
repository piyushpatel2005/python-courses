import math

def vans_needed(people):
    return math.ceil(people / 6)

print(vans_needed(13))
