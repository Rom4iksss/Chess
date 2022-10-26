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
        self.move_log = []
    
    
   
    def make_move(self, move):
        '''
        Takes a Move as a parameter and executes it (this will not work for castling. pawn promotion, and en-passant)
        ''' 
        self.board[move.start_row][move.start_col] = '--'
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move) #log the move so we can undo it later
        self.white_to_move = not self.white_to_move #swap players
    
    
    def undo_move(self):
        '''
        Undo the last move made
        '''
        if len(self.move_log): #make sure that there is a move to undo
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move #switch turns back
            
    
    def get_valid_moves(self):
        '''
        All moves considering checks
        '''
        return self.get_all_possible_moves()
    
    
    def get_all_possible_moves(self):
        '''
        All moves without considering checks
        '''
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0] #represent color of the piece
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.get_pawn_moves(row, col, moves)
                    elif piece == 'R':
                        self.get_rook_moves(row, col, moves)
        return moves
                        
                        
    def get_pawn_moves(self, row, col, moves):
        '''
        Get all the pawn moves for the pawn located at row, col and add these moves to the list
        '''
        pass

    def get_rook_moves(self, row, col, moves):
        '''
        Get all the rook moves for the rook located at row, col and add these moves to the list
        '''
        pass
    
    
class Move():
    # maps keys to values
    # key : value
    ranks_to_rows = {'1': 7, '2': 6, '3': 5, '4': 4,
                     '5': 3, '6': 2, '7': 1, '8': 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                     'e': 4, 'f': 5, 'g': 6, 'h': 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()} 
    
    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row*1000 + self.start_col*100 + self.end_row*10 + self.end_col
        

    def __eq__(self, other):
        '''
        Overriding the equals method 
        '''
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        # you can add to make this like real chesss notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)
    
    
    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
    
    
    
    
    
    
    
    
    
    
    