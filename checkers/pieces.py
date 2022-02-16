import pygame
from checkers.constants import SQUARELENGTH, WHITE, BLACK, YELLOW, SUGGESTMOVECOLOR

class Piece:
    def __init__(self, row, col, color):
        self.board = []
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == WHITE:
            self.direction = [(1,-1), (1,1)]
        else:                  
            self.direction = [(-1,-1), (-1,1)]

    def getPosition(self):
        self.xCenter = self.col*SQUARELENGTH + SQUARELENGTH//2
        self.yCenter = self.row*SQUARELENGTH + SQUARELENGTH//2
    
    def makeKing(self):
        self.king = True
        self.direction = [(-1,-1), (-1,1), (1,-1), (1,1)]

    def drawPiece(self, window):
        self.getPosition()
        pieceRadius = SQUARELENGTH//3
        if self.king:
            pygame.draw.circle(window, YELLOW, (self.xCenter, self.yCenter), pieceRadius, pieceRadius//6)
            pygame.draw.circle(window, self.color, (self.xCenter, self.yCenter), pieceRadius-pieceRadius//6)
        else:
            pygame.draw.circle(window, self.color, (self.xCenter, self.yCenter), pieceRadius)

    def drawMovability(self, window):
        self.getPosition()
        pieceRadius = SQUARELENGTH//3
        if self.king:
            pygame.draw.circle(window, SUGGESTMOVECOLOR, (self.xCenter, self.yCenter), pieceRadius, pieceRadius//6)


    def drawValidMoves(self, window, validMoves):
        validMoveRadius = SQUARELENGTH // 5
        for move in validMoves:
            xMove = move[1]*SQUARELENGTH + SQUARELENGTH//2
            yMove = move[0]*SQUARELENGTH + SQUARELENGTH//2
            pygame.draw.circle(window, SUGGESTMOVECOLOR, (xMove, yMove), validMoveRadius)

    def move(self, row, col):
        self.row = row
        self.col = col 
        self.getPosition()