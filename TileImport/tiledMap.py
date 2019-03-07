import json
from pprint import pprint
import pygame

class TileMap:
	
	def __init__(self, tiledJsonFile, tileSetImage):
		self.jsonFile = tiledJsonFile
		self.tileSetImage = pygame.image.load(tileSetImage)
		
		with open(tiledJsonFile) as f:
			self.mapData = json.load(f)

		self.tileSetPositions = self.getTileSetPositions()


	def getTileSetPositions(self):
		# TODO: fix this method, xy tuples of tiles in tileset
		tilePositions = []
		for h in range(0,self.mapData['tilesets'][0]['imageheight'],self.mapData['tileheight']):
			for w in range(0,self.mapData['tilesets'][0]['imagewidth'],self.mapData['tilewidth']):
				pos = (w*-1,h*-1)
				tilePositions.append(pos)
		return tilePositions


	def draw(self, pygameScreen):
		self.tileSetSurface = pygame.Surface((self.mapData['tilewidth'], self.mapData['tileheight']))
		self.tileSetPositions = self.getTileSetPositions()

		for i in range(0,len(self.mapData['layers'][0]['data'])):
			tile = (self.mapData['layers'][0]['data'][i])
			row = int(i/self.mapData['width'])
			col = abs(int(i-(row*self.mapData['width'])))
			#print('r:{}, c:{}, t:{}'.format(str(row),str(col),str(tile)))
			self.tileSetSurface.blit(self.tileSetImage, self.tileSetPositions[tile-1])
			pygameScreen.blit(self.tileSetSurface, (col*self.mapData['tilewidth'], row*self.mapData['tileheight']))
			



if __name__ == "__main__":
	pass