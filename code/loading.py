import pygame
from support import import_folder
from settings import WIDTH, HEIGTH


class LoadingScreen():
    def __init__(self):
        self.frames = import_folder('../graphics/ui/loading/loading')
        self.frame_index = 0
        self.animation_speed = 0.02
        self.displaysurface = pygame.display.get_surface()

        self.image = self.frames[self.frame_index]
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGTH))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.hitbox = self.rect.inflate(-10, -10)
        self.music = pygame.mixer.Sound('../audio/Light Ambience 1.mp3')
        self.music.set_volume(0.5)

    def animate(self):
        animation = self.frames

        # Loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGTH))
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.animate()
        self.music.play(-1)
        self.displaysurface.blit(self.image, (0, 0), self.rect)
