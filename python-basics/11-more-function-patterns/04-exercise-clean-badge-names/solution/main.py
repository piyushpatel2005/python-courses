supply_prices = [4, 9, 2, 12]
discounted_prices = list(map(lambda price: price - 1, supply_prices))
within_budget = list(filter(lambda price: price <= 8, discounted_prices))
print("After coupon:", discounted_prices)
print("Within $8:", within_budget)
