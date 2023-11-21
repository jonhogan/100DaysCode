# Program to accept user input and calculate the amount each person would pay including the tip

print("Welcome to the Tip Calculator.")
bill_amount = float(input("What is the bill total? "))
tip_percent = float(input("What percent would you like to tip? 10, 12, or 15: ")) / 100
num_people = int(input("How many people will split the bill? "))
even_split = (bill_amount + (bill_amount * tip_percent))/num_people

print(f"Each person should pay: ${even_split:.2f}.")