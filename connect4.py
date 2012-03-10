import re, sys

def find_winner(board):
    column_count = len(board[0])
    winners = ['X', 'O']
    for winner in winners:
        h_regex = '{}{{4}}'.format(winner)
        for row in board:
            if re.search(h_regex, ''.join(row)) is not None:
                return 'Winner: {}'.format(winner)
        board_string = ''.join([''.join(row) for row in board])
        d_v_regexes = ['({0[0]}[XO.]{{{0[1]}}}){{3}}{0[0]}'.\
            format((winner, column_count+x)) for x in [-2, -1, 0]]
        for regex in d_v_regexes:
            if re.search(regex, board_string) is not None:
                return 'Winner: {}'.format(winner)
    return 'No winner.'

if __name__ == '__main__':
    print find_winner(eval(sys.stdin.read()))
