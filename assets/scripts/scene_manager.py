import pygame
from display import *
from player import *
from game import Main

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
https://www.youtube.com/watch?v=A6eSzbllWbM&t=2s

https://nerdparadise.com/programming/pygame/part7


pausing:
https://www.youtube.com/watch?v=sDL7P2Jhlh8
***
"""
#parent class from which each scene can inherit methods
class Scene:
    def __init__(self):
        self.next = self

    #manage inputs and events based on current scene
    def input(self):
        pass
    
    #needs to 
    def update_scene(self):
        pass
    #draw the scene in the to the window 
    def draw_scene(self):
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
                        pygame.quit()

    
class TitleScene(Scene):
    def __init__(self):
        Scene.__init__(self)
    #to handle inputs during the Title screen
    #
    def input(self):
        print('will handle inputs on main menu')
    def update_scene(self):
        print('will handle current scene logic')
    def draw_scene(self):
        print('renders menu scene')

    
class GameScene(Scene):
    pass

"""A stack approach to scene management. An array to hold the scenes
and central logic to pass back and forth between them.
this approach was found in the Rik Cross video listed above."""
class SceneManager:
    def __init__(self):
        #create an array of scenes
        self.scenes = []
    def input(self):
        self.scenes[-1].input()
    def update(self):
        self.scenes[-1].update()
    def draw(self):
        self.scenes[-1].draw()
    def push(self, scene):
        pass
    def pop(self, scene):
        pass
    def set(self, scene):
        self.scenes = [scene]