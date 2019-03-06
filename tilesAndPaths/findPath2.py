def getNeighbours(tile):
    neighbours = []
    if tile != None:
        tileUP = (tile[0],tile[1]-1)
        neighbours.append(tileUP)
        tileRight = (tile[0]+1,tile[1])
        neighbours.append(tileRight)
        tileLeft = (tile[0]-1,tile[1])
        neighbours.append(tileLeft)
        tileDown = (tile[0], tile[1] + 1)
        neighbours.append(tileDown)

        '''
        tileUPLeft = (tile[0] - 1, tile[1] - 1)
        neighbours.append(tileUPLeft)
        tileUPRight = (tile[0] + 1, tile[1] - 1)
        neighbours.append(tileUPRight)
        tileDownLeft = (tile[0] - 1, tile[1] + 1)
        neighbours.append(tileDownLeft)
        tileDownRight = (tile[0] + 1, tile[1] + 1)
        neighbours.append(tileDownRight)
        '''

    return neighbours



def getCost(pos,goal):
    cost = 0
    pos = [pos[0],pos[1]]
    goal = [goal[0],goal[1]]

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



def findPath2(map,walls, start, goal):
    openList = []
    closedList = []

    #add tiles to the lists
    for y in range(0,len(map)):
        for x in range(0,len(map[y])):
            if map[y][x] not in walls:
                openList.append((x,y))
            else:
                closedList.append((x,y))

    #print(closedList)

    path = []
    currentTile = start
    while currentTile != goal:
        neighbourTiles = getNeighbours(currentTile)
        lowestCost = None
        nextTile = None
        for tile in neighbourTiles:
            if tile in openList and tile not in closedList:
                tileCost = getCost(tile,goal)
                if lowestCost == None:
                    lowestCost = tileCost
                    nextTile = tile
                elif tileCost < lowestCost:
                    lowestCost = tileCost
                    nextTile = tile
        if nextTile == None:
            closedList.append(tile)
            currentTile = path[(len(path)-1)]
        else:
            path.append(currentTile)
            if tile in openList:
                openList.remove(currentTile)

            if currentTile not in closedList:
                closedList.append(currentTile)

            currentTile = nextTile

    path.append(goal)
    print(path)
    return path


