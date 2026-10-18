oil_units = 6
key_count = 1
gate_closed = True
enough_oil = oil_units >= 4
can_enter = enough_oil and key_count >= 1
needs_supplies = oil_units < 4 or key_count == 0
gate_open = not gate_closed
print(enough_oil)
print(can_enter)
print(needs_supplies)
print(gate_open)
