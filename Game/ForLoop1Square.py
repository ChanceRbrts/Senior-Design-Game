from Instance import*
class ForLoop1Square(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.name = "ForLoop1Square"
		self.image = pygame.image.load('Game/Sprites/RockBlock.jpg')
	def isInstanceCollide(self, oX, oY, oW, oH):
		if (oX <= self.x+self.xSpace*32 and oX+oW >= self.x
			and oY <= self.y+self.ySpace*32 and oY+oH >= self.y):
			return True
		return False
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))