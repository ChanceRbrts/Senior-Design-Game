from Instance import*
class CondPuzzle4Block(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.name = "CondPuzzle4Block"
	def getPos(self,posBlock):
		if (posBlock == 0):
			x = 117*32
		elif (posBlock == 1):
			x = 120*32
		elif (posBlock == 2):
			x = 123*32
	def isInstanceCollide(self, oX, oY, oW, oH):
		if (oX <= self.x+self.xSpace*32 and oX+oW >= self.x
			and oY <= self.y+self.ySpace*32 and oY+oH >= self.y):
			return True
		return False
	
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(50,50,50),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
	