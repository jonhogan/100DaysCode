print("The Love Calculator is calculating your score...")
name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

combined_name = name1.lower() + name2.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
first_digit = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")