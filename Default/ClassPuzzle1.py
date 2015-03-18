#...Here it is. The files for the class without
#skipping any code.
from Solid import*
class ClassPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ClassPuzzle1"
		self.codingStartVisible = [0]
		self.codingEndVisible = [16]
	def update(self,controlPressed,controlHold):
		self.dY = 0
	def finishUpdate(self):
		self.y += self.dY
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
