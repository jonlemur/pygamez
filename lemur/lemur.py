# -*- coding: utf-8 -*-

import json
from pprint import pprint
import pygame



############################################################
# Private function
# Returns list with (x,y) positions of tiles in tile sheet
############################################################
def __getTileSetPositions__(jsonMapData):
		# TODO: fix this method, xy tuples of tiles in tileset
		tilePositions = []
		for h in range(0,jsonMapData['tilesets'][0]['imageheight'],jsonMapData['tileheight']):
			for w in range(0,jsonMapData['tilesets'][0]['imagewidth'],jsonMapData['tilewidth']):
				pos = (w*-1,h*-1)
				tilePositions.append(pos)
		return tilePositions





############################################################
# Public function
# Returns a pygame surface from a tiled json
############################################################
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





############################################################
# Class
# A sprite with animations
############################################################
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spriteSheet,tilewidth, tileHeight, zoom=1):
        
        self.spriteSheet = pygame.image.load(spriteSheet)
        self.tilewidth = tilewidth
        self.tileHeight = tileHeight
        self.spriteImagePositions = []

        # some usual animations
        self.walk = []
        self.run = []
        self.idle = []
        self.jump = []
        self.dead = []
        self.falling = []
        self.attack = []
        # some extra animations if needed
        self.animExtra01 = []
        self.animExtra02 = []
        self.animExtra03 = []


    # save pixel positions of images in sprite sheet
    def getSpritePostitions(self):
        self.tPositions = []        
        self.imageSize = self.spriteSheet.get_rect().size
        for h in range(0,self.imageSize[1],self.tileHeight):
            for w in range(0,self.imageSize[0],self.tilewidth):
                t= (h,w)
                self.spriteImagePositions.append(t)





if __name__ == "__main__":
	pass