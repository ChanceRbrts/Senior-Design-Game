from Solid import*
class SolidPuzzle3(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle3"
		self.ramEverythingDown = False
		self.codingStartVisible = [5,9,11]
		self.codingEndVisible = [6,10,12]
	def update(self,controlPressed,controlHold):
		self.dX += 0
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
