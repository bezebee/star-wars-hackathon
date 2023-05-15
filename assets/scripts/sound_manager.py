import pygame
from pygame import mixer
import random
import pygame.time

class SoundManager:
    def __init__(self):
        mixer.init()
        pygame.init()
        self.title_scene_music = mixer.Sound("assets/audio/title_scene.mp3")
        self.title_scene_music.set_volume(0.5)
        self.background_music_1 = "assets/audio/background_1.mp3"
        self.background_music_2 = "assets/audio/background_2.mp3"
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
        self.block_fx = mixer.Sound("assets/audio/block.wav")
        self.block_fx.set_volume(0.5)
        self.darth_force_fx = mixer.Sound("assets/audio/darth_force.mp3")
        self.darth_force_fx.set_volume(0.5)
        self.luke_force_fx = mixer.Sound("assets/audio/luke_force.wav")
        self.luke_force_fx.set_volume(0.5)
        self.victory_fx = mixer.Sound("assets/audio/victory.wav")
        self.victory_fx.set_volume(0.5)

    
    def play_title_scene_music(self):
        self.title_scene_music.play()
    
    def stop_title_scene_music(self):
        fadeout_time = 3000  # Duration for fade-out in milliseconds
        pygame.mixer.fadeout(fadeout_time)

    def play_background_music(self):
        background_music = random.choice([self.background_music_1, self.background_music_2])
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.set_volume(0.3)
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
    
    def play_block_sound(self):
        self.block_fx.play()

    def play_darth_force_sound(self):
        self.darth_force_fx.play()

    def play_luke_force_sound(self):
        self.luke_force_fx.play()
        pygame.time.delay(1000)  # Delay for 1 second
        self.luke_force_fx.stop()
    
    def play_victory_sound(self):
        self.victory_fx.play()
        pygame.time.delay(3000)  # Delay for 1 second
        self.victory_fx.stop()
