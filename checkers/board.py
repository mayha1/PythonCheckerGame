import pygame 
from checkers.constants import WHITE, BLACK, LIGHTGREEN, DARKGREEN, NROWS, NCOLS, SQUARELENGTH
# from main import BOARDLIGHTCOLOR, BOARDDARKCOLOR

from checkers.pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.nWhitePieces = 0
        self.nBlackPieces = 0
        self.nWhiteKings = 0
        self.nBlackKings = 0
        self.intitializeBoard()    
        self.boardlightcolor = "darkolivegreen2"
        self.boarddarkcolor = "darkolivegreen4"
        
    def drawSquare(self, window):
        window.fill(self.boarddarkcolor)
        for row in range(NROWS):
            for col in range(NCOLS):
                if (row+col) % 2 == 0:
                    pygame.draw.rect(window, self.boardlightcolor, (col*SQUARELENGTH, row*SQUARELENGTH, SQUARELENGTH, SQUARELENGTH))
                else:
                    pass

    def intitializeBoard(self):
        for row in range(NROWS):
            self.board.append([])
            for col in range(NCOLS):
                if row < 3 and (row+col) % 2 != 0:
                    self.board[row].append(Piece(row, col, WHITE))
                    self.nWhitePieces += 1
                elif row >= NROWS-3  and (row+col) % 2 != 0:
                    self.board[row].append(Piece(row, col, BLACK))
                    self.nBlackPieces += 1
                else:
                    self.board[row].append(0)

    # def drawValidPieces(self, validPieces, window):
        # for piece in validPieces:
            # piece.drawMovability(window)

    def drawBoard(self, window, selected, validPieces):
        self.drawSquare(window) 
        for row in range(NROWS):
            for col in range(NCOLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.drawPiece(window)
        if selected != None:
            selected.drawValidMoves(window, validPieces) 

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