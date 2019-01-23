import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
	""" Respond to keypresses and mouse events """
	# Watch for keyboard and mouse events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets, stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen,stats, play_button,ship, aliens, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
	""" Respond to key presses """
	print(event.key)
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right.
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# Move the ship to the left.
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# Create a new bullet and add it to the bullets group.
		fire_bullet(ai_settings, screen, ship, bullets, stats)
	elif event.key == pygame.K_q:
		sys.exit()
def check_keyup_events(event, ship):
	""" respond to key releases """

	if event.key == pygame.K_RIGHT:
		# Move the ship to the right.
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		# Move the ship to the left.
		ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, background):
	""" Update images on the screen and flip to the new screen """
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	screen.blit(background.image, background.rect)

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	#klingon.blitme()

	if not stats.game_active:
		play_button.draw_button()

	# Make the most recently drawn screen visibile.
	pygame.display.flip()

def update_bullets(ai_settings,screen, ship, aliens, bullets, stats):
	"""Update pos of bullets and get rid of old ones """
	# Get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))

	# check for any bullets that have hit aliens
	# if so get rid of the bullet and the alien
	check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)

	if len(aliens) == 0:
		stats.game_won = True
		#Destroy existing bullets and create new fleet
		bullets.empty()
		#create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets, stats):
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(screen, ai_settings, ship)
		bullets.add(new_bullet)
		if stats.game_active:
			shoot = pygame.mixer.Sound("sounds/shoot.wav")
			pygame.mixer.Sound.play(shoot)

def create_fleet(ai_settings, screen, ship, aliens):
	""" Create a full fleet of aliens. """
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien witdth.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	print(number_rows)
	

	# Create the first row of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
	""" calc number of aliens in a row """
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	""" Create an alien and place it in the row. """
	# Create an alien and palce it in the row.
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
	aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
	available_space_y = (ai_settings.screen_height -
    					(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	
	return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	check_fleet_edges(ai_settings, aliens)
	""" Update the pos of all aliens in the fleet. """
	aliens.update()


    # Look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge """
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Drop the entire fleet and change the fleets direction. """
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	""" Respond to ship being hit by alien. """
	if stats.ships_left > 0:
		click = pygame.mixer.Sound("sounds/schildHit.wav")
		pygame.mixer.Sound.play(click)
		# Decrement ships_left.
		stats.ships_left -= 1
	
		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()
	
		# Create a new fleet and cneter the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
	
		# pause
		sleep(0.5)
	else:
		click = pygame.mixer.Sound("sounds/schildHit.wav")
		pygame.mixer.Sound.play(click)
		stats.game_active = False
		pygame.mixer.music.stop()
		pygame.mouse.set_visible(True)

	
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	""" check if aliens hit bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# treat this the same as if the ship got hit
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		click = pygame.mixer.Sound("sounds/click.wav")
		pygame.mixer.Sound.play(click)
		pygame.mixer.music.play(-1)
		# Reset the game stats
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		#empty list of aliens and bullets.
		aliens.empty()
		bullets.empty()

		#create new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()


