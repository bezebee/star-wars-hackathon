"""Class to describe a player of this game"""
import pygame

class Player(pygame.sprite.Sprite) :
    """Describes a player in the fighting game"""

    def __init__(self, pos=None, color=None) -> None:
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill( color if color else "lightblue")
        self.rect = self.image.get_rect(center = pos if pos else (200,300))
        self.pos = pos

    def move(self): 
        """to handle motion of a player"""
        # to control the speed of the movement. If they move too fast or slow, change this value.
        SPEED = 10 

        # these handle the change in position of the player, when the move() method is called
        delta_x = 0

        # get all keypresses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            delta_x = -SPEED
        if key[pygame.K_d]:
            delta_x = SPEED

        # update player position
        self.rect.centerx += delta_x
