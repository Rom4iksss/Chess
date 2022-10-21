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
        
        clock.tick(MAX_FPS)
        p.display.flip()
    
if __name__ == '__main__':
    main()