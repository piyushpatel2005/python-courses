import math

def beacons_needed(sparks):
    return math.ceil(sparks / 4)

print(beacons_needed(8))
