from Solid import*
class SolidPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle1"
		self.codingStartVisible = [8,11,]
		self.codingEndVisible = [10,13,]
	def update(self,controlPressed,controlHold):
		self.dY = 2
		#LOOK! I'M A COMMENTER!
	def finishUpdate(self):
		self.y += self.dY
		#SEE! I'M A COMMENTER! :D
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
