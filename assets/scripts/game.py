"""This is the starting point for the game"""
from player import Player
import pygame

def main():
    """function that contains the game loop"""
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    player_one  = pygame.sprite.GroupSingle()
    player_one.add(Player((200,300), "blue"))

    player_two  = pygame.sprite.GroupSingle()
    player_two.add(Player((400,300), "red"))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        screen.fill('grey')
        player_one.draw(screen)
        player_two.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
