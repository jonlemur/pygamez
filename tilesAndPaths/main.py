import pygame

from tiledImporter import *


def main():

    pygame.init()

    screen = pygame.display.set_mode((240,240))

    clock = pygame.time.Clock()

    map01 = readTiledMap(screen,'map01.json','tileset01.png',1)

    path = findPath(map01,(8,9),(9,11),[1])

    drawPath(screen,path,16,16)

    pygame.display.flip()
    running = True

    state = 0
    while running:

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                clickedTile = (int(mousePos[0]/16), int(mousePos[1]/16))
                if state == 0:
                    startTile = clickedTile
                    state = 1
                elif state == 1:
                    endTile = clickedTile
                    state = 0
                    #map01 = readTiledMap(screen, 'map01.json', 'tileset01.png', 1)
                    print(startTile)
                    print(endTile)
                    path = findPath(map01, startTile, endTile, [1])
                    drawPath(screen, path, 16, 16)
                    pygame.display.flip()




        clock.tick(15)



if __name__=="__main__":
    # call the main function
    main()