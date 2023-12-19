import random

def select_word(words):
    return random.choice(words)


word_list = ['frozen', 'jungle', 'autumn', 'donkey', 'rocket', 'marble', 'spring', 'basket', 
             'stream', 'yellow', 'summer', 'winter', 'valley', 'shadow', 'orange', 'flower', 
             'castle', 'island', 'market', 'silver', 'bottle', 'guitar', 'rabbit', 'puzzle', 
             'candle', 'window', 'monkey', 'purple', 'garden', 'button', 'pencil', 'needle', 
             'mirror', 'turtle', 'forest', 'mystery', 'planet', 'cheese', 'bubble', 'dragon']

secret_word =select_word(word_list)

while True:
    player_guess = input("Guess a letter in the word:\n").lower()

    for letter in secret_word:
        if player_guess == letter:
            print("Right")
        else:
            print("Wrong")