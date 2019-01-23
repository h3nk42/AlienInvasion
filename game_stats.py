class GameStats():
	"""Track statistics for Alien Invasion"""
	def __init__(self, ai_settings):
		"""init statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# start alien invasion in inacticve state
		self.game_active = False
		self.game_won = False

	def reset_stats(self):
		"""init statistics that can change during the game"""
		self.ships_left = self.ai_settings.ship_limit