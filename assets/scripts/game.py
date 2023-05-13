"""This is the starting point for the game"""
from player import Player, HealthBar
import pygame

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

    # Create health bars for each player
    health_bar_one = HealthBar(player_one.sprite, 20, 20)
    health_bar_two = HealthBar(player_two.sprite, 395, 20)

    # infinite game loop unitl the user clicks on the exit button
    while True:

        # get all events that pygame has registered
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # draw background on the screen for the next frame
        screen.blit(scaled_bg, (0, 0))

        # Draw the health bars
        health_bar_one.draw(screen)
        health_bar_two.draw(screen)

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
