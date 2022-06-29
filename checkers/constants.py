import pygame
import pyautogui

widthScreen, heightScreen= pyautogui.size()
standardSize = heightScreen//10*8
WIDTH, HEIGHT = standardSize, standardSize
NROWS = NCOLS = 8
SQUARELENGTH = WIDTH//NCOLS

BIGFONTSIZE = standardSize//80*3
SMALLFONTSIZE = standardSize//80*2

BUTTONRECT = pygame.image.load("assets/buttonrect.png")
BUTTONRECT = pygame.transform.scale(BUTTONRECT, (WIDTH//8*5, HEIGHT//10))
RULES = pygame.image.load("assets/rules.png")
RULES = pygame.transform.scale(RULES, (WIDTH//8*7, WIDTH//8*6))
WHITE = "white"
BLACK = "black"
YELLOW = "yellow"
SUGGESTMOVECOLOR = "lemonchiffon3"
BOARDDARKCOLOR = "darkolivegreen4"
BOARDLIGHTCOLOR = "darkolivegreen2"