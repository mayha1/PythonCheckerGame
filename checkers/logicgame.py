import pygame
from checkers.constants import BLACK, WHITE, SQUARELENGTH
from checkers.board import Board

class Game:
    def __init__(self, window):
        self.window = window

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