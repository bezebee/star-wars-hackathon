import pygame
from display import Display

class Scene:

    def __init__(self):
        alpha = 128
        self.title_img = pygame.image.load('assets/images/screens/game-start-v2.png')
        self.game_bg = pygame.image.load('assets/images/background/background_swamp.png')
        self.game_over = pygame.image.load('assets/images/screens/game-over.png')
        self.options_menu = pygame.image.load('assets/images/screens/how-to-play.png')

        self.game_over = pygame.image.load('assets/images/screens/game-over.png')
        self.game_over = pygame.transform.scale(self.game_over, (640, 480))
        self.game_over.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
