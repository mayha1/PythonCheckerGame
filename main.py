import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.pieces import Piece

FPS = 60        #frames per second

window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers game")

# pygame.display.flip()

clock = pygame.time.Clock()
board = Board()

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    
    board.drawBoard(window)
    

    pygame.display.update()

# https://xkcd.com/color/rgb/
# https://github.com/github/gitignore/blob/main/Python.gitignore
# numpy homogeneous type