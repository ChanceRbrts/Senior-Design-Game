#Okay... This should look familiar.
#This is to get you used to how functions look.
from Solid import*
class FunctionPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle1"
		self.codingStartVisible = [0,9,]
		self.codingEndVisible = [2,13,]
	def update(self,controlPressed,controlHold):
		self.dY = 12
	def finishUpdate(self):
		self.y += self.dY
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
