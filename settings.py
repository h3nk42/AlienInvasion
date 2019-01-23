class Settings():
	""" A class to store all the settings for Alien Invasion."""

	def __init__(self):
		""" Initialize the game's settings. """
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)

		# Ship settings
		self.ship_speed_factor = 5
		self.ship_limit = 0

		# Bullet settings
		self.bullet_speed_factor = 15
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien settings 
		self.alien_speed_factor = 6
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 left
		self.fleet_direction = 1
