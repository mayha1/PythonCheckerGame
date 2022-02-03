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
        self.validMoves = []    #array of tuple
        self.jumpMoves = []

    def changeTurn(self):
        if self.turn == WHITE: 
            self.turn = BLACK
        else: 
            self.turn = WHITE

    def checkTurn(self, piece):
        if piece.color == self.turn:
            return True 
        else:
            return False

    # def getValidMoves(self):

    # def getMovePermission(self, row, col):        
    #     piece = self.board.getPiece(row, col)
    #     if piece != 0 and self.checkTurn(piece) and (row, col) in self.validMoves:
    #         #check valid
    #         # self.board.move(self.selected, row, col)
    #         return True
    #     else: 
    #         return False


    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if result:
                self.changeTurn()
            else:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.getValidMoves(self.selected)

    def getValidMoves(self, piece):     #havent considered Kings
        rowMove = piece.row + piece.direction
        colLeftMove = piece.col - 1
        colRightMove = piece.col + 1
        if colLeftMove >= 0 and rowMove >= 0 and rowMove <= NROWS-1:
            leftSquare = self.board.getPiece(rowMove, colLeftMove)
            if leftSquare == 0:
                self.validMoves.append((rowMove, colLeftMove))
        if colRightMove <= NCOLS-1 and rowMove >= 0 and rowMove <= NROWS-1:
            rightSquare = self.board.getPiece(rowMove, colRightMove)
            if rightSquare == 0:
                self.validMoves.append((rowMove, colRightMove))



    def _move(self, row, col):
        newSquare = self.board.getPiece(row, col)
        if self.selected and newSquare == 0 and (row, col) in self.validMoves:
            self.board.move(self.selected, row, col)
            return True
        else:
            return False

    

# TODO: movePermission => select1/select again
#        => select2 => check able to move/ select again => move in main

    

    # def getJumpMoveLeft(self, piece):
    #     rowDoubleLeftPiece = piece.row + piece.direction*2
    #     colDoubleLeftPiece = piece.col - 2
    #     if rowDoubleLeftPiece >= 0 and rowDoubleLeftPiece <= NROWS-1 and colDoubleLeftPiece >=0: 
    #         leftPiece = self.board.getPiece(piece.row + piece.direction, piece.col - 1)
    #         if leftPiece == 0: 
    #             return {}
    #         else: 
    #             doubleLeftPiece = self.board.getPiece(rowDoubleLeftPiece, colDoubleLeftPiece)
    #             if doubleLeftPiece == 0:
    #                 return [(rowDoubleLeftPiece, colDoubleLeftPiece)]
    #             else:
    #                 return {}
    #     else:
    #         return {}

    # def getJumpMoveRight(self, piece):
    #     rowDoubleRightPiece = piece.row + piece.direction*2
    #     colDoubleRightPiece = piece.col + 2
    #     if rowDoubleRightPiece >= 0 and rowDoubleRightPiece <= NROWS-1 and colDoubleRightPiece <= NCOLS-1: 
    #         RightPiece = self.board.getPiece(piece.row + piece.direction, piece.col + 1)
    #         if RightPiece == 0: 
    #             return {}
    #         else: 
    #             doubleRightPiece = self.board.getPiece(rowDoubleRightPiece, colDoubleRightPiece)
    #             if doubleRightPiece == 0:
    #                 return [(rowDoubleRightPiece, colDoubleRightPiece)]
    #             else:
    #                 return {}
    #     else:
    #         return {}

    # def getJumpMoves(self):
    #     self.jumpMoves = {}
    #     for row in range(NROWS):
    #         for col in range(NCOLS):
    #             piece = self.board.getPiece(row, col)
    #             if piece != 0:
    #                 self.jumpMoves = self.jumpMoves.add(self.getJumpMoveLeft(piece), self.getJumpMoveRight(piece))
         

        



    # def checkValid(self, piece, row, col):
    #     if self.board.getPiece(row, col) != 0:
    #         return False
    #     else:
    #         if piece.color != self.turn:
    #             return False
    #         else:
    #             if self.board.getPiece(piece.row + piece.direction, pi )



    # # def checkTarget(self, row, col)
    # def checkValid(self, row, col):
    #     if self.board[row][col] == 0:
    #         pass
    #     else: 
    #         selectedPiece = self.board[row][col]
    #         if 

    


    # select --> piece or not ---> if piece --> possible to move ---> possible move  
    #                                           imposs --> pass
    # (row, col, black) --> move when * (row-1,col-1) == 0 or (row -1,col+1)
    #                                 * (row-1,col-1) != 0 and (row-2,col-2)== 0
    #                                 * (row-1,col+1) != 0 and (row+2,col-2)== 0