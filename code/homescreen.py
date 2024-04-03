import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy
from collectables import*
class Homescreen:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.ui_sprites = pygame.sprite.Group()
    def create_map(self):

        layouts = {
            'boundary': import_csv_layout('../map new/ui.csv')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.ui_sprites], 'invisible')
    def run(self):
        # update and draw the game
        self._sprites.custom_draw()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.floor_surf = pygame.image.load('../graphics/ui/home page.jpg').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self):
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
