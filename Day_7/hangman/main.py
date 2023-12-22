import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def select_word(words):
    return random.choice(words)

def guess_word(game_word, guessed_letters):
    puzzle_string = ''
    for letter in game_word:
            if letter in guessed_letters:
                puzzle_string += letter
            else:
                puzzle_string += '_'
    return puzzle_string




play = True
while play:
    word_list = [
        'frozen', 'jungle', 'autumn', 'donkey', 'rocket', 'marble', 'spring',
        'basket', 'stream', 'yellow', 'summer', 'winter', 'valley', 'shadow',
        'orange', 'flower', 'castle', 'island', 'market', 'silver', 'bottle',
        'guitar', 'rabbit', 'puzzle', 'candle', 'window', 'monkey', 'purple',
        'garden', 'button', 'pencil', 'needle', 'mirror', 'turtle', 'forest',
        'mystery', 'planet', 'cheese', 'bubble', 'dragon'
    ]

    secret_word = select_word(word_list)

    correct_guess = False
    guess_count = 0
    correct_letters = []

    #puzzle_string = ''
    while not correct_guess:
        clear()

        print(guess_word(secret_word, correct_letters))

        player_guess = input("Guess a letter in the word:\n").lower()

        if player_guess in secret_word:
            print("You guessed a letter")
            correct_letters.append(player_guess)
        else:
            print("Wrong")
        
        if guess_count > 14:
            correct_guess = True

        if guess_word(secret_word, correct_letters) == secret_word:
            correct_guess = True
            print(f"{secret_word}!!")
            print("You win!")
        guess_count += 1

        time.sleep(.5)
        puzzle_string = ''

    replay = input("Game over. would you like to replay? (y/n)\n").lower()

    if replay in ("no", "n"):
        play = False
