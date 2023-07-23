from pickle import OBJ
import time
import math
import random
import pygame

import animation

"""
	Player game class
"""
class Player ():
	epsilon = 0.001		# 'Epsilon test' of 'floating-point numbers'
	walking_speed = 40.0
	jump_boost = 75.0	# Speed of the jump
	max_speed = 500.0
	gravity = 75.0

	"""
		Initialize the Player object.
	"""
	def __init__ (self):
		self.position = [72.0, 72.0]
		self.speed = [0.0, 0.0]
		self.direction = 1
		self.isGrounded = True

		self.hp = 1	# 1 is small, 2 is big, 3 is powerup


		self.anim = animation.Animation ("player", self.hp)

	"""
		Player based game related physics/logic
	"""
	def update (self, clock):

		# Add gravity to the player, he is in the air
		if not self.isGrounded:
			self.speed[1] += Player.gravity * (clock.get_time () / 1000.0)
		else:
			self.speed[1] = 0.0

		# Check if we are moving too fast
		if math.sqrt ((self.speed[0]**2) + (self.speed[1]**2)) > Player.max_speed:
			# Vector Calculus. Divide the velocity(speed) vector by its absolute value (this gets it's direction vector) and multiply by max_speed
			self.speed = [Player.max_speed * self.speed[0] / (math.sqrt ((self.speed[0]**2) + (self.speed[1]**2))), Player.max_speed * self.speed[1] / (math.sqrt ((self.speed[0]**2) + (self.speed[1]**2)))]
			print ("Player moved too fast!")

		self.position[0] += self.speed[0] * (clock.get_time () / 1000.0)
		self.position[1] += self.speed[1] * (clock.get_time () / 1000.0)

		# What animation state are we in
		if not self.isGrounded:
			self.state = "jump"
		elif self.isMoving:
			self.state = "walk"
		else:
			self.state = "idle"
		# Update the animation
		self.anim (clock, self.state, self.hp, self.direction)

	"""
		Render the Player on the screen
	"""
	def render (self, screen, camera):
		self.anim.render (screen, camera, self.position)

	"""
		Player is holding a direction button.
		Move the Player.
	"""
	def move (self, direction):
		if direction == 0:
			self.speed[0] = 0.0
		else:
			self.direction = direction
			self.speed[0] = direction * Player.walking_speed

	"""
		Make the Player jump
	"""
	def jump (self, clock):
		if self.isGrounded:
			self.speed[1] -= Player.jump_boost
			self.isGrounded = False

	"""
		Player lost a life
	"""
	def hurt (self):
		self.hp -= 1

	"""
		Just test if player has collided with item
		item: [center_x, center_y]
	"""
	def collision (self, item):
		if abs (self.position[0] - item[0]) < 14.0 and abs (self.position[1] - item[1]) < 9.0+0.0:
			if self.position[0] < item[0] and self.speed[0] > 0.0:
				self.speed[0] = 0.0
			elif self.position[0] > item[0] and self.speed[0] < 0.0:
				self.speed[0] = 0.0
			
			# Are we standing on top of it?
			if self.position[1] < item[1]:
				self.speed[1] = 0.0
				self.position[1] = item[1] - (9.0 + 0.0)
				self.isGrounded = True
				return True
			elif self.position[1] > item[1] and self.speed[1] < 0.0:
				print ("Boink")
				self.speed[1] = 0.0
				return True
		else:
			return False
		
	"""
		Is the player in motion?
	"""
	@property
	def isMoving (self):
		# Do we have any speed?
		if abs (self.speed[0] - 0.0) < Player.epsilon and abs (self.speed[1] - 0.0) < Player.epsilon:
			self.speed = [0.0, 0.0]
			return False
		else:
			return True

	"""
		Which direction are we facing?
	"""
	"""
	@property
	def direction (self):
		# Remove any nasty floating point
		self.isMoving

		# Is the player moving to the left?
		if self.speed[0] < 0.0:
			return -1
		# Is the player moving to the right?
		elif self.speed[0] > 0.0:
			return 1
		# He is standing still
		else:
			return 0"""
	"""
		Is the player standing on ground?
	""""""
	@property
	def isGrounded (self):
		# We need a function to get block beneath/below the player.
		# Is there a block below player?
		return not self.hasJumped"""
		

