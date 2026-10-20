def delivery_total(daily_deliveries):
    if not daily_deliveries:
        return 0
    return daily_deliveries[0] + delivery_total(daily_deliveries[1:])


print("Boxes delivered:", delivery_total([2, 3, 1]))
