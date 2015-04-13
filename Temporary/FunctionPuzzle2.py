#This function has a parameter of the
#object blocking your way. It returns
#the object after doing things to it.
#See if you can move the block!
from Solid import*
class FunctionPuzzle2(Solid):
		def __init__(self,oX=0,oY=0,oW=1,oH=1):
			Solid.__init__(self,oX,oY,oW,oH)
			self.name = "FunctionPuzzle2"
			self.codingStartVisible = [0,12]
			self.codingEndVisible = [4,14]
			self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
		def function(self, obj):
			return(obj)
		def draw(self,Window,viewX,viewY):
			pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
		