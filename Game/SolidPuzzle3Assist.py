from Solid import*
class SolidPuzzle3Assist(Solid):
    def __init__(self,oX=0,oY=0,oW=1,oH=1):
        Solid.__init__(self,oX,oY,oW,oH)
        self.name = "SolidPuzzle3Assist"
        self.image = pygame.image.load('Game/Sprites/SolidWall.png');
    def update(self,oX=0,oY=0,oW=1,oH=1,oDX=0,oAc=False):
        if (oY < self.y+self.ySpace*32 and oY+oH*32 > self.y and
                oX+oDX+oW*32 > self.x and oX+oW*32 <= self.x and oAc):
            self.x = 0
    def draw(self,Window,viewX,viewY):
        for i in range(0,self.xSpace):
            for j in range(0,self.ySpace):
                Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))