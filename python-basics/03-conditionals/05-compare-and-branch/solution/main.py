loaves_left = 4
delivery_today = False
if loaves_left < 8:
    stock_message = "Bake more bread"
elif loaves_left < 16 and not delivery_today:
    stock_message = "Check the bread shelf"
else:
    stock_message = "Count inventory"
print(stock_message)
