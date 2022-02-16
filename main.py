import pygame
import sys
from button import Button
from checkers.constants import WHITE, BLACK,  WIDTH, HEIGHT, SQUARELENGTH, BUTTONRECT, BOARDLIGHTCOLOR, BOARDDARKCOLOR, RULES
from checkers.game import Game

pygame.init()

FPS = 60     

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
        
def getFont(size): 
    return pygame.font.Font("assets/font.ttf", size)

def rule():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")
        RULESRECT = RULES.get_rect(center=(WIDTH//2, HEIGHT//2))
        window.blit(RULES, RULESRECT)
        
        BACKBUTTON = Button(image=None, pos=(WIDTH//2, 750), 
                            textInput="BACK", font=getFont(20), baseColor="white", hoveringColor="darkorange2")

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

def colorOptions():
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")

        GREENBUTTON = Button(image=None, pos=(WIDTH//2, HEIGHT//4), 
                            textInput="Dark Green and Light Green", font=getFont(20), baseColor="white", hoveringColor="green")
        BROWNBUTTON = Button(image=None, pos=(WIDTH//2, HEIGHT//2), 
                            textInput="Dark Brown and Light Brown", font=getFont(20), baseColor="white", hoveringColor="brown")
        BLUEBUTTON = Button(image=None, pos=(WIDTH//2, HEIGHT//4*3), 
                            textInput="Dark Blue and Light Blue", font=getFont(20), baseColor="white", hoveringColor="blue")
        
        for button in [GREENBUTTON, BROWNBUTTON, BLUEBUTTON]:
            button.changeColor(OPTIONSMOUSEPOS)
            button.update(window)

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

def showWinner(game):
    while True:
        OPTIONSMOUSEPOS = pygame.mouse.get_pos()

        window.fill("black")

        TEXT1 = getFont(20).render(f'Congratulation!', True, "white")
        RECT1 = TEXT1.get_rect(center=(WIDTH//2, 250))

        if game.winner == WHITE:
            winner = "white"
        elif game.winner == BLACK:
            winner = "black"
        else:
            winner = "nobody"
            
        TEXT2 = getFont(20).render(f'The winner is {winner}.', True, "white")
        RECT2 = TEXT2.get_rect(center=(WIDTH//2, 400))
        window.blit(TEXT1, RECT1)
        window.blit(TEXT2, RECT2)

        PLAYAGAINBUTTON = Button(image=None, pos=(WIDTH//2, 550), 
                            textInput="PLAY AGAIN", font=getFont(30), baseColor="white", hoveringColor="darkorange2")
        MENUBUTTON = Button(image=None, pos=(WIDTH//2, 700), 
                            textInput="MENU", font=getFont(30), baseColor="white", hoveringColor="darkorange2")

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
                if MENUBUTTON.checkForInput(OPTIONSMOUSEPOS):
                    mainMenu()
        pygame.display.update()

def mainMenu():
    BOARDDARKCOLOR = "darkolivegreen4"
    BOARDLIGHTCOLOR = "darkolivegreen2"

    while True:
        window.fill("black")
        MENUMOUSEPOS = pygame.mouse.get_pos()

        MENUTEXT = getFont(50).render("MAIN MENU", True, "darkorange2")
        MENURECT = MENUTEXT.get_rect(center=(WIDTH//2, HEIGHT//8))
        RULEBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, HEIGHT//16*5), 
                            textInput="RULE", font=getFont(30), baseColor="darkorange2", hoveringColor="White")
        PLAYBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, 400), 
                            textInput="PLAY", font=getFont(30), baseColor="darkorange2", hoveringColor="White")
        COLOROPTIONBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, HEIGHT//16*11), 
                            textInput="COLOR OPTIONS", font=getFont(30), baseColor="darkorange2", hoveringColor="White")
        QUITBUTTON = Button(image=BUTTONRECT, pos=(WIDTH//2, HEIGHT//16*14), 
                            textInput="QUIT", font=getFont(30), baseColor="darkorange2", hoveringColor="White")

        window.blit(MENUTEXT, MENURECT)

        for button in [RULEBUTTON, PLAYBUTTON, COLOROPTIONBUTTON, QUITBUTTON]:
            button.changeColor(MENUMOUSEPOS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULEBUTTON.checkForInput(MENUMOUSEPOS):
                    rule()
                if PLAYBUTTON.checkForInput(MENUMOUSEPOS):
                    startGame()
                if COLOROPTIONBUTTON.checkForInput(MENUMOUSEPOS):
                    colorOptions()
                if QUITBUTTON.checkForInput(MENUMOUSEPOS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

mainMenu()