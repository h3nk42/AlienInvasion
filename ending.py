from background import Background
from time import sleep
import pygame



def showPicture(screen, background, ai_settings):
	pygame.mixer.music.load('sounds/outro.wav')
	
	while True:
		screen.fill(ai_settings.bg_color)
		screen.blit(background.image, background.rect)
		pygame.display.flip()
		pygame.mixer.music.play(-1)
		sleep(100)
		break
