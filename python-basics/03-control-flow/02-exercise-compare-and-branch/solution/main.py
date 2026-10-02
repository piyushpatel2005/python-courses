sparks_left = 2
low_signal = sparks_left < 3
if sparks_left == 0:
    gate_status = "Sealed"
elif low_signal:
    gate_status = "Fading"
else:
    gate_status = "Open"
print(low_signal)
print(gate_status)
