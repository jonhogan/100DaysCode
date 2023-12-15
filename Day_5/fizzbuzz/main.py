for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)