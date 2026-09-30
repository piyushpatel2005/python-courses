prices = [3, 5, 7]
with_fee = list(map(lambda price: price + 2, prices))
over_six = list(filter(lambda price: price > 6, with_fee))
print("With fee:", with_fee)
print("Over six:", over_six)
