import pygame
import sys
import csv
from pprint import pprint
from copy import deepcopy


####################################################################
#   SCENEBASE CLASS
####################################################################
class SceneBase():
    def __init__(self):
        self.next = self

    def ProcessInput(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        pygame.quit()
        sys.exit()





####################################################################
#   LOAD TileMap
####################################################################
class TileMap():
    def __init__(self, tileWidth, tileHeight, image, mapCsv):
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight
        self.tileSetImage = pygame.image.load(image)
        self.mapCsv = mapCsv
        self.tilePositions = []
        self.mapList = self.loadMap()



    def loadMap(self):
        with open(self.mapCsv) as mapFile:
            self.layer = 0
            mapDataCSV = csv.reader(mapFile, delimiter=',')

            # the map as a list of lists, one list per row
            mapList = list(mapDataCSV)

            # get dimensions of tilemap
            self.imgDim = self.tileSetImage.get_rect().size

            # get positions of tiles
            for h in range(0, self.imgDim[1], self.tileHeight):
                for w in range(0, self.imgDim[0], self.tileWidth):
                    pos = (w * -1, h * -1)
                    self.tilePositions.append(pos)

            self.tileSetSurface = pygame.Surface((self.tileHeight, self.tileWidth))

            return mapList


    def Render(self, screen):
        for y in range(0, len(self.mapList)):
            for x in range(0, len(self.mapList[y])):
                tileNum = int(self.mapList[y][x])

                self.tileSetSurface.blit(self.tileSetImage, self.tilePositions[tileNum])
                screen.blit(self.tileSetSurface, (x *self.tileWidth, y * self.tileHeight))




####################################################################
#   A* PATH FINDING
# walkable = list of integers(tiles)
# maplist = the maplist from a Tilemap class
# Start = starting tile in tuple (1,1)
# goal = end tile in tuple ex:(10,10)
####################################################################

# helper funcion to visualize the calculated path
def drawPath(screen, thePath,tileWidth,tileHeight):
    green = (0, 255, 0)
    for x in range(0,len(thePath)):
        next = x+1
        if next <= (len(thePath)-1):
            pygame.draw.line(screen,green,[(thePath[x][0]*tileWidth)+tileWidth/2,(thePath[x][1]*tileHeight)+tileHeight/2],[(thePath[next][0]*tileWidth)+tileWidth/2,(thePath[next][1]*tileHeight)+tileHeight/2],5)


# helper function for the a* pathfinding
def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


# the main pathfinding function
def getPath(mapObject, start, goal, walkable):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),(1,1),(1,-1),(-1,-1),(-1,1)]

    openList = []
    closedList = []

    # create lists of tuple positions on map, place in closed or open list depending on walkable
    for y in range(0,len(mapObject.mapList)):
        for x in  range(0,len(mapObject.mapList[y])):
            tile = (int(x),int(y))
            if int(mapObject.mapList[y][x]) in walkable:
                openList.append(tile)
            else:
                closedList.append(tile)

    closedList.append(start)
    if start in openList:
        openList.remove(start)

    frontier = [start]
    startTile = (start[0],start[1],0)
    visited = []

    if goal in closedList:
        print "cant reach that"
        path = []
        return path
    else:
        done = False
        itteration = 0
        while not done:
            itteration +=50
            horizon = []
            if len(frontier) == 0:
                path = []
                return path
            for t in frontier:
                if t == goal:
                    done = True
                else:
                    if t == start:
                        visited.append(startTile)
                    else:
                        heur = heuristic(t,goal)
                        #itteration = itteration *5
                        cost = heur + itteration
                        visitedTile = (t[0],t[1],cost)
                        #print visitedTile
                        visited.append(visitedTile)
                    for n in neighbors:
                        nTile = (t[0]+n[0],t[1]+n[1])
                        if nTile not in closedList and nTile in openList:
                            horizon.append(nTile)
                            closedList.append(nTile)

            frontier = []
            for t in horizon:
                frontier.append(t)


        ########################################
        # go backwards through the visited list
        # to find the path
        ########################################
        currentTile = (goal[0], goal[1], 0)
        pathReversed=[]
        pathReversed.append(currentTile)
        resetVisited = list(visited)

        blacklist=[]
        while currentTile != startTile:
            frontier=[]
            for n in neighbors:
                nTile = None
                nTilePos = (currentTile[0] + n[0], currentTile[1] + n[1])
                for t in visited:
                    if t[0] == nTilePos[0] and t[1] == nTilePos[1]:
                        nTile = t
                if nTile != None:
                    if nTile in visited and nTile not in blacklist:
                        frontier.append(nTile)
                        visited.remove(nTile)


            if len(frontier) == 0 or (len(frontier) ==1 and frontier[0] == currentTile):
                visited = list(resetVisited)
                blacklist.append(currentTile)
                currentTile = (goal[0], goal[1], 0)
                pathReversed = []

            else:
                cost = None
                for t in frontier:
                    if cost == None:
                        cost = t[2]
                        currentTile = t
                    elif t[2] < cost:
                        currentTile = t
                pathReversed.append(currentTile)


        path = []
        for t in reversed(pathReversed):
            path.append((t[0],t[1]))
        path.append(goal)

        return path




####################################################################
#   The main function to run yor game
####################################################################
def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)




if __name__ == "__main__":
    pass