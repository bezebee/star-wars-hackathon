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
        self.hit_fx = mixer.Sound("assets/audio/hit.wav")
        self.hit_fx.set_volume(0.5)
        self.death_fx = mixer.Sound("assets/audio/death.wav")
        self.darth_jump_fx = mixer.Sound("assets/audio/darth_jump.mp3")
        self.darth_jump_fx.set_volume(1)
        self.luke_jump_fx = mixer.Sound("assets/audio/luke_jump.wav")
        self.luke_jump_fx.set_volume(0.3)

    def play_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)

    def play_luke_attack_sound(self):
        self.luke_attack_fx.play()

    def play_darth_attack_sound(self):
        self.darth_attack_fx.play()

    def play_hit_sound(self):
        self.hit_fx.play()

    def play_death_sound(self):
        self.death_fx.play()

    def play_darth_jump_sound(self):
        self.darth_jump_fx.play()

    def play_luke_jump_sound(self):
        self.luke_jump_fx.play()

    # I don't think we need this, but I'll leave it here for now
    # def cleanup(self):
    #     mixer.quit()
    #     pygame.quit()