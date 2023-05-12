"""Class to describe a player of this game"""
import pygame

class Player(pygame.sprite.Sprite) :
    """Describes a player in the fighting game
        Two player names are allowed
            "Luke Skywalker" - this will be Player 1
            "Darth Vader" - this will be Player 2
        In this way, depending on player name, different keys press events cause different moves 
    """

    def __init__(self, pos=None, color=None, name=None) -> None:
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill( color if color else "lightblue")
        self.rect = self.image.get_rect(center = pos if pos else (200,300))
        self.name= name

    def move(self, screen_width):
        """to handle motion of a player"""
        # to control the speed of the movement. If they move too fast or slow, change this value.
        player_speed = 10

        # these handle the change in position of the player, when the move() method is called
        delta_x = 0

        # get all keypresses
        key = pygame.key.get_pressed()

        # The movement depends now on the player name.
        # If Luke (Player 1), the "A" and "D" handle left and right
        # If his father (Player 2), the "Left" and "Right" handle left and right
        if self.name == "Luke Skywalker":
            if key[pygame.K_a]:
                delta_x = -player_speed
            if key[pygame.K_d]:
                delta_x = player_speed
        elif self.name == "Darth Vader":
            if key[pygame.K_LEFT]:
                delta_x = -player_speed
            if key[pygame.K_RIGHT]:
                delta_x = player_speed

        #ensure player stays on screen
        if self.rect.left + delta_x < 0:
            delta_x =  self.rect.left
        if self.rect.right + delta_x > screen_width:
            delta_x = screen_width - self.rect.right

        # update player position. 
        self.rect.centerx += delta_x
