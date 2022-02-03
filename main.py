import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARELENGTH
from checkers.board import Board
from checkers.pieces import Piece
from checkers.game import Game

FPS = 60        #frames per second

window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers game")

# pygame.display.flip()

clock = pygame.time.Clock()
# board = Board()
game = Game(window)

running = True

def getRowColFromMousePosition(mousePostion):
    col = mousePostion[0] // SQUARELENGTH
    row = mousePostion[1] // SQUARELENGTH
    return row, col


sellectedPiece = 0
while running:
    clock.tick(FPS)
    game.board.drawBoard(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            selectedRow, selectedCol = getRowColFromMousePosition(mousePosition)
            game.select(selectedRow, selectedCol)


        pygame.display.update()

# TODO 1: endgame?
# TODO 2: Kings?
# TODO 3: jumps >=2
# TODO 4: if able to jump => compulsory
# TODO 5: visualize valid moves
# TODO 6: start: choose color, size, first turn
# TODO 7: replay and ratio 

# https://xkcd.com/color/rgb/
# https://github.com/github/gitignore/blob/main/Python.gitignore