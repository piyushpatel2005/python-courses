def bundle_total(bundles):
    if not bundles:
        return 0
    return bundles[0] + bundle_total(bundles[1:])

print("Tickets:", bundle_total([2, 3, 1]))
