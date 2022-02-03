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
        rowMove = piece.row + piece.direction
        colLeftMove = piece.col - 1
        colRightMove = piece.col + 1
        if rowMove >= 0 and rowMove <= NROWS-1 and colLeftMove >= 0:
            leftSquare = self.board.getPiece(rowMove, colLeftMove)
            if leftSquare == 0:
                self.validMoves.append((rowMove, colLeftMove))
        if rowMove >= 0 and rowMove <= NROWS-1 and colRightMove <= NCOLS-1:
            rightSquare = self.board.getPiece(rowMove, colRightMove)
            if rightSquare == 0:
                self.validMoves.append((rowMove, colRightMove))



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

    

# TODO: movePermission => select1/select again
#        => select2 => check able to move/ select again => move in main

    

    def getJumpMoves(self, piece):
        rowJump = piece.row + piece.direction*2
        colLeftJump = piece.col - 2
        colRightJump = piece.col + 2

        if rowJump >= 0 and rowJump <= NROWS-1 and colLeftJump >=0: 
            leftPiece = self.board.getPiece(piece.row + piece.direction, piece.col - 1)
            if leftPiece == 0:
                pass
            elif leftPiece.color == self.turn:
                pass
            else: 
                jumpSquare = self.board.getPiece(rowJump, colLeftJump)
                if jumpSquare == 0:
                    self.validMoves.append((rowJump, colLeftJump))
                    self.jumpMoves.append((rowJump, colLeftJump))
                else:
                    pass
        else:
            pass

        if rowJump >= 0 and rowJump <= NROWS-1 and colRightJump <= NCOLS-1: 
            rightPiece = self.board.getPiece(piece.row + piece.direction, piece.col + 1)
            if rightPiece == 0:
                pass
            elif rightPiece.color == self.turn:
                pass
            else: 
                jumpSquare = self.board.getPiece(rowJump, colRightJump)
                if jumpSquare == 0:
                    self.validMoves.append((rowJump, colRightJump))
                    self.jumpMoves.append((rowJump, colRightJump))
                else:
                    pass
        else:
            pass



    # select --> piece or not ---> if piece --> possible to move ---> possible move  
    #                                           imposs --> pass
    # (row, col, black) --> move when * (row-1,col-1) == 0 or (row -1,col+1)
    #                                 * (row-1,col-1) != 0 and (row-2,col-2)== 0
    #                                 * (row-1,col+1) != 0 and (row+2,col-2)== 0