# tic_tac_toe.py
"""Two Player, Two-Dimensional Tic-Tac-Toe"""

# import libraries
import numpy as np


def check_input(char):
    '''Checks user's input's validity'''
    if len(char) == 1 and char.isdigit():
        dig = int(char)
        if dig > 2:
            raise ValueError('The board is 3x3. Only numbers 0-2 allowed.')
    else:
        raise ValueError('Only positive numbers allowed')

    return dig


def write_board(row, column, board, letter):
    '''Writes user input to the board'''
    if board[row, column] == ' ':
        board[row, column] = letter
        print(f'Entered {letter} at position ({row}, {column})')
        return True

    print('Wrong position. Try again...')
    return False


def check_seq(seq):
    '''Checks if all elems of a sequence are equal'''
    return len(set(seq)) == 1 if ' ' not in seq else False


def get_diagonals(multidim):
    '''Get the diagonals from a 3 x 3 board'''
    f_diagonal = [multidim[0, 0], multidim[1, 1], multidim[2, 2]]
    s_diagonal = [multidim[2, 0], multidim[1, 1], multidim[0, 2]]

    return [f_diagonal, s_diagonal]


def check_win(multidim):
    '''Checks for a winning combination'''
    # check rows
    rows = any(list(map(check_seq, multidim)))
    # check columns
    columns = any(list(map(check_seq, multidim.T)))
    # check diagonals
    diagonals = any(list(map(check_seq, get_diagonals(multidim))))

    return rows or columns or diagonals


# Define a print board method
def print_board(board):
    '''Prints the current board's state'''
    board_str = ''
    for row in board:
        board_str += '|'
        for column in row:
            board_str += f' {column} |'
        print(board_str)
        print('-------------')
        board_str = ''


def game():
    '''Simulates the tic tac toe game'''
    p1_count = 0
    p2_count = 0
    board = np.full((3, 3), ' ')  # fills the board with empty spaces
    p1_turn = False
    # p2_turn = False
    letter = ''
    print_board(board)  # print initial board

    while True:
        # get players turn
        if not p1_turn:
            p1_turn = True
            p1_count += 1
            letter = 'X'
            print(f"Player's 1 turn. Letter: {letter}. Round {p1_count}.")
        else:
            p1_turn = False
            # p2_turn = True
            p2_count += 1
            letter = 'O'
            print(f"Player's 2 turn. Letter: {letter}. Round {p2_count}.")

        # get and check user input
        p_input = input('Enter row number: ')
        row = check_input(p_input)
        p_input = input('Enter column number: ')
        column = check_input(p_input)

        # write to the board
        if write_board(row, column, board, letter):
            print_board(board)
            if check_win(board):
                if p1_turn:
                    print('Player 1 Wins!')
                else:
                    print('Player 2 Wins!')

                print()
                print_board(board)
                break
        else:
            p1_turn = not p1_turn


# play the game
game()
