forge = "Gear Forge"
flare_count = 4
flare_price = 2.5
cost = flare_count * flare_price
gear_line = f"{flare_count} flares for {forge}"
cost_line = f"Cost: ${cost:.2f}"
print(gear_line)
print(cost_line)
