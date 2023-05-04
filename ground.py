import pygame

"""
	Ground block class
"""
class Ground ():
	"""
		Ground object
		Just have a position and coordinates
	"""
	def __init__ (self, sprite_filename, position):
		self.sprite = pygame.image.load(sprite_filename).convert_alpha()
		self.height = self.sprite.get_height ()
		self.width = self.sprite.get_width ()
		self.position = position # Top left on the image

		# Bounding box.
		# Used for testing collision
		upperleft = [self.position[0], self.position[1]]
		lowerright = [self.position[0] + self.width, self.position[1] + self.height]
		#self.rect = [upperleft, lowerright]
		self.rect = [self.position[0] + (self.width / 2.0), self.position[1] + (self.height / 2.0)]

	"""
		Render the block to the screen
	"""
	def render (self, screen, camera):
		screen.blit (self.sprite, (self.position[0] - camera.position[0], self.position[1] - camera.position[1]))

