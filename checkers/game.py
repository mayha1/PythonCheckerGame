from ast import While
from tabnanny import check
import pygame
from checkers.constants import BLACK, NCOLS, NROWS, WHITE, SQUARELENGTH
from checkers.board import Board
from checkers.pieces import Piece

class Game:
    def __init__(self, window):
        self.window = window
        self.board = Board()
        self.turn = WHITE
        self.selected = None 
        self.validMoves = []    #array of tuples
        self.jumpMoves = []

    def changeTurn(self):
        if self.turn == WHITE: 
            self.turn = BLACK
        else: 
            self.turn = WHITE

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if result:
                self.changeTurn()
                self.validMoves = []
            else:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.getWalkMoves(self.selected)
                self.getJumpMoves(self.selected)

    def getWalkMoves(self, piece):     #havent considered Kings
        for direction in piece.direction:
            rowMove = piece.row + direction[0]
            colMove = piece.col + direction[1]
            if rowMove >= 0 and rowMove <= NROWS-1 \
                    and colMove >= 0 and colMove <= NCOLS-1:
                leftSquare = self.board.getPiece(rowMove, colMove)
                if leftSquare == 0:
                    self.validMoves.append((rowMove, colMove))

    def _move(self, row, col):
        newSquare = self.board.getPiece(row, col)
        if self.selected and newSquare == 0 and (row, col) in self.validMoves:
            if (row, col) in self.jumpMoves:
                rowEatenPiece = (self.selected.row + row) // 2 
                colEatenPiece = (self.selected.col + col) // 2 
                self.board.board[rowEatenPiece][colEatenPiece] = 0
                if self.turn == WHITE:
                    self.board.nBlackPieces -= 1
                else:
                    self.board.nWhitePieces -= 1
            self.board.move(self.selected, row, col)            
            return True
        else:
            return False

    def getJumpMoves(self, piece):
        for direction in piece.direction:
            rowJump = piece.row + direction[0]*2
            colJump = piece.col + direction[1]*2
            if rowJump >= 0 and rowJump <= NROWS-1 \
                    and colJump >=0 and colJump <= NCOLS-1: 
                leftPiece = self.board.getPiece(piece.row + direction[0], piece.col + direction[1])
                if leftPiece == 0:
                    pass
                elif leftPiece.color == self.turn:
                    pass
                else: 
                    jumpSquare = self.board.getPiece(rowJump, colJump)
                    if jumpSquare == 0:
                        self.validMoves.append((rowJump, colJump))
                        self.jumpMoves.append((rowJump, colJump))
                    else:
                        pass
            else:
                pass