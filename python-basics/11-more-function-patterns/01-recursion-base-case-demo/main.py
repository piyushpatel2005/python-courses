def pulse_steps(number):
    if number == 0:  # Stop here: no further call.
        return [0]
    return [number] + pulse_steps(number - 1)

sample = pulse_steps(2)  # Change the argument to 3.
print("Tower pulses:", sample)
