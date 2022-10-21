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

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def load_images():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'
        
'''
The main driver for our code. This will handle user input and updating the graphics
'''        
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = CE.GameState()
    load_images() #only do this once, before the while loop
    running = True   
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state.
'''
def draw_game_state(screen, gs):
    draw_board(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    draw_pieces(screen, gs.board) #draw pieces on top of those squares

'''
Draw the squares on the board.
'''
def draw_board(screen):
    colors = [p.Color('white'), p.Color('light green')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current game_state
'''      
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))    
        

if __name__ == '__main__':
    main()