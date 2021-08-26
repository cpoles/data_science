"""Improvement of the simulation of the Guess the Number game"""


# import the necessary libraries
import random


def guess_the_number():
    """Logic of the game Guess the Number"""
    # get a random number from 1 to 1000
    number = random.randrange(1, 1000)

    guess = 0
    gcounter = 0
    # compare guess and selected number
    while guess != number:
        # get user input
        guess = int(input('Guess my number between 1 to 1000: '))
        # compare with number
        if guess > number:
            print('Too high. Try again')
            gcounter += 1
        elif guess < number:
            print('Too low. Try again')
            gcounter += 1
        else:
            # if equal, congratulate the user
            print('Congratulations, you guessed the number!')
            print(f'You used {gcounter} guesses')
            # check the number of guesses and provide feedback
            if gcounter > 10:
                print('You should be able to do better')
            else:
                print('Either you know the secret or you got lucky.')
            #  give the option to restart the game or quit.
            response = input(("Would you like to play it again? "
                              "('yes' or  'no'): "))
            # check user response
            if response == 'yes':
                number = random.randrange(1, 100)
                guess = 0
                gcounter = 0
            elif response == 'no':
                print('Bye.')
                break
            else:
                print('Invalid response. Quitting...')
                break
