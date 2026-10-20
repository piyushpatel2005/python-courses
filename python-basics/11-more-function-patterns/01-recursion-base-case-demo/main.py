def days_left(number):
    if number == 0:  # Stop here instead of calling days_left again.
        return [0]
    return [number] + days_left(number - 1)


sample = days_left(2)  # Change the argument to 3.
print("Days until opening:", sample)
