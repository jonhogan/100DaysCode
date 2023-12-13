'''
Rock Paper Scissors Game

Rock beats Scissors
Scissors beats Paper
Paper beats Rock

'''

import random

def rock():
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')

def paper():
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')

def scissors():
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

print("Welcome to Rock Paper Scissors\n\nHow to play: Enter 1 for Rock, 2 for Paper and 3 for Scissors.")

player = int(input("Would you like 1: Rock, 2: Paper or, 3: Scissors? "))
if player == 1:
    print("You picked Rock!")
    rock()
elif player == 2:
    print("You picked Paper!")
    paper()
elif player == 3:
    print("You picked Scissors!")
    scissors()

computer = random.randint(1,3)

if computer == 1:
    print("Computer picked Rock!")
    rock()
elif computer == 2:
    print("Computer picked Paper!")
    paper()
elif computer == 3:
    print("Computer picked Scissors!")
    scissors()

if player == computer:
    print("It is a draw!")
elif player == 1 or computer == 1:
    if player == 2:
        print("Paper covers Rocks, you win!")
    elif computer == 2:
        print("Paper covers Rocks, Computer wins.")
    elif player == 3:
        print("Rock smashes Scissors, Computer wins.")
    elif computer == 3:
        print("Rock smashes Scissors, You win!.")
elif player == 2 or computer == 2:
    if player == 3:
        print("Scissors cut Paper, Computer wins.")
    elif computer == 3:
        print("Scissors cut Paper, You wins.")

