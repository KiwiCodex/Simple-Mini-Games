import pygame

pygame.font.init()

# Window's dimensions
WIDTH = 800
HEIGHT = 600

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
H_FA2F2F = (255, 47, 47)

# Frames
FPS = 60

SCORE = 0
HIGHSCORE = 0

# Fonts
console_font = pygame.font.Font(pygame.font.match_font("consolas"), 25)
times_font = pygame.font.Font(pygame.font.match_font("times"), 50)
arial_font = pygame.font.Font(pygame.font.match_font("arial"), 80)
courier_font = pygame.font.Font(pygame.font.match_font("courier"), 30)