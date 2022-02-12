import pygame
import sys
from button import Button
from checkers.constants import WIDTH, HEIGHT, SQUARELENGTH
from checkers.board import Board
from checkers.pieces import Piece
from checkers.game import Game

pygame.init()

FPS = 60        #frames per second

window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers game")

BOARDCOLOR1 = ""

def getRowColFromMousePosition(mousePostion):
    col = mousePostion[0] // SQUARELENGTH
    row = mousePostion[1] // SQUARELENGTH
    return row, col

def startGame():
    clock = pygame.time.Clock()
    game = Game(window)
    running = True
    while running:
        clock.tick(FPS)
        game.board.drawBoard(window, game.selected, game.validMoves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                selectedRow, selectedCol = getRowColFromMousePosition(mousePosition)
                game.select(selectedRow, selectedCol)
                if game.winner != None:
                    running = False
        pygame.display.update()

    showWinner(game)
        
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def rule():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("white")

        OPTIONSTEXT = get_font(30).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONSTEXT.get_rect(center=(WIDTH//2, 260))
        window.blit(OPTIONSTEXT, OPTIONS_RECT)

        BUTTTONBACK = Button(image=None, pos=(WIDTH//2, 460), 
                            textInput="BACK", font=get_font(30), baseColor="Black", hoveringColor="Green")

        BUTTTONBACK.changeColor(OPTIONSMOUSEPOS)
        BUTTTONBACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTTONBACK.checkForInput(OPTIONSMOUSEPOS):
                    mainMenu()

        pygame.display.update()

def options():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")

        OPTIONSTEXT = get_font(20).render("This is the OPTIONS screen.", True, "white")
        OPTIONS_RECT = OPTIONSTEXT.get_rect(center=(WIDTH//2, 260))
        window.blit(OPTIONSTEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(WIDTH//2, 460), 
                            textInput="BACK", font=get_font(30), baseColor="white", hoveringColor="darkorange2")

        OPTIONS_BACK.changeColor(OPTIONSMOUSEPOS)
        OPTIONS_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONSMOUSEPOS):
                    mainMenu()

        pygame.display.update()

def showWinner(game):
    while True:
            OPTIONSMOUSEPOS = pygame.mouse.get_pos()

            window.fill("black")

            TEXT1 = get_font(20).render(f'Congratulation!', True, "white")
            TEXT2 = get_font(20).render(f'The winner is {game.winner}', True, "white")
            RECT1 = TEXT1.get_rect(center=(WIDTH//2, 250))
            RECT2 = TEXT2.get_rect(center=(WIDTH//2, 400))
            window.blit(TEXT1, RECT1)
            window.blit(TEXT2, RECT2)

            BACKBUTTON = Button(image=None, pos=(WIDTH//2, 550), 
                                textInput="BACK", font=get_font(30), baseColor="white", hoveringColor="darkorange2")

            BACKBUTTON.changeColor(OPTIONSMOUSEPOS)
            BACKBUTTON.update(window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACKBUTTON.checkForInput(OPTIONSMOUSEPOS):
                        mainMenu()

            pygame.display.update()

def mainMenu():
    while True:
        window.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENUTEXT = get_font(50).render("MAIN MENU", True, "darkorange2")
        MENURECT = MENUTEXT.get_rect(center=(WIDTH//2, 100))

        RULEBUTTON = Button(image=pygame.image.load("assets/buttonrect.png"), pos=(WIDTH//2, 250), 
                            textInput="RULE", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        PLAYBUTTON = Button(image=pygame.image.load("assets/buttonrect.png"), pos=(WIDTH//2, 400), 
                            textInput="PLAY", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        OPTIONSBUTTON = Button(image=pygame.image.load("assets/buttonrect.png"), pos=(WIDTH//2, 550), 
                            textInput="OPTIONS", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        QUITBUTTON = Button(image=pygame.image.load("assets/buttonrect.png"), pos=(WIDTH//2, 700), 
                            textInput="QUIT", font=get_font(30), baseColor="darkorange2", hoveringColor="White")

        window.blit(MENUTEXT, MENURECT)

        for button in [RULEBUTTON, PLAYBUTTON, OPTIONSBUTTON, QUITBUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULEBUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if PLAYBUTTON.checkForInput(MENU_MOUSE_POS):
                    startGame()
                if OPTIONSBUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUITBUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

mainMenu()



#  1: endgame?
#  2: Kings?
#  3: jumps >=2
#  4: if able to jump => compulsory
#  5: visualize valid moves
# TODO 6: start: choose color, size, first turn
# TODO 7: replay and ratio 
# TODO 8: visualize valid piece

# https://xkcd.com/color/rgb/
# https://github.com/github/gitignore/blob/main/Python.gitignore