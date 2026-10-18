for number in range(1, 16):
    label = str(number)
    if number % 3 == 0 and number % 5 == 0:
        label = "FizzBuzz"
    elif number % 3 == 0:
        label = "Fizz"
    elif number % 5 == 0:
        label = "Buzz"
    print(label)
