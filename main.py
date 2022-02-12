import pygame
import sys
from button import Button
from checkers.constants import WHITE, BLACK,  WIDTH, HEIGHT, SQUARELENGTH, BUTTONRECT, NCOLS, NROWS, BOARDDARKCOLOR, BOARDLIGHTCOLOR
from checkers.board import Board
from checkers.pieces import Piece
from checkers.game import Game

pygame.init()

FPS = 60        #frames per second

window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers game")


def getRowColFromMousePosition(MOUSEPOS):
    col = MOUSEPOS[0] // SQUARELENGTH
    row = MOUSEPOS[1] // SQUARELENGTH
    return row, col

def startGame():
    global BOARDDARKCOLOR
    global BOARDLIGHTCOLOR
    clock = pygame.time.Clock()
    game = Game(window)
    game.board.changeBoardColor(BOARDDARKCOLOR, BOARDLIGHTCOLOR)
    running = True
    while running:
        clock.tick(FPS)
        game.board.drawBoard(window, game.selected, game.validMoves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                GAMEMOUSEPOS = pygame.mouse.get_pos()
                selectedRow, selectedCol = getRowColFromMousePosition(GAMEMOUSEPOS)
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
        OPTIONSRECT = OPTIONSTEXT.get_rect(center=(WIDTH//2, 260))
        window.blit(OPTIONSTEXT, OPTIONSRECT)

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

def colorOptions():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")

        GREENBUTTON = Button(image=None, pos=(WIDTH//2, 200), 
                            textInput="Dark Green and Light Green", font=get_font(20), baseColor="white", hoveringColor="green")
        BROWNBUTTON = Button(image=None, pos=(WIDTH//2, 400), 
                            textInput="Dark Brown and Light Brown", font=get_font(20), baseColor="white", hoveringColor="brown")
        BLUEBUTTON = Button(image=None, pos=(WIDTH//2, 600), 
                            textInput="Dark Blue and Light Blue", font=get_font(20), baseColor="white", hoveringColor="blue")

        GREENBUTTON.changeColor(OPTIONSMOUSEPOS)
        GREENBUTTON.update(window)
        BROWNBUTTON.changeColor(OPTIONSMOUSEPOS)
        BROWNBUTTON.update(window)
        BLUEBUTTON.changeColor(OPTIONSMOUSEPOS)
        BLUEBUTTON.update(window)

        global BOARDDARKCOLOR
        global BOARDLIGHTCOLOR

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GREENBUTTON.checkForInput(OPTIONSMOUSEPOS):
                    BOARDDARKCOLOR = "darkolivegreen4"
                    BOARDLIGHTCOLOR = "darkolivegreen2"
                    mainMenu()
                if BROWNBUTTON.checkForInput(OPTIONSMOUSEPOS):
                    BOARDDARKCOLOR = "tan3"
                    BOARDLIGHTCOLOR = "khaki2"
                    mainMenu()
                if BLUEBUTTON.checkForInput(OPTIONSMOUSEPOS):
                    BOARDDARKCOLOR = "lightblue4"
                    BOARDLIGHTCOLOR = "lightblue3"
                    mainMenu()
        pygame.display.update()

def options():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")

        OPTIONSTEXT = get_font(20).render("This is the OPTIONS screen.", True, "white")
        OPTIONSRECT = OPTIONSTEXT.get_rect(center=(WIDTH//2, 260))
        window.blit(OPTIONSTEXT, OPTIONSRECT)

        BACKBUTTON = Button(image=None, pos=(WIDTH//2, 460), 
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

def showWinner(game):
    while True:
            OPTIONSMOUSEPOS = pygame.mouse.get_pos()

            window.fill("black")

            TEXT1 = get_font(20).render(f'Congratulation!', True, "white")
            if game.winner == WHITE:
                winner = "white"
            elif game.winner == BLACK:
                winner = "black"
            else:
                winner = "nobody"
            TEXT2 = get_font(20).render(f'The winner is {winner}.', True, "white")
            RECT1 = TEXT1.get_rect(center=(WIDTH//2, 250))
            RECT2 = TEXT2.get_rect(center=(WIDTH//2, 400))
            window.blit(TEXT1, RECT1)
            window.blit(TEXT2, RECT2)

            PLAYAGAINBUTTON = Button(image=None, pos=(WIDTH//2, 550), 
                                textInput="PLAY AGAIN", font=get_font(30), baseColor="white", hoveringColor="darkorange2")
            MENUBUTTON = Button(image=None, pos=(WIDTH//2, 700), 
                                textInput="MENU", font=get_font(30), baseColor="white", hoveringColor="darkorange2")

            PLAYAGAINBUTTON.changeColor(OPTIONSMOUSEPOS)
            PLAYAGAINBUTTON.update(window)
            MENUBUTTON.changeColor(OPTIONSMOUSEPOS)
            MENUBUTTON.update(window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAYAGAINBUTTON.checkForInput(OPTIONSMOUSEPOS):
                        startGame()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENUBUTTON.checkForInput(OPTIONSMOUSEPOS):
                        mainMenu()
                

            pygame.display.update()

def mainMenu():
    BOARDDARKCOLOR = "darkolivegreen4"
    BOARDLIGHTCOLOR = "darkolivegreen2"

    while True:
        window.fill("black")

        MENUMOUSEPOS = pygame.mouse.get_pos()

        MENUTEXT = get_font(50).render("MAIN MENU", True, "darkorange2")
        MENURECT = MENUTEXT.get_rect(center=(WIDTH//2, 100))
        RULEBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 250), 
                            textInput="RULE", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        PLAYBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 350), 
                            textInput="PLAY", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        SIZEOPTIONBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 450), 
                            textInput="SIZE OPTION", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        COLOROPTIONBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 550), 
                            textInput="COLOR OPTION", font=get_font(30), baseColor="darkorange2", hoveringColor="White")
        QUITBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 650), 
                            textInput="QUIT", font=get_font(30), baseColor="darkorange2", hoveringColor="White")

        window.blit(MENUTEXT, MENURECT)

        for button in [RULEBUTTON, PLAYBUTTON, SIZEOPTIONBUTTON, COLOROPTIONBUTTON, QUITBUTTON]:
            button.changeColor(MENUMOUSEPOS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULEBUTTON.checkForInput(MENUMOUSEPOS):
                    options()
                if PLAYBUTTON.checkForInput(MENUMOUSEPOS):
                    startGame()
                if SIZEOPTIONBUTTON.checkForInput(MENUMOUSEPOS):
                    options()
                if COLOROPTIONBUTTON.checkForInput(MENUMOUSEPOS):
                    colorOptions()
                if QUITBUTTON.checkForInput(MENUMOUSEPOS):
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