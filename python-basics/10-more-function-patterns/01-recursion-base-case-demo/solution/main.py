def step_down(number):
    if number == 0:
        return [0]
    return [number] + step_down(number - 1)

sample = step_down(3)
print(sample)
