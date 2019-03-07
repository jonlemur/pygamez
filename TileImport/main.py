import pygame
from tiledMap import TileMap


def main():

	pygame.init()

	screen = pygame.display.set_mode((540,580))

	clock = pygame.time.Clock()

	
	running = True

	test = TileMap(r'C:\Users\JonLemur\Documents\Dev\PyGame\TileImport\tiled\tiled.json', r'C:\Users\JonLemur\Documents\Dev\PyGame\TileImport\tiled\tileSet.png')
	test.draw(screen)

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
