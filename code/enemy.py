import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player,level=1):
        self.movestatus = False

        # general setup
        super().__init__(groups)
        # self.animations = None
        self.sprite_type = 'enemy'
        self.monster_level = level
        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'down_idle'
        # self.image = self.animations[self.status][self.frame_index]
        self.image = self.animations[self.status][self.frame_index]

        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        # movement
        self.image = pygame.transform.scale2x(self.image)
        if self.monster_level == 2:
            self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-100, -52)
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player
        self.monsta = pygame.mixer.Sound('../audio/heal.wav')
        self.monsta_channel = pygame.mixer.Channel(1)

        # invincibility timer
        self.vulnerable = True
        self.hit_time = 200
        self.invincibility_duration = 300

    def import_graphics(self, name):
        character_path = f'../graphics/monsters/{name}/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)


    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        direcshun = self.get_player_distance_direction(player)[1]

        if distance >= self.notice_radius:
            self.movestatus = False
        else:
            self.movestatus = True
        if self.movestatus:
            if direcshun.x > 0 and abs(direcshun.y) < abs(direcshun.x):
                self.status = 'right'
            elif direcshun.x < 0 and abs(direcshun.y) < abs(direcshun.x):
                self.status = 'left'
            elif direcshun.y > 0 and abs(direcshun.x) < abs(direcshun.y):
                self.status = 'down'
            elif direcshun.y < 0 and abs(direcshun.x) < abs(direcshun.y):
                self.status = 'up'
            if distance <= self.attack_radius and self.can_attack:
                if 'attack' not in self.status:
                    if 'idle' in self.status:
                        self.status = self.status.replace('_idle', '_attack')
                    else:
                        self.status = self.status + '_attack'
                        # self.frame_index = 0
                elif 'attack' in self.status:
                    self.status = self.status.replace('_attack', '')
            # elif distance <= self.notice_radius:
            #   self.status = 'move'
            else:

                if direcshun.x > 0 and abs(direcshun.y) < abs(direcshun.x):
                    self.status = 'right'
                elif direcshun.x < 0 and abs(direcshun.y) < abs(direcshun.x):
                    self.status = 'left'
                elif direcshun.y > 0 and abs(direcshun.x) < abs(direcshun.y):
                    self.status = 'down'
                elif direcshun.y < 0 and abs(direcshun.x) < abs(direcshun.y):
                    self.status = 'up'
                elif 'idle' not in self.status and 'attack' not in self.status:
                    self.status = self.status + '_idle'
        else:
            self.status = 'down_idle'

    def actions(self, player):
        if 'attack' in self.status:
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
        elif 'idle' not in self.status and self.movestatus:
            self.get_status(player)
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()


    def animate(self):
        if self.monster_name == "black":
            self.animation_speed = 0.1
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if 'attack' in self.status:
                self.can_attack = True
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        if self.monster_name == "golu":
            self.image = pygame.transform.scale2x(self.image)
        elif self.monster_name == 'black':
            self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center=self.hitbox.center)


        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
            else:
                self.vulnerable = False

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True
            else:
                self.vulnerable = False

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                pass
            # magic damage
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance
            #self.vulnerable = False

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.cooldowns()
        self.check_death()
        if self.movestatus:
            self.animate()
    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()
