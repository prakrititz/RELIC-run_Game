from support import import_folder
import pygame
import sys
from settings import *
from level import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4
from pygame.locals import *
from intro import *

from loading import LoadingScreen
# pygame.mixer.pre_init(44100, 16, 2, 4096)
from pygame.locals import*

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH),pygame.SCALED)
        pygame.display.set_caption('RELIC RUN')
        self.clock = pygame.time.Clock()

        self.level1 = Level1()
        self.level2 = Level2()
        self.level3 = Level3()
        self.level4 = Level4()
        self.intro = Intro()
        self.intro2 = Intro1()# Create an instance of the intro class
        self.final = Final()

        # Transition variables
        self.transition_duration = 5000
        self.transition_start_time = 0
        self.transition_alpha = 0

        # Homescreen vari ables
        self.homescreen_image = pygame.image.load('../graphics/ui/home page.jpg').convert()
        self.homescreen_image = pygame.transform.scale(self.homescreen_image,(1280,720))
        self.gameover_image = pygame.image.load('../graphics/ui/gameover.jpg').convert()
        self.loading = LoadingScreen()
        self.gameover_image_rect = self.gameover_image.get_rect()
        self.homescreen_rect = self.homescreen_image.get_rect()
        self.game_state = 0

        pygame.mixer.music.load('../audio/home.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)


    def homescreen(self):
        self.screen.blit(self.homescreen_image, (0,0))
        pygame.display.update()
    def gameover(self):
        self.gameover_image = pygame.transform.scale(self.gameover_image,(1280,720))
        self.screen.blit(self.gameover_image,(0,0))
        self.reset_game()
        pygame.display.update()

    def reset_game(self):
        # Reset all game-related variables and clear sprites
        self.level1.reset()
        self.level2.reset()
        self.level3.reset()
        self.level4.reset()
        self.intro.reset()
        self.intro2.reset()
        self.final.reset()

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.game_state == 0:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('../audio/intro.wav')
                        pygame.mixer.music.set_volume(0.8)
                        pygame.mixer.music.play(-1)
                        self.transition_start_time = pygame.time.get_ticks()
                        self.game_state = 1  # Set game state to transition


            self.screen.fill((0, 0, 0))  # Fill with black

            if self.game_state == 0:
                self.homescreen()

            elif self.game_state == 1:  # Transition to Intro

                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.transition_start_time
                if elapsed_time < self.transition_duration:
                    self.loading.update()
                    pygame.mixer.music.stop()
                else:
                    self.transition_alpha = 255
                    self.game_state = 2  # Set game state to Intro

            elif self.game_state == 2:# Intro
                self.intro.update()
                self.screen.blit(self.intro.image, (0,0))  # Blit intro frames
                pygame.display.update()
                if self.intro.finished:  # Check if intro has finished
                    self.intro.stop_music()  # Stop the intro music
                    pygame.mixer.music.load('../audio/intro2.wav')
                    self.transition_start_time = pygame.time.get_ticks()
                    self.game_state = 3  # Set game state to Level 1

            elif self.game_state == 3:
                pygame.mixer.music.load('../audio/Ambient 2.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                self.level1.run()
                if self.level1.gameover:
                    pygame.mixer.music.stop()
                    self.game_state = 20  # Game over, return to homescreen
                elif self.level1.completed:
                    self.transition_start_time = pygame.time.get_ticks()
                    self.game_state = 4  # Set game state to transition


            elif self.game_state == 4:  # Transition to Level 2
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.transition_start_time

                if elapsed_time < self.transition_duration:
                    self.transition_alpha = min(255, int(255 * elapsed_time / self.transition_duration))
                    self.loading.update()
                else:
                    self.transition_alpha = 255
                    self.game_state = 5  # Set game state to Level 2

                transition_surface = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
                transition_surface.fill((0, 0, 0, self.transition_alpha))
                self.screen.blit(transition_surface, (WIDTH/2,HEIGTH/2))


            elif self.game_state == 5:# Intro
                self.intro2.finished = False
                self.intro2.update()
                self.screen.blit(self.intro2.image, (0,0))  # Blit intro frames
                pygame.display.update()
                if self.intro2.finished:  # Check if intro has finished
                    self.intro2.stop_music()  # Stop the intro music
                    self.transition_start_time = pygame.time.get_ticks()
                    self.game_state = 6  # Set game state to Level 1

            elif self.game_state == 6:  # Level 2
                self.level2.run()
                if self.level2.gameover:
                    self.game_state == 20
                    pygame.mixer.stop()
                if self.level2.completed:
                    pygame.mixer.stop()
                    self.game_state = 7
                    pygame.mixer.music.load('../audio/darkambience(from fable).mp3')
                    pygame.mixer.music.set_volume(3)
                    pygame.mixer.music.play(-1)


            elif self.game_state == 7:  # Transition to Level 2
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.transition_start_time

                if elapsed_time < self.transition_duration:
                    self.transition_alpha = min(255, int(255 * elapsed_time / self.transition_duration))
                    self.loading.update()
                    self.loading.music.stop()
                else:
                    self.transition_alpha = 255
                    self.game_state = 8  # Set game state to Level 2

                transition_surface = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
                transition_surface.fill((0, 0, 0, self.transition_alpha))
                self.screen.blit(transition_surface, (0,0))

            elif self.game_state == 8:
                self.level3.run()
                if self.level3.completed:
                    pygame.mixer.stop()
                    self.game_state = 9
                    pygame.mixer.music.load('../audio/home.mp3')
                    self.monster_scream = pygame.mixer.Sound('../audio/monsterScream.wav')
                    self.monster_scream_channel = pygame.mixer.Channel(4)
                    self.monster_stomp = pygame.mixer.Sound('../audio/stomp.wav')
                    self.monster_stomp_channel = pygame.mixer.Channel(5)

                    pygame.mixer.music.play(-1)
                    self.monster_scream_channel.play(self.monster_scream,0)


            elif self.game_state == 9:# Intro
                self.final.update()
                self.screen.blit(self.final.image, (0,0))  # Blit intro frames
                pygame.display.update()
                if self.final.finished:  # Check if intro has finished
                    self.monster_stomp_channel.play(self.monster_stomp,-1)
                    self.monster_scream_channel.play(self.monster_scream,0)
                    self.transition_start_time = pygame.time.get_ticks()
                    self.game_state = 10  # Set game state to Level 1

            elif self.game_state == 10:
                self.level4.run()
                if self.level4.completed:
                    pass
                if self.level4.gameover:
                    self.game_state = 20
            elif self.game_state == 20:
                self.gameover()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
