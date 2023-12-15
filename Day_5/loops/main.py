#for loop in Python

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")


heights = [151, 145, 179]

count = 0
avg = 0

for height in heights:
    avg += height
    count += 1
avg /= count

print(f"Average height is: {avg}")