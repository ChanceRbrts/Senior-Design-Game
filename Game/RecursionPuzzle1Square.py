from Instance import*
class RecursionPuzzle1Square(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.name = "RecursionPuzzle1Square"
	def isInstanceCollide(self, oX, oY, oW, oH):
		if (oX <= self.x+self.xSpace*32 and oX+oW >= self.x
			and oY <= self.y+self.ySpace*32 and oY+oH >= self.y):
			return True
		return False
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,150),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))