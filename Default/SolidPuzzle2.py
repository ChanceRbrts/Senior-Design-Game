from Solid import*
class SolidPuzzle2(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle2"
		self.codingStartVisible = [8]
		self.codingEndVisible = [10]
	def finishUpdate(self):
		self.x = 19*32
		self.y = 3*32
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
