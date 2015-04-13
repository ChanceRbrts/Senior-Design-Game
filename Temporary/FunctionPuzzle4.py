#The block over there will not change its
#position unless the value is formatted correctly. 
from Solid import*
class FunctionPuzzle4(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle4"
		self.codingStartVisible = [0,13,]
		self.codingEndVisible = [2,18,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def thisIsHowYouCallAFunction(self):
		pass
	
	def valueForOtherObject(self, value):
		#self.thisIsHowYouCallAFunction() <--ignore self
		return(value)
	
	def formatTheValue(self, value):
		return([value,True])
	

	