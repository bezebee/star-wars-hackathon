'''Holds the display functionality'''
import pygame

class Display:
    '''A class that handles display related actions'''
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

    def load_image(self, path, size=None):
        '''load and scale background image'''
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        return image

    def draw_background(self, image):
        '''Draw background'''
        self.screen.blit(image, (0, 0))

    def draw_sprite(self, sprite):
        '''Draw sprite'''
        sprite.draw(self.screen)

    def draw_health_bar(self, healthbar):
        '''Draw health bar'''
        healthbar.draw(self.screen)

    def update(self):
        '''Update display'''
        pygame.display.flip()
