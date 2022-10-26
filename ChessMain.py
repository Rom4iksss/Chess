'''
This class is responsible for storing all the information about the current state of a chess game. It will also 
be responsible for determining the valid moves at the current state. It will also keep a move log.
'''

import pygame as p
import ChessEngine as CE


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animation later on
IMAGES = {}


def load_images():
    '''
    Initialize a global dictionary of images. This will be called exactly once in the main
    '''
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'
        
      
def main():
    '''
    The main driver for our code. This will handle user input and updating the graphics
    '''  
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = CE.GameState()
    valid_moves = gs.get_valid_moves()
    move_made = False #flag varible for whet a move is made
    
    load_images() #only do this once, before the while loop
    running = True
    sq_selected = () #no square is selected, keep track of the last click of the user (tuple: (row, col))
    player_clicks = [] #keep track of playeer clicks (two tuples: [(6, 4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x, y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col): #the user clicked the same square twice
                    sq_selected = () #deselect
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) #append for both 1st and 2nd clicks
                if len(player_clicks) == 2: #after 2nd click
                    move = CE.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                    sq_selected = () #reset user clicks
                    player_clicks = []  
            #key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undo_move() 
                    move_made = True
        
        if move_made:
            valid_moves = gs.get_valid_moves()
            move_made = False                 
                    
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    '''
    Responsible for all the graphics within a current game state.
    '''
    draw_board(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    draw_pieces(screen, gs.board) #draw pieces on top of those squares


def draw_board(screen):
    '''
    Draw the squares on the board.
    '''
    colors = [p.Color('white'), p.Color('light green')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col)%2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current game_state
'''      
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))    
        

if __name__ == '__main__':
    main()