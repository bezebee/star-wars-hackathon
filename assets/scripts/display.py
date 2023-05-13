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

    def define_font(self, path, size):
        '''Define font'''
        return pygame.font.Font(path, size)

    def draw_text(self, text, font, text_color, x, y):
        '''Draw text'''
        image = font.render(text, True, text_color)
        self.screen.blit(image, (x, y))

    def draw_sprite(self, sprite):
        '''Draw sprite'''
        sprite.draw(self.screen)

    def draw_health_bar(self, bar):
        '''Draw health bar'''
        bar.draw(self.screen)

    def update(self):
        '''Update display'''
        pygame.display.flip()
