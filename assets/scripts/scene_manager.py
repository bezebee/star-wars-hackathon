import pygame
from display import Display

"""This class is a central scene handler which should acomplish several things.
It should be able to switch between scenes. This means that it must be able to draw a new scene. 

It should be able to Update the logic of the current scene,
and it should be able to pause the game during the main loop, while allowing scene persistence, 
i.e., doesn't reset the health and positional values.

A major struggle is trying to avoid duplicating existing code, however for the purposes of this project, I will have to bite the bullet.
Some of the methods herein are likely similar to the Main class but with time constartints, needs must.

sources of reasearching this class: 
***
central logic and methods:
Rik Cross - Python and Pygame Platform Game Part 19 - Scenes
https://www.youtube.com/watch?v=A6eSzbllWbM&t=2s

Rik Cross - Python and Pygame Platform Game Part 20 - Scene Transitions
https://www.youtube.com/watch?v=cZbqMA55PTI

PyGame Tutorial: Centralized Scene Logic
https://nerdparadise.com/programming/pygame/part7


pausing:
thenewboston - Pygame (Python Game Development) Tutorial - 39 - Pausing the Game
https://www.youtube.com/watch?v=sDL7P2Jhlh8
***
"""
screen_width= 640
screen_height = 480
title_img = pygame.image.load('assets/images/screens/game-start-v2.png')
game_bg = pygame.image.load('assets/images/background/background_swamp.png')

#parent class from which each scene can inherit methods
class Scene:

    def __init__(self):
        self.next = self
    #what to do when entering a scene
    def onEnter(self):
        pass
    #what to do when exiting a scene
    def onExit(self):
        pass
    #manage inputs and events based on current scene
    def input(self, sm):
        pass
    
    #handle scenes logic
    def update_scene(self, sm):
        pass
    #draw the scene in the to the window 
    def draw_scene(self, sm, screen):
        pass
    
    #pause creates a new game loop where a screen is dipslayed
    def Pause():
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        SceneManager.push(TitleScene())

    
class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def onEnter(self):
        print('Now entering Main Menu...')

    def onExit(self):
        print('Now Exiting Main Menu...')

    def input(self, sm):
        keys = pygame.key.get_pressed()
        #enter main game
        if keys[pygame.K_RETURN]:
            sm.push(GameScene())
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()

    def draw_scene(self, sm, screen):
        screen= pygame.display.set_mode((screen_width, screen_height))
        bg_image = title_img
        bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(bg_image, (0, 0))
        pygame.display.update()

    
class GameScene(Scene):
    def onEnter(self):
        print('Now entering Game Scene...')
    
    def onExit(self):
        print('Now exiting Game Scene...')
    #to handle inputs during the Game Over screen
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            Scene.Pause()
        #return to title screen
        elif keys[pygame.K_q]:
            sm.pop()

    def draw_scene(self, sm, screen):
        screen= pygame.display.set_mode((screen_width, screen_height))
        bg_image = game_bg
        bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(bg_image, (0, 0))
        pygame.display.update()
   
class GameOver(Scene):
    def onEnter(self):
        print('Now entering Game Over...')
    
    def onExit(self):
        print('Now Exiting Game Over...')
    #to handle inputs during the Game Over screen
    def input(self, sm):
        print('will handle inputs in gameOVER')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            Scene.Pause()
        #return to title screen
        elif keys[pygame.K_q]:
            sm.push(TitleScene())
    def update_scene(self, sm):
        print('will handle GAME OVER logic')
    def draw_scene(self, sm):
        print('renders GAME OVER scene')


"""A stack approach to scene management. An array to hold the scenes
and central logic to pass back and forth between them.
this approach was found in the Rik Cross video listed above."""
class SceneManager:
    def __init__(self):
        #create an array of scenes
        self.scenes = []
    #to enter the scene
    def enterScene(self):
        if len(self.scenes) >0:
            self.scenes[-1].onEnter()
    #to exit the scene
    def exitScene(self):
        if len(self.scenes) >0:
            self.scenes[-1].onExit()
    #to handle inputs in scene
    def input(self):
        if len(self.scenes) > 0:#check that a scene exists
            self.scenes[-1].input(self)
    #to handle scene logic
    def update_scene(self):
        self.scenes[-1].update_scene(self)
    #to draw the scene
    def draw_scene(self, screen):
        self.scenes[-1].draw_scene(self, screen)

    def push(self, scene):
        self.exitScene()        
        self.scenes.append(scene)
        self.enterScene()

    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()

    def set(self, scene):
        while len(self.scenes) >0:
            self.pop()
        self.push(scene)
