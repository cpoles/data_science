"""Simulation of the Guess the Number game"""


# import the necessary libraries
import random


def guess_the_number():
    """Logic of the game Guess the Number"""
    # get a random number from 1 to 1000
    number = random.randrange(1, 1000)

    guess = 0
    # compare guess and selected number
    while guess != number:
        # get user input
        guess = int(input('Guess my number between 1 to 1000: '))
        # compare with number
        if guess > number:
            print('Too high. Try again')
        elif guess < number:
            print('Too low. Try again')
        else:
            # if equal, give the option to restart the game or quit.
            print('Congratulations, you guessed the number!')
            response = input(("Would you like to play it again? "
                              "('yes' or  'no'): "))
            if response == 'yes':
                number = random.randrange(1, 100)
                guess = 0
            elif response == 'no':
                print('Bye.')
                break
            else:
                print('Invalid response. Quitting...')
                break
