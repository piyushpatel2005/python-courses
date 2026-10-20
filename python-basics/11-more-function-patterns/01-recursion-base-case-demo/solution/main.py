def days_left(number):
    if number == 0:
        return [0]
    return [number] + days_left(number - 1)


sample = days_left(3)
print("Days until opening:", sample)
