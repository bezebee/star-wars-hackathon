"""This is the starting point for the game"""
from player import Player, HealthBar
from display import Display
import pygame
from pygame import mixer

mixer.init()

# Colour variables
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Main:
    '''Class for main game loop'''
    def __init__(self):
        # display dimensions and name
        self.display = Display(640, 480, "Luke VS Vader")
        # this clock will be used in the game loop to limit the the frame rate to 60.
        self.clock = pygame.time.Clock()
        # add first player to the game.
        # The use of a GroupSingle was advised to handle collisions between players
        self.player_one = pygame.sprite.GroupSingle()
        self.player_one.add(Player((200, 300), "blue", "Luke Skywalker"))
        # add second player to the game
        self.player_two = pygame.sprite.GroupSingle()
        self.player_two.add(Player((400, 300), "red", "Darth Vader"))
        # Create health bars for each player
        self.health_bar_one = HealthBar(self.player_one.sprite, 20, 20)
        self.health_bar_two = HealthBar(self.player_two.sprite, 395, 20)
        # define fonts
        self.count_font = self.display.define_font("assets/fonts/bungee_regular.ttf", 48)
        self.score_font = self.display.define_font("assets/fonts/bungee_regular.ttf", 24)
        # set countdown starting number
        self.intro_count = 3
        # update last count
        self.last_count_update = pygame.time.get_ticks()

    def handle_events(self):
        '''get all events that pygame has registered'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def update_players(self):
        '''handle the movement of both players'''
        # luke gets vader as target assigned by last parameter
        # vader gets luke as target assigned by last parameter
        for luke, vader in zip(self.player_one, self.player_two):
            luke.move(self.display.width, self.display.height, self.display.screen, vader)
            vader.move(self.display.width, self.display.height, self.display.screen, luke)
    
    def update_countdown(self):
        '''Handle updating the game countdown'''
        # update fight countdown and allow players to move only once complete
        if self.intro_count <= 0:
            # move fighters
            self.update_players()
        else:
            # display count timer
            self.display.draw_text(str(self.intro_count), self.count_font, BLACK, self.display.width / 2, self.display.height / 3)
            # update count timer
            if (pygame.time.get_ticks() - self.last_count_update) >= 1000:
                self.intro_count -= 1
                self.last_count_update = pygame.time.get_ticks()

    def run(self):
        '''Function to run the game'''

        # load background image
        bg_image = self.display.load_image("assets/images/background/background_swamp.png",
                                            (self.display.width, self.display.height))

        # load fighters spritesheet
        luke_sheet = self.display.load_image("assets/images/luke/Sprites/luke_sheet.tiff")
        darth_sheet = self.display.load_image("assets/images/darth/Sprites/darth.png")

        # define number of steps in each animation
        LUKE_ANIMATION_STEPS = [3, 9, 8, 8, 7, 8, 8, 8, 6, 8, 6, 6, 5, 4, 8, 3, 8, 7, 5]
        DARTH_ANIMATION_STEPS = [8, 6, 6, 4, 6, 6, 6, 4, 8, 8, 6, 4, 4, 4, 6, 6]

        #infinite game loop until the user clicks on the exit button
        while True:
            if self.handle_events():
                break

            self.display.draw_background(bg_image)# load background image
            self.display.draw_health_bar(self.health_bar_one)# load health bar player one
            self.display.draw_health_bar(self.health_bar_two)# load health bar player two
            self.update_countdown() # load function that handles countdown at the start of the game
            self.display.draw_sprite(self.player_one)# loads player one
            self.display.draw_sprite(self.player_two)# loads player two
            self.display.update()# update display
            self.clock.tick(60)# start clock

if __name__ == '__main__':
    Main().run()
