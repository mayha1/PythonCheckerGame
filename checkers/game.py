# from ast import While
# from tabnanny import check
import pygame
from pyparsing import White
from checkers.constants import BLACK, NCOLS, NROWS, WHITE, SQUARELENGTH
from checkers.board import Board
from checkers.pieces import Piece

class Game:
    def __init__(self, window):
        self.window = window
        self.board = Board()
        self.turn = WHITE
        self.selected = None
        self.validPieces = set([])
        self.validMoves = set([])    #set of tuples
        self.jumping = False
        self.canJump = False
        self.winner = None

    def changeTurn(self):
        if self.turn == WHITE: 
            self.turn = BLACK
        else: 
            self.turn = WHITE
        self.selected = None
        self.validMoves = set([])
        self.jumping = False
        


    def checkWinner(self):
        if self.validPieces == set() and not self.jumping:
            if self.turn == WHITE:
                self.winner = BLACK
            if self.turn == BLACK:
                self.winner = WHITE


    def getValidPieces(self):
        jumpPieces = set([])
        validPieces = set([])
        for row in range(NROWS):
            for col in range(NCOLS):
                piece = self.board.getPiece(row, col)
                if piece != 0 and piece.color == self.turn:
                    walkMoves = self.getWalkMoves(piece)
                    jumpMoves = self.getJumpMoves1step(piece)
                    validMoves = set.union(walkMoves, jumpMoves)
                    if jumpMoves != set([]):
                        jumpPieces.add(piece)
                    if validMoves != set([]):
                        validPieces.add(piece)
        if jumpPieces != set([]):
            validPieces = jumpPieces
            self.canJump = True
        else:
            self.canJump = False
        return validPieces

    def select(self, row, col):
        # self.checkWinner()
        if self.selected:
            result = self._move(row, col)
            if result:
                #if jump => check jump again?
                if self.canJump:
                    self.jumping = True
                    piece = self.board.getPiece(row, col)
                    self.validMoves = self.getJumpMoves1step(piece)
                    if self.validMoves != set([]):
                        self.validPieces = set([piece])
                        self.selected = self.board.getPiece(row, col)
                    else:
                        self.changeTurn()
                else:
                    self.changeTurn()
            else:
                if not self.jumping:
                    self.selected = None
                    self.checkWinner()                 
                    self.select(row, col)
                    
        else:
            self.validPieces = self.getValidPieces()
            if self.jumping:
                pass
            else:
                piece = self.board.getPiece(row, col)
                if piece != 0 and piece.color == self.turn and piece in self.validPieces:
                    self.selected = piece
                    self.getValidMoves(self.selected)
        
        self.checkWinner()
                
    def getValidMoves(self, piece):
        if self.canJump:
            self.validMoves = self.getJumpMoves1step(piece)
        else:
            self.validMoves = set.union(self.getWalkMoves(self.selected),\
                         self.getJumpMoves1step(self.selected))

    def getWalkMoves(self, piece):
        walkMoves = set([])
        for direction in piece.direction:
            rowMove = piece.row + direction[0]
            colMove = piece.col + direction[1]
            if rowMove >= 0 and rowMove <= NROWS-1 \
                    and colMove >= 0 and colMove <= NCOLS-1:
                leftSquare = self.board.getPiece(rowMove, colMove)
                if leftSquare == 0:
                    walkMoves.add((rowMove, colMove))
        return walkMoves

    def _move(self, row, col):
        newSquare = self.board.getPiece(row, col)
        if self.selected and newSquare == 0 and (row, col) in self.validMoves:
            if self.canJump:
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

    def getJumpMoves1step(self, piece):
        jumpMoves = set([])
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
                        jumpMoves.add((rowJump, colJump))
                    else:
                        pass
            else:
                pass
        return jumpMoves

