print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
player_input = input("You're at a cross road. Do you left, or right? ")
if player_input.lower() == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    player_input = input('Would you like to "swim" across, or "wait" for a boat? ')
    if player_input.lower() == "wait":
        print("You arrive at the island unharmed.")
        player_input = input("You see a house with three doors. One is \"red\", one \"yellow\", and one \"blue\". Which door do you enter? ")
        if player_input.lower() == "red":
            print("You entered a room that is on fire. The floor is on fire, the walls are on fire, the door (which was cool to the touch) is now on fire.. you are on fire: GAME OVER!")
        elif player_input.lower() == "blue":
            print("You entered a room full of beasts, and are now lunch: GAME OVER!")
        elif player_input.lower() == "yellow":
            print("You did it, you found the treasure!!!")
        else:
            print("You came so close, but your lack of faith in yourself caused you to ponder which door until you succumbed to hunger: GAME OVER!")
    elif player_input.lower() == "swim":
        print("The current proves too strong and you are quickly pulled out into the water away from the island: GAME OVER!")
    else:
        print("Unable to come to a decision on swimming or waiting, you begin to pace about. You stumble over a branch and strike your head on a rock: GAME OVER!")
elif player_input.lower() == "right":
    print("You fell down a deep, inescapable hole: GAME OVER!")
else:
    print("Unable to make a decision on left or right, you stayed at the cross roads until you lost the strength to continue: GAME OVER!")