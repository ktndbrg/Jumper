from string import printable
import pygame

"""
	Animation system class
"""
class Animation ():
	"""
		Initialize animation system with type and style
		type: "player"	# "enemy" etc
		style: 1		# hp for player, enemy doesn't use this
	"""
	def __init__ (self, types, style = 1):
		self.type = types
		self.style = style
		self.state = "idle"
		self.direction = 0
		self.sprite = pygame.image.load(f"gamedata/{self.type}_{self.style}_{self.state}.png").convert_alpha()
		
		# Animation stuff
		self.px_size = self.sprite.get_height () # Each sprite_frame should be square in size
		self.number_of_sprites = self.sprite.get_width () / self.px_size # How many sprites do we have?
		self.step = True # Are we going up or down the animation ladder
		self.sprite_length = 0.100 # Number of seconds each frame should last
		self.timer = self.sprite_length
		self.frame = 1 # Which frame are we on
		self.rect = [0, 0] # Selection for rendering

	def reset (self):
		# Animation stuff
		self.px_size = self.sprite.get_height () # Each sprite_frame should be square in size
		self.number_of_sprites = self.sprite.get_width () / self.px_size # How many sprites do we have?
		self.step = True # Are we going up or down the animation ladder
		self.sprite_length = 0.100 # Number of seconds each frame should last
		self.timer = self.sprite_length
		self.frame = 1 # Which frame are we on
		self.rect = [0, 0] # Selection for rendering


	"""
		Update the animation system
		style: = 0, 1, 2 # hp for player
		direction: -1, 0, 1
		state: "idle", "walk", "jump"
	"""
	def __call__(self, clock, state = "idle", style = 0, direction = 0):
		if self.detect_change (style, direction, state):
			# Change happened
			self.state = state
			self.style = style
			self.direction = direction
			
			self.sprite = pygame.image.load(f"gamedata/{self.type}_{self.style}_{self.state}.png").convert_alpha()
			# Make it face left
			if self.direction == -1:
				self.sprite = pygame.transform.flip (self.sprite, True, False)
			self.reset ()
		# We can proceed as normal
		else:
			# Fun animation stuff

			self.timer -= (clock.get_time () / 1000.0)
			if self.timer < 0.0 and self.number_of_sprites != 1:
				self.timer = self.sprite_length
				if self.step:
					self.frame += 1
					# Are we done with the 'upwards' animations?
					if self.frame >= self.number_of_sprites:
						# Yes, so go downwards
						self.step = False
				else:
					self.frame -= 1
					# Are we done with the 'downwards' animations?
					if self.frame == 1:
						# Yes, so go upwards
						self.step = True
			
			# Make the rectangle correct, the correct frame for the sprite
			if self.direction == -1:
				self.rect[0] = (self.sprite.get_width() - self.px_size) - (self.frame - 1) * self.px_size
			else:
				self.rect[0] = 0 + (self.frame - 1) * self.px_size
			
	
	"""
		Render the current animation frame onto the screen
	"""
	def render (self, screen, camera, pos):
		screen.blit (self.sprite, (pos[0] - camera.position[0] - self.px_size, pos[1] - camera.position[1] - self.px_size), pygame.Rect (self.rect, (self.px_size, self.px_size)))

	"""
		Did the animation sprite change?
	"""
	def detect_change (self, style, direction, state):
		if self.style != style or self.direction != direction or self.state != state:
			# Something changed
			return True
		else:
			return False
