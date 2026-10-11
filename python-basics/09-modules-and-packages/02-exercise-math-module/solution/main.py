import math

def lanterns_needed(sparks):
    return math.ceil(sparks / 6)

print(lanterns_needed(13))
