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
            ['--', '--', 'bQ', '--', '--', 'wQ', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.move_functions = {'p': self.get_pawn_moves, 'R': self.get_rook_moves, 'N': self.get_knight_moves,
                               'B': self.get_bishop_moves, 'Q': self.get_queen_moves, 'K': self.get_king_moves}
        
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
                    self.move_functions[piece](row, col, moves)
        return moves
                        
                        
    def get_pawn_moves(self, row, col, moves):
        '''
        Get all the pawn moves for the pawn located at row, col and add these moves to the list
        '''
        if self.white_to_move: #white pawn moves
            if self.board[row-1][col] == '--': #1 square pawn advance
                moves.append(Move((row, col), (row-1, col), self.board))
                if row == 6 and self.board[row-2][col] == '--': #2 square pawn advance
                    moves.append(Move((row, col), (row-2, col), self.board))
            if col-1 >= 0: #captures to the left
                if self.board[row-1][col-1][0] == 'b': #anemy piece to capture
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if col+1 <= 7: #captures to the right
                if self.board[row-1][col+1][0] == 'b': #enemy piece to capture
                    moves.append(Move((row, col), (row-1, col+1), self.board))
        else:
            if row+1 < len(self.board):
                if self.board[row+1][col] == '--': #1 square pawn advance
                    moves.append(Move((row, col), (row+1, col), self.board))
                    if row == 1 and self.board[row+2][col] == '--': #2 square pawn advance
                        moves.append(Move((row, col), (row+2, col), self.board))
                if col-1 >= 0: #captures to the left
                    if self.board[row+1][col-1][0] == 'w': #anemy piece to capture
                        moves.append(Move((row, col), (row+1, col-1), self.board))
                if col+1 <= 7: #captures to the right
                    if self.board[row+1][col+1][0] == 'w': #enemy piece to capture
                        moves.append(Move((row, col), (row+1, col+1), self.board))
                           
                
    def get_rook_moves(self, row, col, moves):
        '''
        Get all the rook moves for the rook located at row, col and add these moves to the list
        '''
        move = ['w', 'b'][self.white_to_move] #for captures (if True white moves and black could be captured)
        new_row = row #for not to change start row position in while
        while new_row+1 < len(self.board): #row moving
            new_row += 1
            if self.board[new_row][col] != '--':
                if self.board[new_row][col][0] == move:
                    moves.append(Move((row, col), (new_row, col), self.board))
                break
            moves.append(Move((row, col), (new_row, col), self.board))
        new_row = row #update new row
        while new_row-1 >= 0: #row moving
            new_row -= 1
            if self.board[new_row][col] != '--':
                if self.board[new_row][col][0] == move:
                    moves.append(Move((row, col), (new_row, col), self.board))
                break
            moves.append(Move((row, col), (new_row, col), self.board))   
            
        new_col = col #for not to change start col position in while
        while new_col+1 < len(self.board): #col moving
            new_col += 1
            if self.board[row][new_col] != '--':
                if self.board[row][new_col][0] == move:
                    moves.append(Move((row, col), (row, new_col), self.board))
                break
            moves.append(Move((row, col), (row, new_col), self.board))
        new_col = col #update new col
        while new_col-1 >= 0: #col moving
            new_col -= 1
            if self.board[row][new_col] != '--':
                if self.board[row][new_col][0] == move:
                    moves.append(Move((row, col), (row, new_col), self.board))
                break
            moves.append(Move((row, col), (row, new_col), self.board))   
        


    def get_knight_moves(self, row, col, moves):
        '''
        Get all the knight moves for the knight located at row, col and add these moves to the list
        '''
        pass
    

    def get_bishop_moves(self, row, col, moves):
        '''
        Get all the bishop moves for the bishop located at row, col and add these moves to the list
        '''
        move = ['w', 'b'][self.white_to_move] #for captures (if True white moves and black could be captured)
        new_row = row #for not to change start row position in while
        new_col = col #for not to change start col position in while
        while new_row+1 < len(self.board) and new_col+1 < len(self.board): 
            new_row += 1
            new_col += 1
            if self.board[new_row][new_col] != '--':
                if self.board[new_row][new_col][0] == move:
                    moves.append(Move((row, col), (new_row, new_col), self.board))
                break
            moves.append(Move((row, col), (new_row, new_col), self.board))
        new_row = row #update new row
        new_col = col #update new col
        while new_row-1 >= 0 and new_col-1 >= 0: 
            new_row -= 1
            new_col -= 1
            if self.board[new_row][new_col] != '--':
                if self.board[new_row][new_col][0] == move:
                    moves.append(Move((row, col), (new_row, new_col), self.board))
                break
            moves.append(Move((row, col), (new_row, new_col), self.board)) 
              
        new_row = row #for not to change start row position in while
        new_col = col #for not to change start col position in while
        while new_col+1 < len(self.board) and new_row-1 >= 0: 
            new_col += 1
            new_row -= 1
            if self.board[new_row][new_col] != '--':
                if self.board[new_row][new_col][0] == move:
                    moves.append(Move((row, col), (new_row, new_col), self.board))
                break
            moves.append(Move((row, col), (new_row, new_col), self.board))
        new_row = row #update new row
        new_col = col #update new col
        while new_col-1 >= 0 and new_row+1 < len(self.board): 
            new_col -= 1
            new_row += 1
            if self.board[new_row][new_col] != '--':
                if self.board[new_row][new_col][0] == move:
                    moves.append(Move((row, col), (new_row, new_col), self.board))
                break
            moves.append(Move((row, col), (new_row, new_col), self.board)) 
        
    
    def get_queen_moves(self, row, col, moves):
        '''
        Get all the queen moves for the queen located at row, col and add these moves to the list
        '''
        self.get_rook_moves(row, col, moves)
        self.get_bishop_moves(row, col, moves)


    def get_king_moves(self, row, col, moves):
        '''
        Get all the king moves for the king located at row, col and add these moves to the list
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
    
    
    
    
    
    
    
    
    
    
    