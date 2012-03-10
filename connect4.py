import re
import sys


def find_winner(board):
    for winner in ['X', 'O']:
        board_string = '\n'.join([''.join(row) for row in board])
        _regex = '({0[0]}[XO.\n]{{{0[1]}}}){{3}}{0[0]}'
        c_cnt = len(board[0])
        d_v_regexes = [_regex.format((winner, c_cnt + x)) for x in [-1, 0, 1]]
        d_v_regexes.append('{}{{4}}(.)*\n'.format(winner))
        for regex in d_v_regexes:
            if re.search(regex, board_string, re.DOTALL) is not None:
                return 'Winner: {}'.format(winner)
    return 'No winner.'

if __name__ == '__main__':
    print find_winner(eval(sys.stdin.read()))
