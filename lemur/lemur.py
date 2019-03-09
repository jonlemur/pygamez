# -*- coding: utf-8 -*-

import json
from pprint import pprint
import pygame

def __getTileSetPositions__(jsonMapData):
		# TODO: fix this method, xy tuples of tiles in tileset
		tilePositions = []
		for h in range(0,jsonMapData['tilesets'][0]['imageheight'],jsonMapData['tileheight']):
			for w in range(0,jsonMapData['tilesets'][0]['imagewidth'],jsonMapData['tilewidth']):
				pos = (w*-1,h*-1)
				tilePositions.append(pos)
		return tilePositions


def getTileMap(tiledJsonFile,tileSetImage, zoom=1):
    tileSetImage = pygame.image.load(tileSetImage)
    
    with open(tiledJsonFile) as f:
        mapData = json.load(f)

    tileSetPositions = __getTileSetPositions__(mapData)

    tileSetSurface = pygame.Surface((mapData['tilewidth'], mapData['tileheight']))
    mapSurface = pygame.Surface((mapData['tilewidth']*mapData['width'], mapData['tileheight']*mapData['height']))

    for i in range(0,len(mapData['layers'][0]['data'])):
        tile = (mapData['layers'][0]['data'][i])
        row = int(i/mapData['width'])
        col = abs(int(i-(row*mapData['width'])))
        #print('r:{}, c:{}, t:{}'.format(str(row),str(col),str(tile)))
        tileSetSurface.blit(tileSetImage, tileSetPositions[tile-1])
        mapSurface.blit(tileSetSurface, (col*mapData['tilewidth'], row*mapData['tileheight']))

    mapSize = mapSurface.get_size()
    scaledMap = pygame.transform.scale(mapSurface,(mapSize[0]*zoom,mapSize[1]*zoom))

    return scaledMap


if __name__ == "__main__":
	pass