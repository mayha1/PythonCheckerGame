import pygame 
from checkers.constants import WHITE, BLACK, LIGHTGREEN, DARKGREEN, NROWS, NCOLS, SQUARELENGTH

from checkers.pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.nWhitePieces = 12
        self.nBlackPieces = 12
        self.nWhiteKings = 0
        self.nBlackKings = 0
        self.intitializeBoard()        
        
    def drawSquare(self, window):
        window.fill(DARKGREEN)
        for row in range(NROWS):
            for col in range(NCOLS):
                if (row+col) % 2 == 0:
                    pygame.draw.rect(window, LIGHTGREEN, (col*SQUARELENGTH, row*SQUARELENGTH, SQUARELENGTH, SQUARELENGTH))
                else:
                    pass
    
    def intitializeBoard(self):     #TODO: use numpy array 0-->nan
        for row in range(NROWS):
            self.board.append([])
            for col in range(NCOLS):
                if row < 3 and (row+col) % 2 != 0:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row > 4 and (row+col) % 2 != 0:
                    self.board[row].append(Piece(row, col, BLACK))
                else:
                    self.board[row].append(0)  

    def drawBoard(self, window):
        self.drawSquare(window) 
        for row in range(NROWS):
            for col in range(NCOLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.drawPiece(window) 

    def getPiece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[row][col] = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = 0
        piece.row = row
        piece.col = col  

        if row == NROWS - 1 or row == 0:
            piece.makeKing()
            if piece.color == WHITE:
                self.nWhiteKings += 1
            else:
                self.nBlackKings += 1

    def getValidMoves(self, piece):     #output: tuple
        return 