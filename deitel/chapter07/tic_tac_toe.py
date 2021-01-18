# tic_tac_toe.py
"""Two Player, Two-Dimensional Tic-Tac-Toe"""

# import libraries
import numpy as np

board = np.full((3, 3), 'T')


def check_seq(seq):
    '''Checks if all elems of a sequence are equal'''
    return len(set(seq)) == 1


def get_diagonals(multidim):
    '''Get the diagonals from a 3 x 3 board'''
    f_diagonal = [multidim[0, 0], multidim[1, 1], multidim[2, 2]]
    s_diagonal = [multidim[2, 0], multidim[1, 1], multidim[0, 2]]

    return [f_diagonal, s_diagonal]


def check_win(multidim):
    '''Checks for a winning combination'''
    # check rows
    rows = all(list(map(check_seq, multidim)))
    # check columns
    columns = all(list(map(check_seq, multidim.T)))
    # check diagonals
    diagonals = any(list(map(check_seq, get_diagonals(multidim))))

    return rows or columns or diagonals
