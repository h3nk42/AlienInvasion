import sys

import pygame
from pygame.sprite import Group
from button import Button

import game_functions as gf
from settings import Settings
from ship import Ship
from klingon import Klingon
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from background import Background
from movie2 import runMovie
from ending import showPicture

def run_game():
	""" Initialize the game and create a screen object. """

	pygame.init()
	pygame.mixer.music.load('sounds/fight.wav')
	pygame.mixer.music.play(-1)

	ai_settings = Settings()

	screen = pygame.display.set_mode(
			(ai_settings.screen_width,
			 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make the Play button
	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game stats
	stats = GameStats(ai_settings)
	
	# Make a ship.
	ship = Ship(screen, ai_settings)
	# Make a klingon.
	klingon = Klingon(screen)
	# Make a bullet
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	#set the background color
	background = Background([0,0],"images/spaceBG (1).bmp",(1200,800))
	background_2 = Background([0,0],"images/spaceBG.jpg",(1200,800))
	bg_color = ai_settings.bg_color


	#start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
	
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats)
	
			gf.update_aliens(ai_settings,stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, background)
		if stats.game_won == True:
			pygame.mixer.music.stop()
			showPicture(screen,background_2,ai_settings)
			break
runMovie()
run_game()

