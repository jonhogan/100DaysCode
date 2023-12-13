import random

coin = random.randint(1, 2)

if coin % 2 == 0:
    print("Heads")
else:
    print("Tails")