import time
import random
import pygame

import camera
import player

"""
	Game Class
"""
class Game ():
	keyboard = {"A": False,
				"B": False,
				"LEFT": False,
				"RIGHT": False,
				"UP": False,
				"DOWN": False}

	"""
		Initialize all the game stuff.
		Including the gamewindow (pygame)
	"""
	def __init__ (self, resolution = (270, 180)):
		pygame.init ()
		self.screen = pygame.display.set_mode (resolution, flags = (pygame.SCALED | pygame.NOFRAME))
		self.test_sprite = pygame.image.load("gamedata/background.png").convert_alpha()
		self.camera = camera.Camera (resolution, self.test_sprite)
		
		self.player = player.Player ()
		self.tick = 0
		self.clock = pygame.time.Clock ()
		self.clock.tick (30)

	"""
		Start the gameloop
	"""
	def run (self):
		self.run_flag = True

		# This is the game loop
		while self.run_flag == True:
			# This checks keyboard inputs
			self.events ()

			# Update the game logic
			self.update ()

			# Render all the visuals/pictures
			self.render ()

			# A frame has passed
			self.clock.tick (30)
			self.tick += 1

		# Cleanup afterwards
		pygame.quit ()
		quit ()

	"""
		Check for game inputs/events
	"""
	def events (self):
		for event in pygame.event.get ():
			if event.type == pygame.QUIT:
				self.run_flag = False
			# Pressed a key
			elif event.type == pygame.KEYDOWN:
				#print (f"Keydown: {event.key}")
				
				# 113 == 'Q' for quit
				if event.key == 113:
					self.run_flag = False
				elif event.key == 1073741904:
					self.keyboard["LEFT"] = True
				elif event.key == 1073741903:
					self.keyboard["RIGHT"] = True
				elif event.key == 1073741906:
					self.keyboard["UP"] = True
				elif event.key == 1073741905:
					self.keyboard["DOWN"] = True
				# 32 == Spacebar
				elif event.key == 32:
					self.keyboard["A"] = True
			# Released a Key
			elif event.type == pygame.KEYUP:
				if event.key == 1073741904:
					self.keyboard["LEFT"] = False
				elif event.key == 1073741903:
					self.keyboard["RIGHT"] = False
				elif event.key == 1073741906:
					self.keyboard["UP"] = False
				elif event.key == 1073741905:
					self.keyboard["DOWN"] = False
				# 32 == Spacebar
				elif event.key == 32:
					self.keyboard["A"] = False

	
	"""
		Update the gamelogic
	"""
	def update (self):
		# Player input/movement
		if self.keyboard["LEFT"]:
			self.player.move (-1)
		elif self.keyboard["RIGHT"]:
			self.player.move (1)
		else:
			self.player.move (0)

		if self.keyboard["A"]:
			self.player.jump (self.clock)

		self.player.update (self.clock)
		self.camera.update (self.player.position)

	"""
		Render the graphics
	"""
	def render (self):
		DARK_GREY = (45, 45, 45)
		self.screen.fill (DARK_GREY)

		# Background
		self.screen.blit (self.test_sprite, (0, 0))

		self.player.render (self.screen, self.camera)


		# Flip the table
		pygame.display.flip ()

if __name__ == "__main__":
	#answer = input ("Do you want multiplayer? [y/n]")
	game = Game ()
	game.run ()

else:
	print ("ERROR! You need to run main.py as the main file!")
	quit ()
