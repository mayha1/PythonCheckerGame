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
            if sellectedPiece == 0:
                sellectedPiece = game.board.getPiece(selectedRow, selectedCol)

            else:
                targetRow = selectedRow
                targetCol = selectedCol
                game.getJumpMoves()
                print(game.jumpMoves)
                #checkTarget
                game.board.move(sellectedPiece, targetRow, targetCol)
                sellectedPiece = 0
                


        pygame.display.update()

# https://xkcd.com/color/rgb/
# https://github.com/github/gitignore/blob/main/Python.gitignore