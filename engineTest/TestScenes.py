import pygame
from Lemur import *



#############################################
#
#############################################
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        pass

    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tiled/player01.png")
        self.image.convert_alpha()

    def Render(self, screen):
        screen.blit(self.image,(128,120))



##################################################
#
##################################################
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        tMapImage = "tiled/tileMap1.png"
        tMapData = "tiled/dng1.csv"
        self.tMap = TileMap(32, 32, tMapImage, tMapData)
        self.path = []
        self.start = None
        self.goal = None

        self.player = Player()

        self.zoom = 1.5


    def getTile(self,pos):
        tile = (pos[0]/32,pos[1]/32)
        print tile
        return tile

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(TitleScene())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.start = self.getTile(pygame.mouse.get_pos())
                else:
                    self.goal = self.getTile(pygame.mouse.get_pos())

                if self.start != None and self.goal != None:
                    self.path = getPath(self.tMap, self.start, self.goal, [14, 15, 16, 20, 21, 22])
                    self.start = None
                    self.goal = None

    def Update(self):
        pass

    def Render(self, screen):

        self.tMap.Render(screen)
        if len(self.path)>0:
            drawPath(screen,self.path,32,32)

        self.player.Render(screen)





if __name__ == "__main__":
    pass