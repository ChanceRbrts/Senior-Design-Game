#The block over there will not change its
#position unless the value is formatted correctly. 
from Solid import*
class FunctionPuzzle4(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle4"
		self.codingStartVisible = [0,12,]
		self.codingEndVisible = [2,17,]
	def thisIsHowYouCallAFunction(self):
		pass
	
	def valueForOtherObject(self, value):
		#self.thisIsHowYouCallAFunction() <--ignore self
		return(value)
	
	def formatTheValue(self, value):
		return([value,True])
	
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))

	