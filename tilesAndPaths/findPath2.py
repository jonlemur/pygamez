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
    return neighbours



def findPath2(map,walls, start, goal):
    openList = []
    closedList = []

    #add tiles to the lists
    for row in map:
        for tile in row:
            if tile not in walls:
                openList.append(tile)
            else:
                closedList.append(tile)

    currentTile = start
    while currentTile != goal:
        neighbourTiles = getNeighbours(currentTile)
        for tile in neighbourTiles:
            if
