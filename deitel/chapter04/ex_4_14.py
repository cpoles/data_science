"""Computer Assisted Instruction"""

import random


def multiplication():
    """Helps a student to practice multiplication"""
    while True:
        # generate numbers
        num1, num2 = generate_numbers()
        answer = num1 * num2
        # prompt user for response
        response = int(input(f'How much is {num1} * {num2}? '))
        if answer == response:
            print('Very good! Keep up the good work!')
        elif response == -1:
            print('Quitting...')
            break
        else:
            while answer != response:
                print('No. Please try again.')
                response = int(input(f'How much is {num1} * {num2}? '))
            print('Very good! Keep up the good work!')


def generate_numbers():
    """Generate two random numbers 1 - 10"""
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    return (num1, num2)
