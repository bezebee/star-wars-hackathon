"""Class to describe a player of this game"""
import pygame
pygame.font.init() # Initialize the Pygame font

# Colour variables
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class HealthBar():
    """A class to represent a health bar for a player
        setting dimensions and colour attributes
    """

    def __init__(self, player, width, height):
        self.player = player
        self.width = width
        self.height = height
        self.border_width = 222
        self.border_height = 22
        self.border_radius = 5
        self.border_colour = WHITE
        self.health_colour = BLUE if player.color == 'blue' else RED
        self.font = pygame.font.SysFont('Arial', 14)  # Set the font for the health text

    def draw(self, screen):
        """Draws the health bar on the screen"""
        ratio = self.player.health / 100
        # Border
        border_rect = pygame.Rect(self.width, self.height, self.border_width, self.border_height)
        # Health bar
        health_rect = pygame.Rect(self.width + 1, self.height + 1, int(220 * ratio)
                                  , self.height - 2)
        # Draw health bar
        pygame.draw.rect(screen, self.border_colour, border_rect, 2,
                          border_radius=self.border_radius)
        pygame.draw.rect(screen, self.health_colour, health_rect, border_radius=self.border_radius)
        # Draw the health stats
        health_text = self.font.render(f' {self.player.health} /100', True, WHITE)
        text_rect = health_text.get_rect()
        text_rect.center = (self.width + self.border_width / 2,
                             self.height + self.border_height / 2)
        screen.blit(health_text, text_rect)


class Player(pygame.sprite.Sprite) :
    """Describes a player in the fighting game
        Two player names are allowed
            "Luke Skywalker" - this will be Player 1
            "Darth Vader" - this will be Player 2
        In this way, depending on player name, different keys press events cause different moves 
    """

    def __init__(self, pos=None, color=None, name=None, data=None, sprite_sheet=None, animation_steps=None ) -> None:
        """
        is_jumping : this variable ensures that jump button has no effect
                     while jumping to avoid double jumps
        attack_type : this variable stores the attack type that was used by the player.
                       currently 0 means not attack, 1 means standard sabre attack 
                       (for now just one attack)
        is_jumping : this variable ensures that attack button has no effect
                     while attacking to avoid multiple attacks by keeping key pressed
        """
        super().__init__()
        self.flip = False
        self.image = pygame.Surface((32, 32))
        self.image.fill( color if color else "lightblue")
        self.rect = self.image.get_rect(center = pos if pos else (200,300))
        self.name= name
        self.velocity_y = 0
        self.is_jumping = False
        self.is_attacking = False
        self.attack_type = 0
        self.health = 100
        self.color = color
        self.update_time = pygame.time.get_ticks
        self.size = data[0]
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0   # 0 is idle, 1 is run
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]

    def load_images(self, sprite_sheet, animation_steps):
        """extract images from spritesheet"""
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size )
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list

    def update(self, surface):
        """hanlde animation update image """
        self.image = self.animation_list[self.action][self.frame_index]
        surface.blit(self.image, (self.rect.x, self.rect.y))

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


        # for now, don't do any movements while attacking.
        # Can be refined later
        if not self.is_attacking:

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

        # Make players always face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # update player position.
        self.rect.centerx += delta_x
        self.rect.centery += delta_y

    def attack(self, surface, target):
        """handles the attack movement 
            not implemented yet
        """

        # set attacking state to suppress any other movements
        # currently this would just freeze the player
        # i will not activate the is_attacking for now 
        # but if you want to keep implementing, uncomment the next line 
        #self.is_attacking = True

        # create an attacking rectanlge when the player presses attack button
        # the attack is hitting the enemy if that rectange collides
        # with the space of the enemy rectangle
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),
                                     self.rect.y,
                                     2 * self.rect.width, self.rect.height)

        # check for collision. if the target player is in reach, reduce health by 10
        if attacking_rect.colliderect(target.rect):
            # Reduces health if is bigger than 0 
            if target.health > 0:
                target.health -= 10

        pygame.draw.rect( surface, "green", attacking_rect)
        return
