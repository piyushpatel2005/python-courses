def pulse_steps(number):
    if number == 0:
        return [0]
    return [number] + pulse_steps(number - 1)

sample = pulse_steps(3)
print("Tower pulses:", sample)
