from Solid import*
from pygame import*
class SolidPuzzle3(Solid):
        def __init__(self,oX=0,oY=0,oW=1,oH=1):
                Solid.__init__(self,oX,oY,oW,oH)
                self.name = "SolidPuzzle3"
                self.ramEverythingDown = False
                self.codingStartVisible = [6,11,13]
                self.codingEndVisible = [7,12,14]
                self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
        def update(self,controlPressed,controlHold):
                self.dX += 0
        def finishUpdate(self):
                self.x += self.dX
        def draw(self,Window,viewX,viewY):
                for i in range(0,self.xSpace):
                        for j in range(0,self.ySpace):
                                Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))
