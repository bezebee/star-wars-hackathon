import pygame
from pygame import mixer

class SoundManager:
    def __init__(self):
        mixer.init()
        pygame.init()
        self.background_music = "assets/audio/music.mp3"
        self.luke_attack_fx = mixer.Sound("assets/audio/lightsabre_luke.wav")
        self.luke_attack_fx.set_volume(0.5)
        self.darth_attack_fx = mixer.Sound("assets/audio/lightsabre_darth.mp3")
        self.darth_attack_fx.set_volume(0.5)

    def play_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)

    def play_luke_attack_sound(self):
        self.luke_attack_fx.play()

    def play_darth_attack_sound(self):
        self.darth_attack_fx.play()

    # def cleanup(self):
    #     mixer.quit()
    #     pygame.quit()