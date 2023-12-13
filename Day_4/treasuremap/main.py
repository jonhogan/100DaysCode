line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot")
print("Map layout:\n A B C\n1_|_|_|\n2_|_|_|\n3 | | |")
print("Position A3 will mark like this:\n A B C\n1_|_|_|\n2_|_|_|\n3X| | |")

position = input("Where do you want to put the treasure? ")

coord1 = position[0]
coord2 = int(position[1])

if coord1.lower() == 'a':
    coord1 = 0
elif coord1.lower() == 'b':
    coord1 = 1
elif coord1.lower() == "c":
    coord1 = 2

map[coord1][coord2 - 1] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")
