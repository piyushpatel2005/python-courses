import math

def boxes_needed(length):
    return math.ceil(length / 4)

print(boxes_needed(8))
