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
        """
        is_jumping : this variable ensures that jump button has no effect
                     while jumping to avoid double jumps
        attack_type : this variable stores the attack type that was used by the player.
                       currently 0 means not attack, 1 means standard sabre attack 
                       (for now just one attack)
        """
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill( color if color else "lightblue")
        self.rect = self.image.get_rect(center = pos if pos else (200,300))
        self.name= name
        self.velocity_y = 0
        self.is_jumping = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, surface, target):
        """to handle motion of a player"""
        # to control the speed of the movement. If they move too fast or slow, change this value.
        player_speed = 10

        # add gravity so that player falls down to his position after jumping up
        gravity = 2

        # this is to define the ground level of the players
        # (currently 110 pixels above the screen bottom)
        bottom_level = 110

        # these handle the change in position of the player, when the move() method is called
        delta_x = 0
        delta_y = 0

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
            if key[pygame.K_w] and not self.is_jumping:
                self.velocity_y = -30 # jumping of the players.
                self.is_jumping = True
            if key[pygame.K_r]:  #attacking of the player
                self.attack_type = 1
                self.attack(surface, target)
        elif self.name == "Darth Vader":
            if key[pygame.K_LEFT]:
                delta_x = -player_speed
            if key[pygame.K_RIGHT]:
                delta_x = player_speed
            if key[pygame.K_UP] and not self.is_jumping:
                self.velocity_y = -30 # jumping of the players.
                self.is_jumping = True
            if key[pygame.K_RSHIFT]:  #attacking of the player
                self.attack_type = 1
                self.attack(surface, target)

        # reduce velocity each frame so that jumping slows down and eventually reverses
        self.velocity_y += gravity

        # update the players jumping speed
        delta_y += self.velocity_y

        #ensure player stays on screen
        if self.rect.left + delta_x < 0:
            delta_x =  self.rect.left
        if self.rect.right + delta_x > screen_width:
            delta_x = screen_width - self.rect.right
        if self.rect.bottom + delta_y > screen_height - bottom_level:
            self.velocity_y = 0
            self.is_jumping = False 
            # allow to jump again now that player is back on the ground level
            delta_y = screen_height - bottom_level - self.rect.bottom

        # update player position.
        self.rect.centerx += delta_x
        self.rect.centery += delta_y

    def attack(self, surface, target):
        """handles the attack movement 
            not implemented yet
        """

        # create an attacking rectanlge when the player presses attack button
        # the attack is hitting the enemy if that rectange collides
        # with the space of the enemy rectangle
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y,
                                     2 * self.rect.width, self.rect.height)

        # check for collision. if the target player is in reach, for now just print this
        if attacking_rect.colliderect(target.rect):
            print(f'{self.name} hit the target!')

        pygame.draw.rect( surface, "green", attacking_rect)
        return
