from Solid import*
class SolidPuzzle3Assist(Solid):
    def __init__(self,oX=0,oY=0,oW=1,oH=1):
        Solid.__init__(self,oX,oY,oW,oH)
        self.name = "SolidPuzzle3Assist"
    def update(self,oX=0,oY=0,oW=1,oH=1,oDX=0,oAc=False):
        if (oY < self.y+self.ySpace*32 and oY+oH*32 > self.y and
                oX+oDX+oW*32 > self.x and oX+oW*32 <= self.x and oAc):
            self.x = 0
    def draw(self,Window,viewX,viewY):
            pygame.draw.rect(Window,(0,100,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))