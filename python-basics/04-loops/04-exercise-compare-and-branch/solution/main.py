charge_left = 2
gate_signal = "Not set"

if charge_left == 0:
    gate_signal = "Sealed"
elif charge_left < 4:
    gate_signal = "Flickering"
else:
    gate_signal = "Open"
print(gate_signal)
