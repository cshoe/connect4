import re
import sys

def get_vertical_strings(board):
    """ Get string representation of columns """
    column_strings = []
    for column in range(0, 7):
        column_string = ''
        for row in range(0, 6):
            column_string += board[row][column]
        column_strings.append(''.join(column_string))
    # print column_strings
    return column_strings


def get_horizontal_strings(board):
    """ Get string representation of rows """
    row_strings = []
    for row in board:
        row_strings.append(''.join(row))
    # print row_strings
    return row_strings


def get_diagonal_strings(board):
    """
    Get string representation of diagonal areas where a connect 4
    is possible.

    """
    d_strings = []


    d_strings = []
    for column in range(0, 7):
        row = 0
        _string = ''
        try:
            next_char = board[row][column]
        except IndexError:
            d_strings.extend(''.join(_string))
        else:
            _string += next_char
            row += 1

    for column in reversed(range(0, 7)):
        row = 0
        _string = ''
        try:
            next_char = board[row][column]
        except IndexError:
            d_strings.extend(''.join(_string))
        else:
            _string += next_char
            row += 1
    print d_strings
    return d_strings


def flatten_board(board):
    """
    Flatten JSON representation of a board. Return
    a list of 25 string that represent all ways that
    a connect 4 can happen.

    """
    strings = []
    strings.extend(get_vertical_strings(board))
    strings.extend(get_horizontal_strings(board))
    strings.extend(get_diagonal_strings(board))
    return strings


def find_winner(board):
    """ Find a winner of the game if there is one """
    strings = flatten_board(board)
    x_winner = re.compile('[X]{4}')
    o_winner = re.compile('[O]{4}')
    # print strings
    for string in strings:
        if string is not None and string is not []:
            # print string
            if x_winner.search(string) is not None:
                return 'Winner: X'
            elif o_winner.search(string) is not None:
                return 'Winner: 0'
    return 'No winner.'


if __name__ == '__main__':
    board = sys.stdin.read()
    print find_winner(eval(board))

