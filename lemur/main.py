import pygame
import os
#from tiledMap import TileMap
from lemur import *

def main():

	pygame.init()

	# SET SOME VARS
	CURRENT_PATH =  os.path.dirname(__file__)
	ZOOM = 3

	screen = pygame.display.set_mode((600,360))

	clock = pygame.time.Clock()

	running = True

	print os.path.dirname(__file__)

	tiledJson = CURRENT_PATH + r'\tiled\tiled.json'
	tileMapImage = CURRENT_PATH + r'\tiled\tileSet.png'
	tileMap = getTileMap(tiledJson, tileMapImage,3)

	playerImagePath = CURRENT_PATH + r'\sprites\8bit Player_3.png'
	playerSprite = AnimatedSprite(playerImagePath,16,16,ZOOM)

	screen.blit(tileMap,(0,0))

	pygame.display.flip()

	while running:

		# event handling, gets all event from the eventqueue
		for event in pygame.event.get():
			# only do something if the event if of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False
		
		
		clock.tick(15)



if __name__=="__main__":
	# call the main function
	main()
