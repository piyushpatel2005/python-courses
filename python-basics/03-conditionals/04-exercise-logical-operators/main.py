oil_units = 6
key_count = 1
gate_closed = True
enough_oil = oil_units >= 4
can_enter = False  # Require both enough_oil and at least one key.
needs_supplies = True  # Check for either missing supply.
gate_open = True  # Reverse gate_closed.
print(enough_oil)
print(can_enter)
print(needs_supplies)
print(gate_open)
