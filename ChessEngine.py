'''
This is main driver file. It will be responsible for handling user input and displaying the current GameState object.
'''

class GameState():
    def __init__(self) -> None:
        #board is an 8x* 2d list, each element of the list gas 2 characters.
        #The first character repr the color of the piece, 'b' or 'w'
        #The second character repr the type of the piece, 'K', 'Q', 'R', 'B', 'N' or 'p'
        #"--" - repr an empty space with no piec
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.white_to_move = True
        self.moveLog = []
        