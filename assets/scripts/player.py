"""Class to describe a player of this game"""
import pygame

class Player(pygame.sprite.Sprite) :
    """Describes a player in the fighting game"""

    def __init__(self, pos=None, color=None) -> None:
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill( color if color else "lightblue")
        self.rect = self.image.get_rect(center = pos if pos else (200,300))

    def player_input(self):
        """to handle all possible user input"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            # example how to handle jump
            pass
