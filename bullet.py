import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to manage bullets fired from the ship """
	def __init__(self, screen, ai_settings, ship):
		""" Create a bullet object at the ship'‚ current position. """
		super().__init__()
		self.screen = screen
		# Load the ship image and get its rect.
		self.image = pygame.image.load("images/beam.bmp")
		self.image = pygame.transform.scale(self.image, (80,50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		""" Move the bullet up the screen. """
		# Update the decimal postition of the bullet.
		self.y -= self.speed_factor
		#Update the rect position.
		self.rect.y = self.y

	def draw_bullet(self):
		""" Draw the bullet to the screen. """
		self.screen.blit(self.image, self.rect)

	