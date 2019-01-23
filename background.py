import pygame


class Background(pygame.sprite.Sprite):
	def __init__(self, location, path, scale):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		#self.image = pygame.image.load("images/spaceBG.bmp")
		self.image = pygame.image.load(path).convert()
		self.image = pygame.transform.scale(self.image, scale)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location