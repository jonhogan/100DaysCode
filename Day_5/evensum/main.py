try:
    target = int(input("Enter a number between 1 and 1000: "))
except(ValueError):
    # Set "target" to a number outside of the range, if a non-numeric value is entered
    target = 0

if  target > 0 and target < 1001:
    sum = 0
    for num in range(2, target + 1, 2):
        sum += num

    print(f"The sum of all even numbers between 1 and {target} is: {sum}")

else:
    print("You did not enter a valid number")