

import random

def guessing_game():
    number = random.randint(1,100)
    #print(f'The Number is {number}')
    while True:
        guess = int(input('What is your guess?'))
        if number == guess: 
            print(f"Your guess of {guess} is Just Right")
            break
        elif number > guess:
            print(f'Your guess of {guess} is Too Low')
        else:
            print(f' Your guess of {guess} is Too High')

guessing_game()



