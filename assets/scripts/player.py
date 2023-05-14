"""Class to describe a player of this game"""
import pygame
from sound_manager import SoundManager
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
        # Set the font for the health text
        self.font = pygame.font.SysFont('Nunito', 14)

    def draw(self, screen):
        """Draws the health bar on the screen"""
        ratio = self.player.health / 100
        # Border
        border_rect = pygame.Rect(
            self.width, self.height, self.border_width, self.border_height)
        # Health bar
        health_rect = pygame.Rect(
            self.width + 1, self.height + 1, int(220 * ratio), self.height - 2)
        # Draw health bar
        pygame.draw.rect(screen, self.border_colour, border_rect, 2,
                         border_radius=self.border_radius)
        pygame.draw.rect(screen, self.health_colour,
                         health_rect, border_radius=self.border_radius)
        # Draw the health stats
        health_text = self.font.render(
            f' {self.player.health} /100', True, WHITE)
        text_rect = health_text.get_rect()
        text_rect.center = (self.width + self.border_width / 2,
                            self.height + self.border_height / 2)
        screen.blit(health_text, text_rect)


class Player(pygame.sprite.Sprite):
    """Describes a player in the fighting game
        Two player names are allowed
            "Luke Skywalker" - this will be Player 1
            "Darth Vader" - this will be Player 2
        In this way, depending on player name, different keys press events cause different moves 
    """

    def __init__(self, pos=None, color=None, name=None, data=None, sprite_sheet=None, animation_steps=None) -> None:
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
        self.image = pygame.Surface((48, 48))
        self.image.fill(color if color else "lightblue")
        self.rect = self.image.get_rect(center=pos if pos else (200, 300))
        self.name = name
        self.velocity_y = 0
        self.is_jumping = False
        self.is_attacking = False
        self.is_blocking = False # check if player is blocking
        self.is_winning = False
        self.is_falling = False
        self.is_running = False
        self.is_alive = True
        self.blocking_start_time = 0 # controls blocking cooldown time
        self.attack_type = 0
        self.attack_cooldown = 10 # controls attack type cooldown
        self.health = 100
        self.force = 10 # controls attack type cooldown
        self.color = color
        self.update_time = pygame.time.get_ticks
        self.height = data[0]
        self.width = data[1]
        self.image_scale = data[2]
        self.offset = data[3]
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0:idle, 1:attack , 2:run, 3: jump
        self.frame_index = 0
        self.sound_manager = SoundManager()
        # just for debugging. This is just to confirm that the second movement (attack) of the luke character gets displayed correctly.
        if self.name=="Luke Skywalker":
             self.action = 0
        print(f"current action : {self.action}")

    def load_images(self, sprite_sheet, animation_steps):
        """extract images from spritesheet"""
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * self.width, y * self.height, self.width, self.height)
                temp_img_list.append(pygame.transform.scale(
                    temp_img, (self.width * self.image_scale, self.width * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def update(self):
        """add animation to static images from sprite sheet"""
        # determine what kind of action the player is doing at the moment 
        # quick debuggin : since we have only the sheet for luke ready, only animate luke
        # for the moment 
        if self.name == "Luke Skywalker":
            self.set_current_action()
        self.frame_index += .1
        # ensure that it reads only images that are in the sprite sheet
        if self.frame_index > len(self.animation_list[self.action]):
            self.frame_index = 0
        self.image = self.animation_list[self.action][int(self.frame_index)]
        pygame.draw.rect(self.image, "red", [0, 0, self.width, self.height], 2)

    def set_current_action(self):
        """
        based on the current state of the player, set action variable to change between animation types
        0 : idle, 1: attack , 3: running, 4: jumping, 6: death
        """
        # depending on the state, set the action parameter to select the corresponding sprite sheet
        if self.is_jumping:
            self.action = 3
        else:
            if self.is_attacking:
                self.action = 1
            elif self.is_blocking:
                pass # needs to be implemented. The running animation is the 
                        #placeholder currently for this state 
            elif self.is_winning:
                pass # needs to be implemented
            elif self.health <= 0:
                self.health = 0
                self.is_alive = False
                # self.action = 6 # death state
            elif self.is_falling:
                pass # needs to be implemented
            elif self.is_running:
                self.action = 2
            else:
                self.action = 0 # idle state

    def move(self, screen_width, screen_height, surface, target, game_over):
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

        # for now, don't do any movements while attacking or if dead or if game over.
        # Can be refined later
        if not self.is_attacking and self.is_alive and not game_over:

            # The movement depends now on the player name.
            # If Luke (Player 1), the "A" and "D" handle left and right
            # If his father (Player 2), the "Left" and "Right" handle left and right
            if self.name == "Luke Skywalker":
                if not self.is_blocking:  # Stop all movements if blocking
                    if key[pygame.K_a]:
                        delta_x = -player_speed
                    if key[pygame.K_d]:
                        delta_x = player_speed
                    if key[pygame.K_w] and not self.is_jumping:
                        self.velocity_y = -30  # jumping of the players.
                        self.is_jumping = True
                        # play the jump sound fx
                        self.sound_manager.play_luke_jump_sound()
                    if key[pygame.K_r] and self.attack_cooldown == 10:  # attack type 1
                        self.attack_type = 1 # attack type
                        self.attack(surface, target) # calls attack function
                        self.attack_cooldown = 0 # sets cooldown to 0
                        self.attack_cooldown = pygame.time.get_ticks()  # Start a timer
                        # play the attack sound fx
                        self.sound_manager.play_luke_attack_sound()
                    if key[pygame.K_f] and self.force == 10:  # attack type 2
                        self.attack_type = 2 # attack type
                        self.attack(surface, target) #calls attack function 
                        self.force = 0 # sets force to 0
                        self.force = pygame.time.get_ticks()  # Start a timer
                    if key[pygame.K_q] and not self.is_blocking:
                        self.block() # blocks an attack when "q" is pressed"
                    
            elif self.name == "Darth Vader":
                if not self.is_blocking:  # stop all movements if blocking
                    if key[pygame.K_LEFT]:
                        delta_x = -player_speed
                    if key[pygame.K_RIGHT]:
                        delta_x = player_speed
                    if key[pygame.K_UP] and not self.is_jumping:
                        self.velocity_y = -30 # jumping of the players.
                        self.is_jumping = True
                        # play the jump sound fx
                        self.sound_manager.play_darth_jump_sound()
                    if key[pygame.K_RSHIFT] and self.attack_cooldown == 10: # attack type 1 
                        self.attack_type = 1 # attack type
                        self.attack(surface, target) #calls attack function
                        self.attack_cooldown = 0 #sets cooldown to sero
                        self.attack_cooldown = pygame.time.get_ticks()  # Start a timer
                        # play the attack sound fx
                        self.sound_manager.play_darth_attack_sound()
                    if key[pygame.K_RCTRL] and self.force == 10:  # attack type 2
                        self.attack_type = 2 #attack type
                        self.attack(surface, target)# calls atack fucntion
                        self.force = 0 #set force to zero
                        self.force = pygame.time.get_ticks()  # Start a timer
                    if key[pygame.K_SLASH] and not self.is_blocking:
                        self.block() # blocks an attack when "/" is pressed"

            current_time = pygame.time.get_ticks()  # gets current time
            # checks if more than 1 second has passed since blocking
            if current_time - self.blocking_start_time >= 1000:
                self.is_blocking = False  # Changes blocking to false
            # checks if more than 15 second has passed since using the force
            if current_time - self.force >= 15000:
                self.force = 10
            # checks if more than 1 second has passed since attacking
            if current_time - self.attack_cooldown >= 1000:
                self.attack_cooldown = 10            

        # reduce velocity each frame so that jumping slows down and eventually reverses
        self.velocity_y += gravity

        # update the players jumping speed
        delta_y += self.velocity_y

        # ensure player stays on screen
        if self.rect.left + delta_x < 0:
            delta_x = self.rect.left
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

        # update the player state
        if abs(delta_x) > 0:
            self.is_running = True
        else:
            self.is_running = False

    def block(self):
        '''Handles the blocking action'''
        self.is_blocking = True
        self.blocking_start_time = pygame.time.get_ticks()  # Start a timer

    def attack(self, surface, target):
        """handles the attack movement"""

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
            # play the hit sound fx
            self.sound_manager.play_hit_sound()
            if target.health > 0:  # Reduces health if is bigger than 0
                if target.is_blocking is False:  # only deals damage if target isn't blocking
                    if self.attack_type == 1:
                        target.health -= 5 # attack type 1 deals 5 of damage
                    elif self.attack_type == 2:
                        target.health -= 10 # attack type 2 deals 10 of damage
                elif self.attack_type == 2: # attack type 2 will deal damage even when blocking
                    target.health -= 20 # if blocking attack type 2 deals double damage
        pygame.draw.rect(surface, "green", attacking_rect)
        return
