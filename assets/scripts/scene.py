import pygame
from display import Display

class Scene:

    def __init__(self):
        self.title_img = pygame.image.load('assets/images/screens/game-start-v2.png')
        self.game_bg = pygame.image.load('assets/images/background/background_swamp.png')
        self.game_over = pygame.image.load('assets/images/screens/game-over.png')
