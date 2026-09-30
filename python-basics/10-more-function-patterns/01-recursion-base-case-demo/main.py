def step_down(number):
    if number == 0:  # Base case.
        return [0]
    return [number] + step_down(number - 1)

sample = step_down(2)  # Change the argument to 3.
print(sample)
