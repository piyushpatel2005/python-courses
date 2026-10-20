prices = [3, 5, 7]
with_delivery = list(map(lambda price: price + 2, prices))
over_six = list(filter(lambda price: price > 6, with_delivery))
print("With delivery:", with_delivery)
print("Over $6:", over_six)
