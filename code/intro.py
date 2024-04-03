
import pygame
from settings import *
from support import import_folder

class Intro:
    def __init__(self):
        self.frames = import_folder('../graphics/intro')
        self.frame_index = 0
        self.animation_speed = 0.2

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hitbox = self.rect
        self.count = 0
        self.finished = False  # Flag to indicate if the intro has finished

        # Load intro music but don't play it immediately
        # pygame.mixer.music.load('../audio/intro.wav')
        # pygame.mixer.music.set_volume(1)  # Adjust volume if needed

    def animate(self):
        animation = self.frames

        # Loop over the frame index
        if self.count == 0:
            self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = len(animation) - 1
            self.count = 1
        # Set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image,(WIDTH, HEIGTH))
        self.rect = self.image.get_rect(topleft=self.hitbox.center)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.finished = True  # Set the flag to indicate that the intro has finished

    def update(self):
        self.handle_input()
        if not self.finished:
            self.animate()

        # Check if the music is not already playing before starting it
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

    def reset(self):
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.count = 0
        self.finished = False

    def stop_music(self):
        # pygame.mixer.music.stop()
        pass


class Intro1:
    def __init__(self):
        self.frames = import_folder('../graphics/intro2')
        self.frame_index = 0
        self.animation_speed = 0.2

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.count = 0
        self.finished = False
        # pygame.mixer.music.load('../audio/intro2.wav')
        # pygame.mixer.music.set_volume(0.5)  # Adjust volume if needed

    def animate(self):
        animation = self.frames

        # Loop over the frame index
        if self.count == 0:
            self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        # Set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image,(WIDTH, HEIGTH))

        self.rect = self.image.get_rect()

    def reset(self):
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hitbox = self.rect
        self.count = 0
        self.finished = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.finished = True  # Set the flag to indicate that the intro has finished

    def update(self):
        self.handle_input()
        if not self.finished:
            self.animate()

        # Check if the music is not already playing before starting it
        # if not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.play(-1)

    def stop_music(self):
        pass
class Final:
    def __init__(self):
        self.frames = import_folder('../graphics/final2')
        self.frame_index = 0
        self.animation_speed = 0.2

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hitbox = self.rect
        self.count = 0
        self.finished = False  # Flag to indicate if the intro has finished

        # # Load intro music but don't play it immediately
        # pygame.mixer.music.load('../audio/stomp.wav')
        # pygame.mixer.music.set_volume(0.5)  # Adjust volume if needed

    def animate(self):
        animation = self.frames

        # Loop over the frame index
        if self.count == 0:
            self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = len(animation) - 1
            self.count = 1
        # Set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image,(WIDTH, HEIGTH))

        self.rect = self.image.get_rect()

    def reset(self):
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hitbox = self.rect
        self.count = 0
        self.finished = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.finished = True  # Set the flag to indicate that the intro has finished

    def update(self):
        self.handle_input()
        if not self.finished:
            self.animate()

        # Check if the music is not already playing before starting it
        # if not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.play(-1)

    def stop_music(self):
    #     pygame.mixer.music.stop()
        pass


