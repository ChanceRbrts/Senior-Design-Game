#Okay... This should look familiar.
#This is to get you used to how functions look.
from Solid import*
class FunctionPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle1"
		self.codingStartVisible = [0,10,]
		self.codingEndVisible = [2,14,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def update(self,controlPressed,controlHold):
		self.dY = 0
	def finishUpdate(self):
		self.y += self.dY