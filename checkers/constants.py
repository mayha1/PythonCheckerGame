import pygame

WIDTH, HEIGHT = 800, 800
NROWS = NCOLS = 8
SQUARELENGTH = WIDTH//NCOLS

BUTTONRECT = pygame.image.load("assets/buttonrect.png")
BUTTONRECT = pygame.transform.scale(BUTTONRECT, (500, 80))
RULES = pygame.image.load("assets/rules.png")
RULES = pygame.transform.scale(RULES, (700, 600))
WHITE = "white"
BLACK = "black"
YELLOW = "yellow"
SUGGESTMOVECOLOR = "lemonchiffon3"
BOARDDARKCOLOR = "darkolivegreen4"
BOARDLIGHTCOLOR = "darkolivegreen2"