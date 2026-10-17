player_text = "Adam"
flares_text = "3"
flare_cost = 6.0
flare_count = int(flares_text)
energy_cost = flare_count * flare_cost
display_line = f"Gear for {player_text}: {flare_count} flares, {energy_cost:.2f} energy"
print("Flares:", flare_count)
print("Energy:", energy_cost)
print(display_line)
