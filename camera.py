import pygame

class Camera ():
	"""
	"""
	def __init__ (self, resolution, background_sprite):
		self.resolution = resolution
		self.position = [int (resolution[0] / 2), int (resolution[1] / 2)]
		self.bg_width = background_sprite.get_width()
		self.bg_height = background_sprite.get_height()
	
	"""
		Update the camera position based on players X-coordinate.
		Player *should* always be in the center of the screen.
	"""
	def update (self, position):
		self.position[0] = int (position[0] - self.resolution[0] / 2)
		self.position[1] = int (position[1] - self.resolution[1] / 2)

		# The camera will never move outside the gameworld.
		# This code below ensures it, first left side of screen < 0
		# then right side of screen >
		if self.position[0] < 0:
			self.position[0] = 0
		elif self.position[0] > self.bg_width - self.resolution[0]:
			self.position[0] = self.bg_width - self.resolution[0]

		if self.position[1] < 0:
			self.position[1] = 0
		elif self.position[1] > self.bg_height - self.resolution[1]:
			self.position[1] = self.bg_height - self.resolution[1]
