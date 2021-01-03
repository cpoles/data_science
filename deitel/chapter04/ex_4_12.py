"""The tortoise and the hare game simulator"""

# import libraries
import random
import time

# type aliases
Move = int
Position = int  # position is linear on the x axis
Animal = str
Track = str


def race():
    """The logic for the race"""
    # create animals
    hare = 'hare'
    h_ini = 'H'
    tortoise = 'tortoise'
    t_ini = 'T'

    # set initial positions
    hare_pos = 1
    tortoise_pos = 1

    # print start message
    print('BANG !!!!!!\nAND THEY ARE OFF')

    while True:
        hare_pos = move_animal(hare, hare_pos)
        tortoise_pos = move_animal(tortoise, tortoise_pos)
        # sentinel
        if hare_pos > 70 or tortoise_pos > 70:
            break
        # print the animal's positions
        track(h_ini, hare_pos, t_ini, tortoise_pos)

    print(f'{hare} final position: {hare_pos}')
    print(f'{tortoise} final position: {tortoise_pos}')


def track(an1: Animal, pos1: Position,
          an2: Animal, pos2: Position) -> Track:
    """Prints the animals' positions"""
    if pos1 == pos2 and pos1 == 70:
        str_track = 'YAY!!! IT IS A TIE!!!!'
        print(70 * ' ', end="\r")
        print(str_track)
    elif pos1 == 70:
        str_track = f'YAY!! {an1} WINS!'
        print(70 * ' ', end="\r")
        print(str_track)
    elif pos2 == 70:
        str_track = f'YAY!! {an2} WINS!'
        print(70 * ' ', end="\r")
        print(str_track)
    elif pos1 > pos2:
        # create string and add trailing spaces
        str_track = f'{an1:>{pos1 - pos2}} {an2:>{pos2}}'
        end = ((70 - pos1) * ' ') + 'FINISH'
        # print str, clear str and terminal and print on the same line
        print(str_track + end, end="\r")
        time.sleep(1)
        print(' ', end="\r")
    elif pos1 < pos2:
        str_track = f'{an1:>{pos1}} {an2:>{pos2 - pos1}}'
        end = ((70 - pos2) * ' ') + 'FINISH'
        print(str_track + end, end="\r")
        print(' ', end="\r")
        time.sleep(1)
    elif pos1 == pos2 and pos1 != 70:
        ouch = 'OUCH!!'
        str_track = f'{ouch:>{pos1}}' + ((70 - pos1) * ' ')
        print(str_track, end="\r")
        time.sleep(1)
        print(' ', end="\r")


def move_animal(animal: Animal, position: Position) -> Position:
    """Creates the moves of the animals"""
    step = random.randrange(1, 11)
    if animal == 'tortoise':
        if 1 <= step <= 5:
            move = "fast plod"
            position = position + 3
        elif 6 <= step <= 7:
            move = 'slip'
            position = -6 + position
        elif 8 <= step <= 10:
            move = 'slow pod'
            position = 1 + position
    elif animal == 'hare':
        if 1 <= step <= 2:
            move = 'sleep'
            # step = 0 . position does not change
        elif 3 <= step <= 4:
            move = 'big hop'
            position = 9 + position
        elif step == 5:
            move = 'big slip'
            position = -12 + position
        elif 6 <= step <= 8:
            move = 'small hop'
            position = 1 + position
        elif 9 <= step <= 10:
            move = 'small slip'
            position = 2 + position

    if position < 1:
        position = 1

#    print(f'{move}')

    return position
