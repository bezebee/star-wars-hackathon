"""This is the starting point for the game"""
from player import Player
import pygame

# Colour variables
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def main():
    """function that contains the game loop"""

    # This will create a fixed size window of the the game.
    # We could make it flexible but for now hard-coded
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set screen game name
    # name can be decided on and updated as desired
    pygame.display.set_caption("Luke VS Vader")


    # load and scale background image
    bg_image = pygame.image.load("assets/images/background/background_swamp.png")
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # load fighters spritesheet
    luke_sheet = pygame.image.load("assets/images/luke/Sprites/luke_sheet.tiff").convert_alpha()
    darth_sheet = pygame.image.load("assets/images/darth/Sprites/darth.png").convert_alpha()


    # define number of steps in each animation
    LUKE_ANIMATION_STEPS = [3, 9, 8,8,7,8,8,8,6,8,6,6,5,4,8,3,8,7,5]
    DARTH_ANIMATION_STEPS = [8,6,6,4,6,6,6,4,8,8,6,4,4,4,6,6]
    
    # this clock will be used in the game loop to limit the the frame rate to 60.
    # Happy to change that, it's copy+paste from a tutorial
    clock = pygame.time.Clock()

    # add first player to the game.
    # The use of a GroupSingle was advised to handle collisions between players
    player_one  = pygame.sprite.GroupSingle()
    player_one.add(Player((200,300), "blue", "Luke Skywalker"))

    # add second player to the game. Add this player to a second Group
    player_two  = pygame.sprite.GroupSingle()
    player_two.add(Player((400,300), "red", "Darth Vader"))

    # Create health bar
    def create_health_bar(player, health, x, y):
        '''create a health bar with differnt colours for each player'''
        ratio = health / 100
        if player == player_one:
            pygame.draw.rect(screen, WHITE, (x - 1, y - 1, 222, 22), 2, border_radius=5) # white border
            pygame.draw.rect(screen, BLUE, (x, y, 220 * ratio, 20), border_radius=5) # blue health bar
        elif player == player_two:
            pygame.draw.rect(screen, WHITE, (x, y, 222, 22), 2, border_radius=5) # white border
            pygame.draw.rect(screen, RED, (x, y, 220 * ratio, 20), border_radius=5) # red health bar

    # infinite game loop unitl the user clicks on the exit button
    while True:

        # get all events that pygame has registered
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # draw background on the screen for the next frame
        screen.blit(scaled_bg, (0, 0))

        # display health bar
        create_health_bar(player_one, player_one.sprite.health, 20, 20)
        create_health_bar(player_two, player_two.sprite.health, 395, 20)

        # handle the movement of both players
        # luke gets vader as target assigned by last parameter
        # vader gets luke as target assigned by last parameter
        for luke, vader in zip(player_one, player_two):
            luke.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, vader)
            vader.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, luke)

       # draw the two players
        player_one.draw(screen)
        player_two.draw(screen)

        # update the canvas
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
