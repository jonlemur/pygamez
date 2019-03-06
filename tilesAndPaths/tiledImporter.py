import json
from pprint import pprint
import pygame


def readTiledMap(screen, mapJsonPath,imagePath,layer):

    with open(mapJsonPath) as mapFile:
        layer -= 1
        mapData = json.load(mapFile)
        mapWidth = mapData['layers'][layer]['width']
        mapHeight = mapData['layers'][layer]['height']

        mapList = []

        tileNumber = 0
        row = []
        for tile in mapData['layers'][layer]['data']:
            tileNumber += 1
            row.append(tile)

            if tileNumber == mapWidth:
                mapList.append(row)
                tileNumber = 0
                row = []

        tileWidth = mapData['tilesets'][0]['tilewidth']
        tileHeight = mapData['tilesets'][0]['tileheight']

        # tilepositions will hold all positions for tiles in the current tilemap
        tilePositions = []
        for h in range(0,mapData['tilesets'][0]['imageheight'],tileHeight):
            for w in range(0,mapData['tilesets'][0]['imagewidth'],tileWidth):
                pos = (w*-1,h*-1)
                tilePositions.append(pos)

        tileSetImage = pygame.image.load(imagePath)
        tileSetSurface = pygame.Surface((tileHeight, tileWidth))


        for y in range(0,len(mapList)):
            for x in range(0,len(mapList[y])):
                tileNum = mapList[y][x]
                #print(tilePositions[tileNum-1])
                tileSetSurface.blit(tileSetImage, tilePositions[tileNum-1])
                screen.blit(tileSetSurface, (x*tileWidth, y*tileHeight))


        return mapList



def findNeighbours(tile, map):
    neighbours = []

    '''
    tileUPLeft = (tile[0]-1,tile[1]-1)
    if tileUPLeft[0] > 0 and tileUPLeft[1] >0:
        neighbours.append(tileUPLeft)
        
    tileUPRight = (tile[0]+1,tile[1]-1)
    if tileUPRight[0] < len(map[0]):
        neighbours.append(tileUPRight)
        
    tileDownLeft = (tile[0]-1,tile[1]+1)
    if tileDownLeft[0] > 0 and tileDownLeft[1] < len(map):
        neighbours.append(tileDownLeft)
          
    tileDownRight = (tile[0]+1, tile[1] + 1)
    if tileDownRight[0] > 0 and tileDownRight[1] < len(map):
        neighbours.append(tileDownRight)
    '''
    if tile != None:
        tileUP = (tile[0],tile[1]-1)
        if tileUP[1] > 0:
            neighbours.append(tileUP)

        tileRight = (tile[0]+1,tile[1])
        if tileRight[0] < len(map[0]):
            neighbours.append(tileRight)

        tileLeft = (tile[0]-1,tile[1])
        if tileLeft[0] > 0:
            neighbours.append(tileLeft)

        tileDown = (tile[0], tile[1] + 1)
        if tileDown[1] < len(map):
            neighbours.append(tileDown)

    return neighbours


def calcCost(map,pos,goal):
    cost = 0

    pos = [pos[0],pos[1]]

    while pos != goal:
        cost += 1
        if pos[0] < goal[0]:
            pos[0]+=1
        elif pos[0] > goal[0]:
            pos[0] -= 1
        elif pos[1] < goal[1]:
            pos[1] += 1
        elif pos[1] > goal[1]:
            pos[1] -= 1

        cpos = (pos[0],pos[1])
        if cpos == goal:
            break

    return cost



def findPath(map,start,goal,walls=[1]):
    frontiers = []
    starHistory = []
    frontier = [start]
    visited = []
    wallList = []
    walkable = []

    # sort out coordinates for all wall tiles
    for y in range(0,len(map)):
        for x in range(0,len(map[y])):
            tileValue = map[y][x]
            if tileValue in walls:
                wallList.append((x,y))
            else:
                walkable.append((x,y))

    frontier.append(start)
    Searching = True

    itteration = 0
    while Searching:

        if start not in walkable or goal not in walkable:
            Searching = False
            path = []
            return path

        frontierSave = []
        nextFrontier = []
        itteration += 1
        for tile in frontier:
            if tile == goal:
                Searching = False
                print("GOAL")
            else:
                if tile not in visited and tile not in wallList:
                    c = calcCost(map,tile,goal)
                    c = c+itteration
                    if tile == start:
                        c = 0
                    tileWithCost = {'pos':tile, 'cost': c}
                    if tileWithCost not in starHistory:
                        starHistory.append(tileWithCost)
                    visited.append(tile)
                    tileNeighbours = findNeighbours(tile, map)
                    for tileN in tileNeighbours:
                        if tileN not in walls and tileN not in frontier and tileN not in visited and tileN not in nextFrontier:
                            nextFrontier.append(tileN)

        frontier = []
        for t in nextFrontier:
            frontier.append(t)

        #print(frontier)


    print(starHistory)

    # make path
    path = [goal]
    visited = []
    currentTile = goal


    while currentTile != start:
        tileNeighbours = findNeighbours(currentTile, map)

        nNodes = []
        for n in tileNeighbours:
            if n not in path and n not in visited:
                for tile in starHistory:
                    if tile['pos'] == n:
                        nNodes.append(tile)
                        visited.append(n)

        costs = []
        for tile in nNodes:
            costs.append(tile['cost'])

        costs.sort()
        sorted = []
        for c in costs:
            for tile in nNodes:
                if tile['cost'] == c:
                    if tile not in sorted:
                        sorted.append(tile)

        nextNode = None
        for tile in sorted:
            if nextNode == None:
                if tile not in path:
                    nextNode = tile['pos']

        path.append(nextNode)
        currentTile = nextNode

    print(path)

    path.reverse()
    return path



def drawPath(screen, thePath,tileWidth,tileHeight):
    green = (0, 255, 0)
    for x in range(0,len(thePath)):
        next = x+1
        if next <= (len(thePath)-1):
            pygame.draw.line(screen,green,[(thePath[x][0]*tileWidth)+tileWidth/2,(thePath[x][1]*tileHeight)+tileHeight/2],[(thePath[next][0]*tileWidth)+tileWidth/2,(thePath[next][1]*tileHeight)+tileHeight/2],5)











