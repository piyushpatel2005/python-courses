def signal_total(signals):
    if not signals:
        return 0
    return signals[0] + signal_total(signals[1:])

print("Beacon signal:", signal_total([2, 3, 1]))
