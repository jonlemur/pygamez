import pygame
#from tiledMap import TileMap
from lemur import *

def main():

	pygame.init()

	screen = pygame.display.set_mode((600,360))

	clock = pygame.time.Clock()

	running = True

	tileMap = getTileMap(r'C:\Users\JonLemur\Documents\Dev\PyGame\tiled\tiled.json', r'C:\Users\JonLemur\Documents\Dev\PyGame\tiled\tileSet.png',3)

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
