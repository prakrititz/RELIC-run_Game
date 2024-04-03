import pygame
from settings import * 
from player import Player
class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH*3,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)

		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			magic = pygame.image.load(magic['graphic']).convert_alpha()
			self.magic_graphics.append(magic)

		self.pixelated_font = pygame.font.Font('../graphics/font/joystix.ttf', 30)

		# Status message variables
		self.status_message = ""
		self.status_message_duration = 2000  # Duration in milliseconds
		self.status_message_start_time = 0
		self.current_level = 1

	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,player):
		if self.current_level == 1:
			text_surf = self.font.render(f"Space to attack, Shift to run",False,TEXT_COLOR)
		elif self.current_level == 2:
			text_surf = self.font.render(f"Find a way out of the maze!",False,TEXT_COLOR)
		elif self.current_level == 3:
			text_surf = self.font.render(f"You have {player.inventory['keys']} keys",False,TEXT_COLOR)
		elif self.current_level == 4:
			text_surf = self.font.render(f"Escape!",False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(10,630,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def blit_pixelated_text(self, text, position):
		text_surface = self.pixelated_font.render(text, True, TEXT_COLOR)
		self.display_surface.blit(text_surface, position)

	def magic_overlay(self,magic_index,has_switched):
		bg_rect = self.selection_box(80,635,has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf,magic_rect)

	def show_status_message(self):
		if self.status_message:
			current_time = pygame.time.get_ticks()
			elapsed_time = current_time - self.status_message_start_time

			if elapsed_time < self.status_message_duration:
				text_surface = self.pixelated_font.render(self.status_message, True, TEXT_COLOR)
				x = self.display_surface.get_size()[0] // 2 - text_surface.get_width() // 2
				y = self.display_surface.get_size()[1] - 50
				text_rect = text_surface.get_rect(topleft=(x, y))

				pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
				self.display_surface.blit(text_surface, text_rect)
				pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)
			else:
				self.status_message = ""  # Clear the status message when its duration is over

	def display(self,player):
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)
		self.show_exp(player)
		self.show_status_message()

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
		self.magic_overlay(player.magic_index,not player.can_switch_magic)

	def set_status_message(self, message):
		self.status_message = message
		self.status_message_start_time = pygame.time.get_ticks()
