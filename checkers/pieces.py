import pygame
from checkers.constants import SQUARELENGTH, NCOLS, NROWS, WHITE, BLACK, YELLOW

class Piece:
    def __init__(self, row, col, color):
        self.board = []
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == WHITE:
            self.direction = 1
        else: # self.color == BLACK                   
            self.direction = -1

    def getPosition(self):
        self.xCenter = self.col*SQUARELENGTH + SQUARELENGTH//2
        self.yCenter = self.row*SQUARELENGTH + SQUARELENGTH//2
    
    def makeKing(self):
        self.king = True
        self.direction = (-1,1)

    def drawPiece(self, window):
            self.getPosition()
            pieceRadius = SQUARELENGTH//3
            if self.king:
                pygame.draw.circle(window, YELLOW, (self.xCenter, self.yCenter), pieceRadius, pieceRadius//6)
                pygame.draw.circle(window, self.color, (self.xCenter, self.yCenter), pieceRadius-pieceRadius//6)
            else:
                pygame.draw.circle(window, self.color, (self.xCenter, self.yCenter), pieceRadius)

    def move(self, row, col):
        self.row = row
        self.col = col 
        self.getPosition()

    

