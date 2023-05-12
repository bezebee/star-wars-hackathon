"""This is the starting point for the game"""
from player import Player
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

    # infinite game loop unitl the user clicks on the exit button
    while True:

        # get all events that pygame has registered
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # handle the movement of the first player
        for player in player_one:
            player.move(SCREEN_WIDTH)

        # handle the movement of the second player
        for player in player_two:
            player.move(SCREEN_WIDTH)

        # draw background and the two players on the screen for the next frame
        screen.blit(scaled_bg, (0, 0))
        player_one.draw(screen)
        player_two.draw(screen)

        # update the canvas
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
